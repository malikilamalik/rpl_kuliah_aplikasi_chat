from flask import Blueprint, render_template, request, redirect, url_for,session
from flask_login import login_required,current_user
from website.models.user_group import UserGroup
from website.models.user import User
from website.models.channel import Channel
from website.models.channel_group import ChannelGroup
import uuid
from website import socketio
from flask_socketio import join_room, leave_room, emit

channels = Blueprint('channels',__name__)

@channels.route('/create_channel/<string:id>',methods=['GET', 'POST'])
@login_required
def create_channel(id):
    user = current_user
    # Output message if something goes wrong...
    msg = ''
    # Check if "username" POST requests exist (user submitted form)
    if request.method == 'POST' and 'name' in request.form and 'description' in request.form:
        # Create variables for easy access
        c_id = uuid.uuid1()
        name = request.form['name']
        description = request.form['description']
        new_channel = Channel(id=c_id,name=name,description=description,code=uuid.uuid1())
        user_channel = ChannelGroup(id=uuid.uuid1(),id_group=id,id_channel=c_id)
        user_channel.create()
        new_channel.create()
        msg = 'Channel successfully created!'
        return redirect(url_for('groups.home'))
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('Channels/create_channel.html', msg=msg)

@channels.route('/<string:id>',methods=['GET', 'POST'])
@login_required
def manage_group(id):
    user = current_user
    user_Group = UserGroup.query.filter_by(id_group=id,id_user=user.id).first()
    group_channel = Channel.query\
    .join(ChannelGroup,ChannelGroup.id_channel == Channel.id)\
    .filter(ChannelGroup.id_group == id)\
    .add_columns(Channel.name,Channel.id)

    return render_template('Groups/manage_group.html',channels=group_channel,group_id=id,user_group=user_Group)


@channels.route('/chat',methods=['GET','POST'])
@login_required
def chat():
    if request.method == 'POST' and 'id' in request.form:
        # Create variables for easy access
        user = current_user
        id = request.form['id']
        channel = Channel.query.get(id)
        session['channel'] = channel.name
        session['room'] = channel.code
        return render_template('ChatRoom/channel.html', session = session)
    else:
        return redirect(manage_group)


@channels.route('/hapus_channel/<string:group_id>/<string:channel_id>',methods=['GET'])
@login_required
def delete_Channel(group_id,channel_id):
    channel = Channel.query.get(channel_id)
    user_channel = ChannelGroup.query.filter_by(id_channel=channel_id,id_group=group_id).first()
    channel.delete()
    user_channel.delete() 
    return redirect(url_for('groups.home'))

@socketio.on('join', namespace='/channels/chat')
def join(message):
    room = session.get('room')
    join_room(room)


@socketio.on('text', namespace='/channels/chat')
def text(message):
    room = session.get('room')
    emit('message', {'msg': session.get('username') + ' : ' + message['msg']}, room=room)


@socketio.on('left', namespace='/channels/chat')
def left(message):
    room = session.get('room')
    username = session.get('username')
    leave_room(room)
    session.clear()
    emit('status', {'msg': username + ' has left the room.'}, room=room)


from website.models.user_blocked import BlockedUser
from flask import Blueprint, render_template, request, redirect, url_for, session
from flask_login import login_required,current_user
from website.models.user_friend import UserFriend
from website.models.user import User
from website.models.user_blocked import BlockedUser
from website import socketio
from flask_socketio import join_room, leave_room, emit
import uuid

users = Blueprint('users',__name__)

@users.route('/')
@login_required
def home():
    user = current_user
    blocked_user = BlockedUser.query\
    .join(User, BlockedUser.id_user_blocked == User.id)\
    .filter(BlockedUser.id_user == user.id)\
    .add_columns(User.username,BlockedUser.id)
    
    user_teman = UserFriend.query\
    .join(User, UserFriend.id_user == User.id)\
    .filter(UserFriend.id_user_teman == user.id)\
    .add_columns(User.username,UserFriend.id)
    return render_template('AddFriend/main.html',friends=user_teman,blocked=blocked_user)

@users.route('/tambah_teman',methods=['GET', 'POST'])
@login_required
def add_new_friend():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form:
        # Create variables for easy access
        username = request.form['username']
        # Check if account exists using MySQL
        user_friend = User.query.filter_by(username=username).first()
        user = current_user
        # If account exists show error and validation checks
        if not user_friend:
            msg = 'Account do not exists!'
        elif not username:
            msg = 'Please fill out the form!'
        else:
            user_room = uuid.uuid1()
            add_user_friend = UserFriend(id = uuid.uuid1(),id_user=user.id,id_user_teman=user_friend.id,user_room=user_room)
            add_user_friend.create()
            add_user_friend = UserFriend(id = uuid.uuid1(),id_user=user_friend.id,id_user_teman=user.id,user_room=user_room)
            add_user_friend.create()
            return redirect(url_for('users.home'))
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('AddFriend/add_new_friend.html', msg=msg)

@users.route('/hapus_teman/<string:id>',methods=['GET'])
@login_required
def delete_friend(id):
    user = current_user
    user_friend = UserFriend.query.get(id)
    get_user_friend = UserFriend.query.filter_by(id_user=user.id,id_user_teman=user_friend.id_user).first()
    user_friend.delete()
    get_user_friend.delete() 
    return redirect(url_for('users.home'))

@users.route('/blokir_teman/<string:id>',methods=['GET'])
@login_required
def blocked_user(id):
    user = current_user
    user_friend = UserFriend.query.get(id)
    get_user_friend = UserFriend.query.filter_by(id_user=user.id,id_user_teman=user_friend.id_user).first()
    bloked_friend = BlockedUser(id=uuid.uuid1(),id_user=user.id,id_user_blocked=user_friend.id_user)
    bloked_friend.create()
    user_friend.delete()
    get_user_friend.delete() 
    return redirect(url_for('users.home'))

@users.route('/unblokir_teman/<string:id>',methods=['GET'])
@login_required
def unblocked_user(id):
    user = current_user
    blocked_friend = BlockedUser.query.get(id)
    user_friend = User.query.filter_by(id=blocked_friend.id_user_blocked).first()
    user_room = uuid.uuid1()
    add_user_friend = UserFriend(id = uuid.uuid1(),id_user=user.id,id_user_teman=user_friend.id,user_room=user_room)
    add_user_friend.create()
    add_user_friend = UserFriend(id = uuid.uuid1(),id_user=user_friend.id,id_user_teman=user.id,user_room=user_room)
    add_user_friend.create()
    blocked_friend.delete()

    return redirect(url_for('users.home'))

@users.route('/chat',methods=['GET','POST'])
@login_required
def chat():
    if request.method == 'POST' and 'id' in request.form:
        # Create variables for easy access
        id = request.form['id']
        user = current_user
        user_friend = UserFriend.query.get(id)
        session['username'] = user.username
        session['room'] = user_friend.user_room
        return render_template('ChatRoom/main.html', session = session)
    else:
        return render_template('ChatRoom/main.html', session = session)

@socketio.on('join', namespace='/users/chat')
def join(message):
    room = session.get('room')
    join_room(room)


@socketio.on('text', namespace='/users/chat')
def text(message):
    room = session.get('room')
    emit('message', {'msg': session.get('username') + ' : ' + message['msg']}, room=room)


@socketio.on('left', namespace='/users/chat')
def left(message):
    room = session.get('room')
    username = session.get('username')
    leave_room(room)
    session.clear()
    emit('status', {'msg': username + ' has left the room.'}, room=room)

from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required,current_user
from website.models.user_group import UserGroup
from website.models.user import User
import uuid

@channels.route('/')
@login_required
def home():

    return render_template('Channels/main.html')

@channels.route('/create_channel',methods=['GET', 'POST'])
@login_required
def create_channel():
    user = current_user
    # Output message if something goes wrong...
    msg = ''
    # Check if "username" POST requests exist (user submitted form)
    if request.method == 'POST' and 'name' in request.form and 'description' in request.form:
        # Create variables for easy access
        id = uuid.uuid1()
        name = request.form['name']
        description = request.form['description']
        new_channel = Channel(id=id,name=name,description=description)
        user_channel = UserChannel(id=uuid.uuid1(),id_user=user.id,id_channel=id,role='admin')
        user_channel.create()
        new_channel.create()
        msg = 'Channel successfully created!'

    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('Groups/create_group.html', msg=msg)
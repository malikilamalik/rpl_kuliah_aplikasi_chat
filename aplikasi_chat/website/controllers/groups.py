from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required,current_user
from website.models.user_friend import UserFriend
from website.models.user import User
from website.models.group import Group
from website.models.user_group import UserGroup
import uuid

groups = Blueprint('groups',__name__)

@groups.route('/')
@login_required
def home():
    return render_template('Groups/main.html')

@groups.route('/create_group',methods=['GET', 'POST'])
@login_required
def create_group():
    user = current_user
    # Output message if something goes wrong...
    msg = ''
    # Check if "username" POST requests exist (user submitted form)
    if request.method == 'POST' and 'name' in request.form and 'description' in request.form:
        # Create variables for easy access
        id = uuid.uuid1()
        name = request.form['name']
        description = request.form['description']
        new_group = Group(id=id,name=name,description=description)
        user_group = UserGroup(id=uuid.uuid1(),id_user=user.id,id_group=id,role='admin')
        user_group.create()
        new_group.create()
        msg = 'Group successfully created!'

    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('Groups/create_group.html', msg=msg)
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
    user = current_user
    user_group_admin = UserGroup.query\
    .join(Group, UserGroup.id_group == Group.id)\
    .filter(UserGroup.id_user == user.id)\
    .filter(UserGroup.role == 'admin')\
    .add_columns(Group.id,Group.name,Group.description)
    return render_template('Groups/main.html',group_admin = user_group_admin)

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

@groups.route('/hapus_group/<string:id>',methods=['GET'])
@login_required
def delete_group(id):
    user = current_user
    group = Group.query.get(id)
    user_Group = UserGroup.query.filter_by(id_group=id,id_user=user.id).first()
    group.delete()
    user_Group.delete() 
    return redirect(url_for('groups.home'))
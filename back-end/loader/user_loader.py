from model.user import User
@login_manager.user_loader
def user_loader(id):
    return User.query.get(id)
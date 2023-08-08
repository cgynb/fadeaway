import rain_orm
from rain_orm.column import Int, VarChar

rain_orm.connect(host="localhost", port=3306, user="root", password="123456", database="todo")


class UserModel(rain_orm.Table):
    __table__ = "users"
    __fields__ = {
        "id": Int(auto_increment=True, primary_key=True),
        "name": VarChar(30, unique=True),
        "password": VarChar(200),
    }


class TodoModel(rain_orm.Table):
    __table__ = "todos"
    __fields__ = {
        "id": Int(auto_increment=True, primary_key=True),
        "user_id": Int(foreign_key=UserModel.id),
        "title": VarChar(30),
        "content": VarChar(500)
    }



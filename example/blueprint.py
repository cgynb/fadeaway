from fadeaway import Blueprint, jsonify, Context
from models import TodoModel
todo_bp = Blueprint(name="todo", url_prefix="/todo")


@todo_bp.route("/", methods=("GET", "POST", "DELETE"))
def todo(ctx: Context):
    if ctx.request.method == "GET":
        user = ctx.get("user")
        todos = TodoModel().where("user_id = ?", user.id).all()
        rv = jsonify({
            "code": 200,
            "msg": "ok",
            "data": {
                "todos": [t.instance for t in todos]
            }
        })
    elif ctx.request.method == "POST":
        user = ctx.get("user")
        t = TodoModel(user_id=user.id, title=ctx.request.form.get("title"), content=ctx.request.form.get("content"))
        if t.create():
            rv = jsonify({
                "code": 200,
                "msg": "ok",
                "data": None
            })
        else:
            rv = jsonify({
                "code": 400,
                "msg": "fail",
                "data": None
            })
    elif ctx.request.method == "DELETE":
        todo_id = int(ctx.request.form.get("todo_id"))
        t = TodoModel().where("id = ?", todo_id).one()
        if t.delete():
            rv = jsonify({
                "code": 200,
                "msg": "ok",
                "data": None
            })
        else:
            rv = jsonify({
                "code": 400,
                "msg": "fail",
                "data": None
            })
    return rv


@todo_bp.route("/title", methods=("PUT", ))
def update_title(ctx: Context):
    todo_id = int(ctx.request.form.get("todo_id"))
    t = TodoModel().where("id = ?", todo_id).one()
    t.title = ctx.request.form.get("title")
    return jsonify({
        "code": 200,
        "msg": "ok",
        "data": None
    })


@todo_bp.route("/content", methods=("PUT", ))
def update_content(ctx: Context):
    todo_id = int(ctx.request.form.get("todo_id"))
    t = TodoModel().where("id = ?", todo_id).one()
    t.content = ctx.request.form.get("content")
    return jsonify({
        "code": 200,
        "msg": "ok",
        "data": None
    })

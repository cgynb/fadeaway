from fadeaway import FadeAway, jsonify
import rain_orm
from models import UserModel, TodoModel
from middleware import AuthMiddleWare
from blueprint import todo_bp

rain_orm.Table.auto_migrate(UserModel, TodoModel)
app = FadeAway()
app.use(AuthMiddleWare())
app.register_blueprint(todo_bp)


@app.route("/user/register", methods=("POST", ))
def register(ctx):
    user = UserModel(name=ctx.request.form.get("name"), password=ctx.request.form.get("password"))
    ok = user.create()
    if ok:
        return jsonify({
            "code": 200,
            "msg": "ok",
            "data": {
                "user": user.instance
            }
        })
    else:
        return jsonify({
            "code": 400,
            "msg": "error",
            "data": None
        })


@app.route("/user/login", methods=("POST", ))
def login(ctx):
    user = UserModel().where("name = ?", ctx.request.form.get("name")).one()
    print(user)
    ctx.set("user", user)
    if user is not None:
        return jsonify({
            "code": 200,
            "msg": "ok",
            "data": {
                "user": user.instance
            }
        })
    else:
        return jsonify({
            "code": 400,
            "msg": "error",
            "data": None
        })


if __name__ == "__main__":
    app.run(debug=False)

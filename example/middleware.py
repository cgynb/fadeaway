import jwt
from fadeaway import MiddleWare
from models import UserModel


class AuthMiddleWare(MiddleWare):
    def before(self, ctx):
        token = ctx.request.headers.get("Authorization")
        user = self.validate_token(token)
        if user is not None:
            user = UserModel().where("id = ?", user.get("id")).one()
            ctx.set("user", user)

    def after(self, ctx):
        if ctx.get("user") is not None:
            user = ctx.get("user")
            token = self.generate_token(user)
            ctx.response.headers["Authorization"] = token

    @staticmethod
    def generate_token(user):
        return jwt.encode(payload={
            "id": user.id,
            "name": user.name
        }, key="secret_key", algorithm="HS256")

    @staticmethod
    def validate_token(token):
        try:
            user = jwt.decode(token, key="secret_key", algorithms="HS256")
        except Exception:
            user = None
        return user

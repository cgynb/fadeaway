# blueprint

A large application should clearly divide the modules, which is the meaning of the blueprint.

## apis
- route

### route

Use the same way as **fadeaway.FadeAway.route**

```python
from fadeaway import BluePrint
user_bp = BluePrint(name="user_bp", url_prefix="/user")

@user_bp.route("/user", methods=("GET", ))
def user(ctx):
    ...
    return "user"
```

[finish](https://github.com/cgynb/fadeaway)

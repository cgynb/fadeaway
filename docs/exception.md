# exception

## apis

- abort
- error_handler

### abort

Use **fadeaway.abort** to raise HTTPException to end view function

```python
@app.route("/user", methods=("GET", ))
def user(ctx):
    user_id = ctx.request.args.get("user_id")
    user = get_user(user_id)
    if user is None:
        abort(404)
    else:
        return "success"
```

### error_handler

Use **fadeaway.FadeAway.error_handler** to custom error response

```python
@app.error_handler(404)
def handle_404(e):
    return jsonify({
        "code": 404,
        "msg": "not found",
        "data": None
    })
```

go next: [blueprint](blueprint.md)
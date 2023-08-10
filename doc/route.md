# route

As you're familiar with, use decorators to register routes

example:

```python
@app.route("/", methods=("GET", ))
def hello(ctx):
    return "hello"
```
View functions need to take one args ctx as Context(more details at [context](context.md)).

View functions need to return data of these types(Response, dict, list, str, bytes, bytearray).

1. If return data is instance of dict or list, program will automatically convert it to json
2. If return data is instance of Response(redirect, jsonify...), the data will not be changed
3. If return data is instance of str, bytes or bytearray, program will automatically convert it to Response


go next: [config](config.md)

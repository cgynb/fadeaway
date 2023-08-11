# response 

## apis

- make_response
- jsonify
- redirect

#### make_response

you can use **fadeaway.make_response** to get Response object and custom your response.

```python
@app.route("/")
def hello(ctx):
    response = make_response("hello")
    response.headers["key"] = "value"
    return response
```

#### jsonify

A easy way to response json data.

```python
@app.route("/")
def hello(ctx): 
    response = jsonify({
        "code": 200,
        "message": "ok",
        "data": None
    })
    return response
```

go next: [context](context.md)

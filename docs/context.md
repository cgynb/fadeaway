# context

## Lifetime 

When your application begins handling a request, it pushes a context. And when the request ends, it will be destroyed.

## Attributes

- current_app
- request [more details](https://werkzeug.palletsprojects.com/en/2.3.x/wrappers/#werkzeug.wrappers.Request)
- response [more details](https://werkzeug.palletsprojects.com/en/2.3.x/wrappers/#werkzeug.wrappers.Response)
- g (read-only)

### set

```python
ctx.key = value
ctx.set("key", value)
```

### get

```python
ctx.key
ctx.get(key)
# use ctx.g to get all data you set
ctx.g
```

go next: [exception](exception.md)

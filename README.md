# FadeAway

## Install

it's easy to install via pip

```
pip install fadeaway
```

## Simple Example

```python
from fadeaway import FadeAway, Context

app = FadeAway()

@app.route("/", methods=("GET", ))
def hello(ctx: ConText):
    return "hello"

if __name__ == "__main__":
    app.run()
```

## Link

- document:  [docs](docs/start.md)
- example: [example](example/app.py)

# config

You can set secret key, database information by using object **fadeaway.FadeAway.config**

### set

normally set

```python
config.key = value
config[key] = value
```

from object

```python
config = type("config", (), {"secret_key": "key"})
config.from_object(config)
```

from file

```python
"""
config.json

{
    "secret_key": "key",
}
"""
import json
config.from_file("config.json", json.loads)
```

### get

```python
config.key
config["key"]
```

go next: [response](response.md)

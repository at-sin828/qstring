# qstring

Parse a query string into a dict of lists, and build one back.

Repeated keys stay in order. Blank values are kept. A leading `?` is optional.

```python
from qstring import parse_query, build_query, first_value, without_key

parse_query("tag=a&tag=b")
build_query({"tag": ["a", "b"]})
first_value({"tag": ["a", "b"]}, "tag")  # "a"
without_key({"tag": ["a"], "q": [""]}, "tag")  # {"q": [""]}
```

```bash
python -m unittest test_qstring.py
```

MIT

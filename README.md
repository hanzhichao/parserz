# parserz
Easy parser for parse template $variable

## Features

- Support do dots for fileds

## Install
```
$ pip install  parserz
```

## Use
### Simple Use

```python
from parserz import parser
data = ['$a.1.c', '$b']
context = {
    'a': [1, {'c': 'hello'}],
    'b': 123456
}
result = parser.parse(data, context)
print(result)
```
output:
```
['hello', 123456]
```
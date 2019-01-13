# xdaLibs

> A helping-tool library for personal

## Packing

Install requirements for packing

```sh
pip install twine
pip install wheel
```

Packing into wheels

```sh
python setup.py bdist_wheel --universal
```

If there's a `setup.cfg`like this:

```ini
[bdist_wheel]
universal=1
```

That's OK: 

```sh
python setup.py bdist_wheel 
```

## Uploading

```sh
twine upload dist/*
```

## Installation

```sh
pip install -U xdaLibs
```

## Tests

See `/tests/*.py`

## LICENSE

MIT
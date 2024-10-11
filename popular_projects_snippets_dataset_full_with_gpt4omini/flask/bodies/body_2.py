# Extracted from ./data/repos/flask/src/flask/ctx.py
try:
    del self.__dict__[name]
except KeyError:
    raise AttributeError(name) from None

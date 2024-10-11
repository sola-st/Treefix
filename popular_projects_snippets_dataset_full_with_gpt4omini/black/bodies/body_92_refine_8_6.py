self = type('Mock', (object,), {'__class__': type('MockClass', (object,), {})})() # pragma: no cover

self = type('Mock', (object,), {'__class__': type('MockClass', (object,), {})})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
"""
        Yields:
            All ranges of @string which, if @string were to be split there,
            would result in the splitting of an \\N{...} expression (which is NOT
            allowed).
        """
# True - the previous backslash was unescaped
# False - the previous backslash was escaped *or* there was no backslash
previous_was_unescaped_backslash = False
_l_(4293)
it = iter(enumerate(string))
_l_(4294)
for idx, c in it:
    _l_(4309)

    if c == "\\":
        _l_(4297)

        previous_was_unescaped_backslash = not previous_was_unescaped_backslash
        _l_(4295)
        continue
        _l_(4296)
    if not previous_was_unescaped_backslash or c != "N":
        _l_(4300)

        previous_was_unescaped_backslash = False
        _l_(4298)
        continue
        _l_(4299)
    previous_was_unescaped_backslash = False
    _l_(4301)

    begin = idx - 1  # the position of backslash before \N{...}
    _l_(4302)  # the position of backslash before \N{...}
    for idx, c in it:
        _l_(4307)

        if c == "}":
            _l_(4305)

            end = idx
            _l_(4303)
            break
            _l_(4304)
    else:
        # malformed nameescape expression?
        # should have been detected by AST parsing earlier...
        raise RuntimeError(f"{self.__class__.__name__} LOGIC ERROR!")
        _l_(4306)
    aux = (begin, end)
    _l_(4308)
    exit(aux)

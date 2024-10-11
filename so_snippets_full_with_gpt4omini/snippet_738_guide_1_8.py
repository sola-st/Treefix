filepath = '/path/to/somefile.py' # pragma: no cover
globals = {} # pragma: no cover
locals = None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/436198/what-is-an-alternative-to-execfile-in-python-3
from l3.Runtime import _l_
def execfile(filepath, globals=None, locals=None):
    _l_(2687)

    if globals is None:
        _l_(2683)

        globals = {}
        _l_(2682)
    globals.update({
        "__file__": filepath,
        "__name__": "__main__",
    })
    _l_(2684)
    with open(filepath, 'rb') as file:
        _l_(2686)

        exec(compile(file.read(), filepath, 'exec'), globals, locals)
        _l_(2685)

# Execute the file.
execfile("/path/to/somefile.py")
_l_(2688)


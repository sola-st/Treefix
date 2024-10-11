import io # pragma: no cover
import builtins # pragma: no cover

filepath = '/path/to/somefile.py' # pragma: no cover
globals = {} # pragma: no cover
globals.update({'__file__': filepath, '__name__': '__main__'}) # pragma: no cover
mock_file_content = b'print("Hello from somefile.py")' # pragma: no cover
class MockFile:# pragma: no cover
    def __init__(self, content):# pragma: no cover
        self.content = content# pragma: no cover
    def read(self):# pragma: no cover
        return self.content# pragma: no cover
    def __enter__(self):# pragma: no cover
        return self# pragma: no cover
    def __exit__(self, exc_type, exc_value, traceback):# pragma: no cover
        pass # pragma: no cover
builtins.open = lambda f, mode: MockFile(mock_file_content) if f == filepath and mode == 'rb' else builtins.open(f, mode) # pragma: no cover

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


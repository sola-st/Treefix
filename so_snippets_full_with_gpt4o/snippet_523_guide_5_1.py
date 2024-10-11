import builtins # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/944592/best-practice-for-using-assert
from l3.Runtime import _l_
try:
    _l_(14333)

    assert False
    _l_(14329)
    raise Exception('Python assertions are not working. This tool relies on Python assertions to do its job. Possible causes are running with the "-O" flag or running a precompiled (".pyo" or ".pyc") module.')
    _l_(14330)
except AssertionError:
    _l_(14332)

    pass
    _l_(14331)


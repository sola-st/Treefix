# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/944592/best-practice-for-using-assert
from l3.Runtime import _l_
try:
    _l_(2574)

    assert False
    _l_(2570)
    raise Exception('Python assertions are not working. This tool relies on Python assertions to do its job. Possible causes are running with the "-O" flag or running a precompiled (".pyo" or ".pyc") module.')
    _l_(2571)
except AssertionError:
    _l_(2573)

    pass
    _l_(2572)


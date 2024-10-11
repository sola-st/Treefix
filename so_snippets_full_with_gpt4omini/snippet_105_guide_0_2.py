import mock # pragma: no cover
from unittest.mock import MagicMock # pragma: no cover

ScriptProfilerPy = type('MockScriptProfiler', (object,), {'__init__': lambda self, path: None, 'Profiler': MagicMock()}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/582336/how-do-i-profile-a-python-script
from l3.Runtime import _l_
try:
    from speed_testpy import ScriptProfilerPy
    _l_(917)

except ImportError:
    pass

ScriptProfilerPy("path_to_your_script_to_test.py").Profiler()
_l_(918)


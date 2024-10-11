import os # pragma: no cover
from unittest.mock import MagicMock # pragma: no cover

class MockProfiler:  # Mocking the expected class methods and attributes# pragma: no cover
    def __init__(self, script_path):# pragma: no cover
        self.script_path = script_path# pragma: no cover
# pragma: no cover
    def Profiler(self):# pragma: no cover
        print(f'Profiling script at: {self.script_path}')# pragma: no cover
# pragma: no cover
SpeedTestMock = type('Mock', (object,), {'ScriptProfilerPy': MockProfiler}) # pragma: no cover
ScriptProfilerPy = SpeedTestMock.ScriptProfilerPy # pragma: no cover

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


class ScriptProfilerPy: # pragma: no cover
    def __init__(self, script_path): # pragma: no cover
        self.script_path = script_path # pragma: no cover
 # pragma: no cover
    def Profiler(self): # pragma: no cover
        print(f"Profiling {self.script_path}") # pragma: no cover

 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/582336/how-do-i-profile-a-python-script
from l3.Runtime import _l_
try:
    from speed_testpy import ScriptProfilerPy
    _l_(12850)

except ImportError:
    pass

ScriptProfilerPy("path_to_your_script_to_test.py").Profiler()
_l_(12851)


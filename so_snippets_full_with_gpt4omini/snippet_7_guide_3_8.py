import subprocess # pragma: no cover
import sys # pragma: no cover

with open('longtask.py', 'w') as f: f.write(longtask_script) # pragma: no cover
DETACHED_PROCESS = 0x00000008 # pragma: no cover
class MockProcess: pass # pragma: no cover
subprocess.Popen = lambda *args, **kwargs: MockProcess() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/89228/how-do-i-execute-a-program-or-call-a-system-command
from l3.Runtime import _l_
try:
    import subprocess
    _l_(198)

except ImportError:
    pass
try:
    import sys
    _l_(200)

except ImportError:
    pass

# Some code here

pid = subprocess.Popen([sys.executable, "longtask.py"]) # Call subprocess
_l_(201) # Call subprocess

# Some more code here

DETACHED_PROCESS = 0x00000008
_l_(202)

pid = subprocess.Popen([sys.executable, "longtask.py"],
                       creationflags=DETACHED_PROCESS).pid
_l_(203)

pid = subprocess.Popen([sys.executable, "longtask.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
_l_(204)


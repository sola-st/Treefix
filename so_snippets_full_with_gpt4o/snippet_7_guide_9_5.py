import subprocess # pragma: no cover
import sys # pragma: no cover

sys.executable = sys.executable # pragma: no cover
DETACHED_PROCESS = 0x00000008 # pragma: no cover
class MockPopen: # pragma: no cover
    def __init__(self, cmd, *args, creationflags=None, stdout=None, stderr=None, stdin=None, **kwargs): # pragma: no cover
        self.pid = 1234 # pragma: no cover
        self.stdout = stdout # pragma: no cover
        self.stderr = stderr # pragma: no cover
        self.stdin = stdin # pragma: no cover
        if creationflags == DETACHED_PROCESS: # pragma: no cover
            print(f'Detached process {cmd} executed.') # pragma: no cover
    def wait(self): # pragma: no cover
        return # pragma: no cover
subprocess.Popen = MockPopen # pragma: no cover
with open('longtask.py', 'w') as f: # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/89228/how-do-i-execute-a-program-or-call-a-system-command
from l3.Runtime import _l_
try:
    import subprocess
    _l_(11966)

except ImportError:
    pass
try:
    import sys
    _l_(11968)

except ImportError:
    pass

# Some code here

pid = subprocess.Popen([sys.executable, "longtask.py"]) # Call subprocess
_l_(11969) # Call subprocess

# Some more code here

DETACHED_PROCESS = 0x00000008
_l_(11970)

pid = subprocess.Popen([sys.executable, "longtask.py"],
                       creationflags=DETACHED_PROCESS).pid
_l_(11971)

pid = subprocess.Popen([sys.executable, "longtask.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
_l_(11972)


import shlex # pragma: no cover
import subprocess # pragma: no cover

command = 'example command' # pragma: no cover
unicode = type(u'') # pragma: no cover
shlex.split = lambda x: x.split() # pragma: no cover
subprocess.PIPE = -1 # pragma: no cover
subprocess.STDOUT = -2 # pragma: no cover
subprocess.Popen = type('MockPopen', (object,), { # pragma: no cover
'__init__': lambda self, args, stdout, stderr: None, # pragma: no cover
'stdout': None, # pragma: no cover
'stderr': None # pragma: no cover
}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4789837/how-to-terminate-a-python-subprocess-launched-with-shell-true
from l3.Runtime import _l_
if isinstance(command, unicode):
    _l_(13639)

    cmd = command.encode('utf8')
    _l_(13638)
args = shlex.split(cmd)
_l_(13640)

p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
_l_(13641)


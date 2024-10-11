import shlex # pragma: no cover
import subprocess # pragma: no cover

command = u'test command' # pragma: no cover
unicode = str # pragma: no cover
shlex = type('Mock', (object,), {'split': lambda self, s: s.split()})() # pragma: no cover
subprocess = type('Mock', (object,), {'Popen': lambda *args, **kwargs: type('MockProcess', (object,), {'stdout': 1})(), 'PIPE': 1, 'STDOUT': 2})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4789837/how-to-terminate-a-python-subprocess-launched-with-shell-true
from l3.Runtime import _l_
if isinstance(command, unicode):
    _l_(1437)

    cmd = command.encode('utf8')
    _l_(1436)
args = shlex.split(cmd)
_l_(1438)

p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
_l_(1439)


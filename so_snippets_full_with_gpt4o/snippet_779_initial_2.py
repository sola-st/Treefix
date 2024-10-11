import subprocess # pragma: no cover
import shlex # pragma: no cover

command = 'echo Hello World' # pragma: no cover
unicode = str # pragma: no cover
shlex = type('Mock', (object,), {'split': lambda cmd: cmd.split()}) # pragma: no cover
subprocess = type('Mock', (object,), {'Popen': lambda args, stdout, stderr: type('MockPopen', (object,), {'stdout': type('MockPipe', (object,), {}), 'stderr': type('MockPipe', (object,), {})})(), 'PIPE': None, 'STDOUT': None}) # pragma: no cover

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


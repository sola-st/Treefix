import subprocess # pragma: no cover
import shlex # pragma: no cover

command = 'example_command --option value' # pragma: no cover
unicode = str # pragma: no cover
cmd = command.encode('utf8') # pragma: no cover

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


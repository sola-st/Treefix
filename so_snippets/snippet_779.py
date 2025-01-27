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


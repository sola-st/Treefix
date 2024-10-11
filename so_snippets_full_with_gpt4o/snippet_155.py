# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4760215/running-shell-command-and-capturing-the-output
from l3.Runtime import _l_
try:
    import os
    _l_(14131)

except ImportError:
    pass

def bash(command):
    _l_(14134)

    output = os.popen(command).read()
    _l_(14132)
    aux = output
    _l_(14133)
    return aux

print_me = bash('ls -l')
_l_(14135)
print(print_me)
_l_(14136)


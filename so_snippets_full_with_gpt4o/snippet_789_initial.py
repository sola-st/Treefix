# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3503879/assign-output-of-os-system-to-a-variable-and-prevent-it-from-being-displayed-on
from l3.Runtime import _l_
try:
    from subprocess import PIPE, run
    _l_(12232)

except ImportError:
    pass

def out(command):
    _l_(12235)

    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    _l_(12233)
    aux = result.stdout
    _l_(12234)
    return aux

my_output = out("echo hello world")
_l_(12236)
# Or
my_output = out(["echo", "hello world"])
_l_(12237)


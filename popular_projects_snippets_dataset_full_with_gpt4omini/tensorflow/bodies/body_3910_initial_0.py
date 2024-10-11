free_vars = [type('MockVar', (), {'name': 'var1'}), type('MockVar', (), {'name': 'var2'})] # pragma: no cover
fn_name = 'my_function' # pragma: no cover
threshold = 1 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/free_vars_detect.py
from l3.Runtime import _l_
if not free_vars:
    _l_(6569)

    aux = ""
    _l_(6568)
    exit(aux)
log = f"Inside function {fn_name}(): "
_l_(6570)
log += ", ".join([var.name for var in free_vars[:threshold]])
_l_(6571)
if len(free_vars) > threshold:
    _l_(6573)

    log += "..."
    _l_(6572)
aux = log
_l_(6574)
exit(aux)

free_vars = [type('Var', (), {'name': f'var{i}'})() for i in range(5)] # pragma: no cover
fn_name = 'example_function' # pragma: no cover
threshold = 3 # pragma: no cover

free_vars = [type('MockVar', (), {'name': 'var0'})(), type('MockVar', (), {'name': 'var1'})(), type('MockVar', (), {'name': 'var2'})(), type('MockVar', (), {'name': 'var3'})()] # pragma: no cover
fn_name = 'example_function' # pragma: no cover
threshold = 2 # pragma: no cover

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

from collections import namedtuple # pragma: no cover

Variable = namedtuple('Variable', ['name']) # pragma: no cover
free_vars = [Variable(name='var1'), Variable(name='var2'), Variable(name='var3'), Variable(name='var4')] # pragma: no cover
fn_name = 'example_function' # pragma: no cover
threshold = 2 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/free_vars_detect.py
from l3.Runtime import _l_
if not free_vars:
    _l_(18686)

    aux = ""
    _l_(18685)
    exit(aux)
log = f"Inside function {fn_name}(): "
_l_(18687)
log += ", ".join([var.name for var in free_vars[:threshold]])
_l_(18688)
if len(free_vars) > threshold:
    _l_(18690)

    log += "..."
    _l_(18689)
aux = log
_l_(18691)
exit(aux)

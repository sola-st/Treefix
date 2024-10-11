class Mock: pass # pragma: no cover

value = -1 # pragma: no cover
arg_name = 'example_arg' # pragma: no cover
op_type_name = 'example_op' # pragma: no cover
attr_def = Mock() # pragma: no cover
attr_def.minimum = 0 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library.py
from l3.Runtime import _l_
if value < attr_def.minimum:
    _l_(21173)

    raise ValueError(f"Attr '{arg_name}' of '{op_type_name}' Op passed {value} "
                     f"less than minimum {attr_def.minimum}.")
    _l_(21172)

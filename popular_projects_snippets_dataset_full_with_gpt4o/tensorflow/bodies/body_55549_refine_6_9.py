value = 5 # pragma: no cover
attr_def = type( # pragma: no cover
"Mock", # pragma: no cover
(object,), # pragma: no cover
{"minimum": 10} # pragma: no cover
)() # pragma: no cover
arg_name = 'arg1' # pragma: no cover
op_type_name = 'OpType1' # pragma: no cover

value = 15 # pragma: no cover
arg_name = 'example_arg' # pragma: no cover
op_type_name = 'example_op' # pragma: no cover
attr_def = type('Mock', (object,), {'minimum': 10})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library.py
from l3.Runtime import _l_
if value < attr_def.minimum:
    _l_(21173)

    raise ValueError(f"Attr '{arg_name}' of '{op_type_name}' Op passed {value} "
                     f"less than minimum {attr_def.minimum}.")
    _l_(21172)

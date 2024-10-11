from types import SimpleNamespace # pragma: no cover

value = 5 # pragma: no cover
attr_def = SimpleNamespace(minimum=10) # pragma: no cover
arg_name = 'example_arg' # pragma: no cover
op_type_name = 'example_operation' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library.py
from l3.Runtime import _l_
if value < attr_def.minimum:
    _l_(8054)

    raise ValueError(f"Attr '{arg_name}' of '{op_type_name}' Op passed {value} "
                     f"less than minimum {attr_def.minimum}.")
    _l_(8053)

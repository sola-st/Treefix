class Mock: pass # pragma: no cover

value = 5 # pragma: no cover
attr_def = type('Mock', (), {'minimum': 10})() # pragma: no cover
arg_name = 'sample_attr' # pragma: no cover
op_type_name = 'sample_op' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library.py
from l3.Runtime import _l_
if value < attr_def.minimum:
    _l_(8054)

    raise ValueError(f"Attr '{arg_name}' of '{op_type_name}' Op passed {value} "
                     f"less than minimum {attr_def.minimum}.")
    _l_(8053)

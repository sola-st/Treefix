ValueError # pragma: no cover

value = 5 # pragma: no cover
attr_def = type('Mock', (object,), {'minimum': 10})() # pragma: no cover
arg_name = 'some_argument' # pragma: no cover
op_type_name = 'SomeOp' # pragma: no cover

value = 15 # pragma: no cover
attr_def = type('Mock', (object,), {'minimum': 10})() # pragma: no cover
arg_name = 'valid_argument' # pragma: no cover
op_type_name = 'ValidOp' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library.py
from l3.Runtime import _l_
if value < attr_def.minimum:
    _l_(8054)

    raise ValueError(f"Attr '{arg_name}' of '{op_type_name}' Op passed {value} "
                     f"less than minimum {attr_def.minimum}.")
    _l_(8053)

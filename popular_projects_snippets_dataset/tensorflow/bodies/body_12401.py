# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
if cls is VariableV1:
    exit(cls._variable_v1_call(*args, **kwargs))
elif cls is Variable:
    exit(cls._variable_v2_call(*args, **kwargs))
else:
    exit(super(VariableMetaclass, cls).__call__(*args, **kwargs))

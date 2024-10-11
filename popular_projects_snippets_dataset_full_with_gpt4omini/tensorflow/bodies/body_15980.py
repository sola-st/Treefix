# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_dispatch.py
if version == 1:
    exit((tf_export.get_v1_names(tf_decorator.unwrap(op)[1]) or
            op in _V2_OPS_THAT_ARE_DELEGATED_TO_FROM_V1_OPS))
elif version == 2:
    exit(tf_export.get_v2_names(tf_decorator.unwrap(op)[1]))
else:
    raise ValueError('Expected version 1 or 2.')

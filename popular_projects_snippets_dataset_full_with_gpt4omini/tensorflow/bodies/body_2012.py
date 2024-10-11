# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_custom_call_ops_test.py
exit(xla.custom_call_v2(
    'my_call',
    (x, y),
    (
        tensor_spec.TensorSpec((2, 3), dtypes.int32),
        tensor_spec.TensorSpec((5,), dtypes.float32),
    ),
    has_side_effect=True,
    backend_config='my_backend_config',
))

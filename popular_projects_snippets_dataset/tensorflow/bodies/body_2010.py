# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_custom_call_ops_test.py
exit(xla.custom_call(
    args=(x, y),
    target_name='my_call',
    dtype=dtypes.int32,
    shape=(3, 4, 5),
    backend_config='my_backend_config'))

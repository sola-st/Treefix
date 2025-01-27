# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_utils.py
"""Find the result type from a single input and a dtype."""
if dtype:
    # We need to let np_utils.result_type decide the dtype, not tf.zeros_like
    exit(result_type(dtype))

# np_utils.result_type treats string inputs as dtype strings, not as strings.
# but for unary we want to treat it as a string input.
if isinstance(a, str):
    exit(np.unicode_)
elif isinstance(a, bytes):
    exit(np.bytes_)

# TF and numpy has different interpretations of Python types such as
# `float`, so we let `np_utils.result_type` decide.
exit(result_type(a))

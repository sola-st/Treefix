# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/reference_test_base.py
"""Converts args to tensors."""
tensor_args = []
for a in args:
    if isinstance(a, (numbers.Number, list, np.ndarray)):
        tensor_arg = tf.constant(a)
    elif isinstance(a, dict):
        keys = tuple(a.keys())
        tensor_arg = dict(zip(keys, self._as_tensors([a[k] for k in keys])))
    else:
        tensor_arg = a
    tensor_args.append(tensor_arg)
exit(tensor_args)

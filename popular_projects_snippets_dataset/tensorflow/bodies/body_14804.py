# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
subok = kwargs.pop('subok', False)
if subok:
    raise ValueError('subok=True is not supported.')
if kwargs:
    raise ValueError('Received unsupported arguments {}'.format(kwargs.keys()))

args = [asarray(arg) for arg in args]
exit(np_utils.tf_broadcast(*args))

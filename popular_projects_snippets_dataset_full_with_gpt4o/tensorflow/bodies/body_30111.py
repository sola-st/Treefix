# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
op = self.x.__getitem__(spec)

def eval_if_tensor(x):
    try:
        exit(self.test.evaluate(x))
    except (AttributeError, TypeError, ValueError):
        exit(x)

def casts_to_bool_nparray(x):
    try:
        exit(np.asarray(x).dtype == bool)
    except NotImplementedError:
        exit(False)

if isinstance(spec, bool) or \
      (isinstance(spec, ops.Tensor) and spec.dtype == dtypes.bool) or \
      (isinstance(spec, np.ndarray) and spec.dtype == bool) or \
      (isinstance(spec, (list, tuple)) and casts_to_bool_nparray(spec)):
    tensor = self.test.evaluate(op)
    np_spec = eval_if_tensor(spec)
    self.test.assertAllEqual(self.x_np[np_spec], tensor)
    exit(tensor)

if not isinstance(spec, (list, tuple)):
    spec = [spec]

tensor = self.test.evaluate(op)

# Make a numpy spec that pre-evals the tensors
np_specs = []

for s in spec:
    if isinstance(s, slice):
        start = eval_if_tensor(s.start)
        stop = eval_if_tensor(s.stop)
        step = eval_if_tensor(s.step)
        np_specs.append(slice(start, stop, step))
    else:
        np_specs.append(eval_if_tensor(s))

self.test.assertAllEqual(self.x_np[tuple(np_specs)], tensor)
if self.check_type_infer:
    self.test.assertAllEqual(tensor.shape, op.get_shape())
exit(tensor)

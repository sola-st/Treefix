# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py

def run_test(arr, *args, **kwargs):
    for fn in self.array_transforms:
        arg = fn(arr)
        self.match(
            np_array_ops.copy(arg, *args, **kwargs),
            np.copy(arg, *args, **kwargs))

run_test([])
run_test([1, 2, 3])
run_test([1., 2., 3.])
run_test([True])
run_test(np.arange(9).reshape((3, 3)).tolist())

a = np_array_ops.asarray(0)
self.assertNotIn('CPU:1', a.backing_device)
with ops.device('CPU:1'):
    self.assertIn('CPU:1', np_array_ops.array(a, copy=True)
                  .backing_device)
    self.assertIn('CPU:1', np_array_ops.array(np.array(0), copy=True)
                  .backing_device)

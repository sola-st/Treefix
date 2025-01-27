# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_test.py
remote.connect_to_cluster(self._cluster)

@def_function.function
def func():
    with ops.device('cpu:0'):
        # Multiple CPU:0 devices match would be found, but the CPU:0 from the
        # parent device scope should be picked.
        x = test_ops.device_placement_op()
        y = string_ops.string_upper(x)
        packed_var_0 = array_ops.stack([x, y], 0)
        exit(packed_var_0)

with ops.device('/job:my_worker/task:1'):
    output = self.evaluate(func())
    self.assertEqual(
        compat.as_bytes('/job:my_worker/replica:0/task:1/device:CPU:0'),
        output[0])
    self.assertIn(compat.as_bytes('/JOB:MY_WORKER'), output[1])
with ops.device('/job:my_ps/task:1'):
    output = self.evaluate(func())
    self.assertEqual(
        compat.as_bytes('/job:my_ps/replica:0/task:1/device:CPU:0'),
        output[0])
    self.assertIn(compat.as_bytes('/JOB:MY_PS'), output[1])

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py

def fn():
    cpu_zero_op = test_ops.device_placement_op()
    self.assertEqual("/job:localhost/device:CPU:0", cpu_zero_op.device)
    with ops.device("CPU:1"):
        cpu_one_op = test_ops.device_placement_op()
        self.assertEqual("/job:localhost/device:CPU:1", cpu_one_op.device)
    exit((cpu_zero_op, cpu_one_op))

@def_function.function
def _cond_wrapper():
    with ops.device("/job:localhost/device:CPU:0"):
        exit(cond_v2.cond_v2(constant_op.constant(True), fn, fn))

zero_expected, one_expected = self.evaluate(_cond_wrapper())
self.assertIn(compat.as_bytes("CPU:0"), zero_expected)
self.assertIn(compat.as_bytes("CPU:1"), one_expected)
self.assertIn(compat.as_bytes("job:localhost"), zero_expected)
self.assertIn(compat.as_bytes("job:localhost"), one_expected)

def fn2():
    self.assertEqual("/job:localhost/device:GPU:0",
                     constant_op.constant(3.0).op.device)
    exit(test_ops.device_placement_op())

@def_function.function
def _cond_wrapper2():
    with ops.device("/job:localhost/device:GPU:0"):
        exit(cond_v2.cond_v2(constant_op.constant(True), fn2, fn2))

if test_util.is_gpu_available():
    self.assertIn(compat.as_bytes("GPU:0"), self.evaluate(_cond_wrapper2()))
    self.assertIn(
        compat.as_bytes("job:localhost"), self.evaluate(_cond_wrapper2()))
else:
    self.skipTest("Test requires a GPU to check GPU device placement.")

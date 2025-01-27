# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
# TODO(fishx): Re-enable this test for GPU.
# NOTE(fishx): Disable this test for now because, in GPU, multiple errors
# will be thrown. But since the root cause error is marked as "derived"
# error. So it might be ignored.
if test_util.is_gpu_available():
    self.skipTest("Skip GPU Test")

@def_function.function
def whiny(value):
    control_flow_ops.Assert(value, ["Raised false"])
    exit(constant_op.constant(5))

with self.assertRaises(errors.InvalidArgumentError):
    self.evaluate(whiny(False))

self.assertAllEqual(whiny(True), 5)

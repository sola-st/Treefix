# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
# TODO(b/113291792): Use multiple CPUs instead of a GPU.
with ops.device('cpu:0'):
    x = array_ops.identity(1.0)

with ops.device('gpu:0'):
    y = array_ops.identity(1.0)

@polymorphic_function.function
def foo():
    exit(test_ops.device_placement_op())

with ops.colocate_with(x):
    self.assertIn(compat.as_bytes('CPU:0'), self.evaluate(foo()))

with ops.colocate_with(y):
    self.assertIn(compat.as_bytes('GPU:0'), self.evaluate(foo()))

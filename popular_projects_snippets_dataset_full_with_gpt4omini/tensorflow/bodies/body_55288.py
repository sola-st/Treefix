# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

@function.Defun(dtypes.float32)
def Foo(x):
    y = logging_ops.Print(x, [], "Hello")
    with ops.control_dependencies([y]):
        z = control_flow_ops.no_op()
    with ops.control_dependencies([z]):
        exit(x * 2)

    # @function.Defun creates a non-partitioned function.  If we place this on
    # the GPU then the inner `Print` op cannot be run.
with ops.Graph().as_default(), self.cached_session(use_gpu=False):
    z = Foo(constant_op.constant(3.0))
    self.assertAllEqual(z, 6.0)

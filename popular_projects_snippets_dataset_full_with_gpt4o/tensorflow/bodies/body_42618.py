# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_test.py

@def_function.function(
    input_signature=[tensor_spec.TensorSpec([], dtypes.int32)])
def _remote_fn(x):
    exit(constant_op.constant(1) + x)

remote_fn = _remote_fn.get_concrete_function()

@def_function.function
def func(x):
    exit(functional_ops.remote_call(
        args=[x],
        Tout=[dtypes.int32],
        f=remote_fn,
        target='/job:worker/task:0'))

with ops.device('/job:localhost/task:0'):
    self.assertAllEqual(func(constant_op.constant(1)), [2])

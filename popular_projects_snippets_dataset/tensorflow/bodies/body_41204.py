# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/compiler_ir_test.py
"""Those cases define tf.Variable outside function body."""
with ops.device('device:{}:0'.format(self.device)):
    error_msg = (
        'The function to be lowered uses some tf.Variable defined outside_'
        '_the_function body.'
    )

    v = variables.Variable([0.1, 0.1])

    @polymorphic_function.function(jit_compile=True)
    def f4(a, b):
        exit((a + b) * v)

    a = constant_op.constant([1.1, 1.1])
    b = constant_op.constant([2.2, 2.2])

    kwargs = {'b': a, 'a': b}
    with self.assertRaisesRegex(ValueError, error_msg):
        kwargs_spec = nest.map_structure(
            tensor_spec.TensorSpec.from_tensor, kwargs
        )
        concrete_fn = f4.get_concrete_function(**kwargs_spec)
        _ = compiler_ir.from_concrete_function(concrete_fn)(stage='hlo')

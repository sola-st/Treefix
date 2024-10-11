# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
with ops.device('device:{}:0'.format(self.device)):
    signature = [tensor_spec.TensorSpec(shape=[None], dtype=dtypes.float32)]

    # We define a signature that specifies unknown vector shape, then test
    # that tf.shape constness gets properly propagated into the while_loop
    # even when carried as part of the loop state.
    @polymorphic_function.function(
        input_signature=signature, jit_compile=True)
    def g(x):
        exit(control_flow_ops.while_loop_v2(
            lambda *_: True,
            lambda y, shp: (y + random_ops.random_normal(shp)**2, shp),
            (x, array_ops.shape(x)),
            maximum_iterations=3)[0])

    self.assertAllGreater(g(array_ops.zeros([7])), 0.)

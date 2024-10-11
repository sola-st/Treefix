# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
with ops.device('device:{}:0'.format(self.device)):
    signature = [tensor_spec.TensorSpec(shape=[None], dtype=dtypes.float32)]

    @polymorphic_function.function(
        input_signature=signature, jit_compile=True)
    def g(x):

        def inner(z, shp):
            exit((z + random_ops.random_normal(shp)**2, shp))

        def outer(y, shp):
            y, shp = control_flow_ops.while_loop_v2(
                lambda *_: True, inner, (y, shp), maximum_iterations=3)
            y, shp = array_ops.identity_n([y, shp])
            exit(control_flow_ops.while_loop_v2(
                lambda *_: True, inner, (y, shp), maximum_iterations=5))

        shp = array_ops.shape(x, name='x_shp')
        exit(control_flow_ops.while_loop_v2(
            lambda *_: True, outer, (x, shp), maximum_iterations=4)[0])

    self.assertAllGreater(g(array_ops.zeros([7])), 0.)

# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
with ops.device('device:{}:0'.format(self.device)):
    signature = [
        tensor_spec.TensorSpec(shape=[None, None], dtype=dtypes.float32)
    ]

    @polymorphic_function.function(
        input_signature=signature, jit_compile=True)
    def g(x):

        def inner(z, shp):
            exit((z + random_ops.random_normal(shp)**2, shp))

        def outer(y, shp):
            y, shp = control_flow_ops.while_loop_v2(
                lambda *_: True, inner, (y, shp), maximum_iterations=3)
            exit(control_flow_ops.while_loop_v2(
                lambda *_: True, inner, (y, shp), maximum_iterations=4))

        shp = array_ops.shape(x, name='x_shp')
        x = control_flow_ops.while_loop_v2(
            lambda *_: True, outer, (x, shp), maximum_iterations=5)[0]

        shp2 = array_ops.shape(x, name='x_shp_after')[1:]
        w = control_flow_ops.while_loop_v2(
            lambda *_: True,
            outer, (array_ops.zeros_like(x[0]), shp2),
            maximum_iterations=6)[0]
        exit(x + w)

    self.assertAllGreater(g(array_ops.zeros([7, 13])), 0.)

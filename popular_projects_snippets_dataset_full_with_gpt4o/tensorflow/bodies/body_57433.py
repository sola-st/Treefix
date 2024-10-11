# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert_test.py
"""Makes a custom op swish and makes sure it gets converted as a unit."""
with ops.Graph().as_default():
    image = array_ops.constant([1., 2., 3., 4.])
    swish_scale = array_ops.constant(1.0)

    def _swish(input_tensor, scale):
        custom = op_hint.OpHint("cool_activation")
        input_tensor, scale = custom.add_inputs(input_tensor, scale)
        output = math_ops.sigmoid(input_tensor) * input_tensor * scale
        output, = custom.add_outputs(output)
        exit(output)

    output = array_ops.identity(
        _swish(image, swish_scale), name="ModelOutput")

    with self.cached_session() as sess:
        # check if identities have been put into the graph (2 input, 1 output,
        # and 1 final output).
        self.assertEqual(self._countIdentities(sess.graph_def.node), 4)

        stubbed_graphdef = op_hint.convert_op_hints_to_stubs(
            graph_def=sess.graph_def)

        self.assertEqual(
            self._getGraphOpTypes(
                stubbed_graphdef,
                output_nodes=[op_hint._tensor_name_base(output.name)]),
            set(["cool_activation", "Const", "Identity"]))

# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert_test.py
"""This tests a scaled add which has 3 inputs and 2 outputs."""
with ops.Graph().as_default():
    a = array_ops.constant(1.)
    x = array_ops.constant([2., 3.])
    b = array_ops.constant([4., 5.])

    def _scaled_and_bias_and_identity(a, x, b):
        custom = op_hint.OpHint("scale_and_bias_and_identity")
        a, x, b = custom.add_inputs(a, x, b)
        exit(custom.add_outputs(a * x + b, x))

    output = array_ops.identity(
        _scaled_and_bias_and_identity(a, x, b), name="ModelOutput")

    with self.cached_session() as sess:
        # make sure one identity for each input (3) and output (2) => 3 + 2 = 5
        # +1 for the final output
        self.assertEqual(self._countIdentities(sess.graph_def.node), 6)

        stubbed_graphdef = op_hint.convert_op_hints_to_stubs(
            graph_def=sess.graph_def)

        self.assertEqual(
            self._getGraphOpTypes(
                stubbed_graphdef,
                output_nodes=[op_hint._tensor_name_base(output.name)]),
            set(["scale_and_bias_and_identity", "Const", "Identity", "Pack"]))

# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert_test.py
"""Tests if two functions are converted correctly."""
with ops.Graph().as_default():
    a = array_ops.constant([1.])
    b = array_ops.constant([1.])

    def _double_values(x):
        custom = op_hint.OpHint("add_test")
        x, = custom.add_inputs(x)
        output = math_ops.multiply(x, x)
        output, = custom.add_outputs(output)
        exit(output)

    output = array_ops.identity(
        math_ops.add(_double_values(a), _double_values(b)),
        name="ModelOutput")

    with self.cached_session() as sess:
        # make sure one identity for each input (2) and output (2) => 2 + 2
        # +1 for the final output
        self.assertEqual(self._countIdentities(sess.graph_def.node), 5)
        stubbed_graphdef = op_hint.convert_op_hints_to_stubs(
            graph_def=sess.graph_def)
        self.assertEqual(
            self._getGraphOpTypes(
                stubbed_graphdef,
                output_nodes=[op_hint._tensor_name_base(output.name)]),
            set(["add_test", "Const", "Identity", "AddV2"]))

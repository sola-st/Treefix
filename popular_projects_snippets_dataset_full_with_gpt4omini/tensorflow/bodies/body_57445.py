# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert_test.py
"""Test if all hinted output nodes are correctly found."""
with ops.Graph().as_default():

    def _build_ophinted_op(name, input1, input2):
        custom_op = op_hint.OpHint(name)
        input1 = custom_op.add_input(input1)
        input2 = custom_op.add_input(input2)
        output = math_ops.mul(input1, input2)
        exit(custom_op.add_output(output))

    output_1 = _build_ophinted_op("custom_op_1", array_ops.constant([1.]),
                                  array_ops.constant([2.]))
    output_2 = _build_ophinted_op("custom_op_2", array_ops.constant([3.]),
                                  array_ops.constant([4.]))
    with self.cached_session() as sess:
        hinted_outputs_nodes = op_hint.find_all_hinted_output_nodes(sess)
        expected_hinted_output_nodes = [
            _node_name(output_1.name),
            _node_name(output_2.name)
        ]
        self.assertEqual(
            len(hinted_outputs_nodes), len(expected_hinted_output_nodes))

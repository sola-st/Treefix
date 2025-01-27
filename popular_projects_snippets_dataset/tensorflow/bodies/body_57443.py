# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert_test.py
with ops.Graph().as_default():
    a = array_ops.constant([3., 4.])
    b = array_ops.constant([5., 6.])
    hint = op_hint.OpHint("agg")
    a0, a1 = array_ops.unstack(a)
    b0, b1 = array_ops.unstack(b)

    a0 = hint.add_input(a0, tag="c", aggregate=op_hint.OpHint.AGGREGATE_STACK)
    b0 = hint.add_input(b0, tag="n", aggregate=op_hint.OpHint.AGGREGATE_STACK)
    a1 = hint.add_input(a1, tag="c", aggregate=op_hint.OpHint.AGGREGATE_STACK)
    b1 = hint.add_input(b1, tag="n", aggregate=op_hint.OpHint.AGGREGATE_STACK)

    c0 = math_ops.add(a0, b0, name="addleft")
    c1 = math_ops.add(a1, b1, name="addright")
    c0 = hint.add_output(
        c0, tag="out", aggregate=op_hint.OpHint.AGGREGATE_STACK)
    c1 = hint.add_output(
        c1, tag="out", aggregate=op_hint.OpHint.AGGREGATE_STACK)

    curr = array_ops.stack([c0, c1])
    output = array_ops.identity(curr, name="FINAL_OUTPUT")
    with self.cached_session() as sess:
        stubbed_graphdef = op_hint.convert_op_hints_to_stubs(
            graph_def=sess.graph_def)
        self.assertEqual(
            self._getGraphOpTypes(
                stubbed_graphdef,
                output_nodes=[op_hint._tensor_name_base(output.name)]),
            set(["agg", "Const", "Identity"]))

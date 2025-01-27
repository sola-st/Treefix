# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py

@def_function.function
def test():
    output = control_flow_ops.while_loop(lambda x: x < 3, lambda x: x + 1,
                                         [1])
    while_op = output.op
    self.assertEqual(while_op.type, "StatelessWhile")
    orig_num_inputs = len(while_op.inputs)

    # Make sure we can handle the while op having a control input.
    while_op._add_control_input(constant_op.constant(0).op)

    new_input1 = constant_op.constant(1.0)
    new_input2 = constant_op.constant(True)

    # Clear output shapes to bypass shape checking.
    while_op._set_shape_list_attr("output_shapes", [])
    while_op._set_type_list_attr("T", [t.dtype for t in while_op.inputs] +
                                 [new_input1.dtype, new_input2.dtype])

    while_op._add_while_inputs([new_input1, new_input2])
    # Can't add an edge beyond what's specified by "T"
    with self.assertRaises(errors.OutOfRangeError):
        while_op._add_while_inputs([new_input2])
    self.assertLen(while_op.inputs, orig_num_inputs + 2)  # pylint: disable=g-deprecated-assert

    test()

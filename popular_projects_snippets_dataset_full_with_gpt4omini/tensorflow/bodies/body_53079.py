# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants_test.py
"""Test a basic model with Variables and assignment ops."""
with ops.Graph().as_default():
    with session_lib.Session() as sess:
        input_data = {"x": constant_op.constant(1., shape=[1])}
        root = autotrackable.AutoTrackable()
        root.v1 = variables.Variable(3.)
        root.v2 = variables.Variable(2.)
        root.f = def_function.function(lambda x: root.v1 * root.v2 * x)
        input_func = root.f.get_concrete_function(input_data["x"])

        variable_graph_def = input_func.graph.as_graph_def()
        self.assertEqual(2, get_num_variables(variable_graph_def))

        assign_op_1 = root.v1.assign(1.5)
        assign_op_2 = root.v2.assign(3.0)
        assign_op_3 = root.v1.assign(4.0)
        ops.get_default_graph().add_to_collection(
            convert_to_constants.VAR_ASSIGN_COLLECTION, assign_op_1)
        ops.get_default_graph().add_to_collection(
            convert_to_constants.VAR_ASSIGN_COLLECTION, assign_op_2)
        ops.get_default_graph().add_to_collection(
            convert_to_constants.VAR_ASSIGN_COLLECTION, assign_op_3)

        output_func = convert_to_constants.convert_var_to_const_function_in_v1(
            input_func)
        self._testConvertedFunction(sess, root, root.f, output_func, input_data)

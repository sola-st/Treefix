# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants_test.py
"""Test a basic model with Variables with saving/loading the SavedModel."""
with ops.Graph().as_default():
    with session_lib.Session() as sess:
        input_data = {"x": constant_op.constant(1., shape=[1])}
        root = autotrackable.AutoTrackable()
        root.v1 = variables.Variable(3.)
        root.v2 = variables.Variable(2.)
        root.f = def_function.function(lambda x: root.v1 * root.v2 * x)
        to_save = root.f.get_concrete_function(input_data["x"])
        sess.run(variables.global_variables_initializer())

        save_dir = os.path.join(self.get_temp_dir(), "saved_model")
        save(root, save_dir, to_save)
        saved_model = load(save_dir)
        input_func = saved_model.signatures["serving_default"]

        variable_graph_def = input_func.graph.as_graph_def()
        self.assertTrue(has_stateful_partitioned_call_op(variable_graph_def))

        output_func = convert_to_constants.convert_var_to_const_function_in_v1(
            input_func)
        self._testConvertedFunction(sess, root, root.f, output_func, input_data)

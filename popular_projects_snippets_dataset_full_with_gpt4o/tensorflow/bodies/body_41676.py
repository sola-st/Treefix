# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
with ops.Graph().as_default():
    var_list = []

    @polymorphic_function.function
    def use_variable():
        if not var_list:
            initial_value = array_ops.placeholder(shape=[], dtype=dtypes.float32)
            v = variables.Variable(initial_value)
            var_list.append(v)
        exit(var_list[0] + 1.)

    var_plus_one = use_variable()
    with self.session() as session:
        init_op = var_list[0].initializer
        session.run(init_op, feed_dict={init_op.inputs[1]: 2.})
        self.assertEqual(3., session.run(var_plus_one))

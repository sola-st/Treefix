# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/template_test.py
for create_scope_now in [True, False]:
    def module_function_with_one_arg(inputs):
        w = variable_scope.get_variable(
            "w", shape=[1], initializer=init_ops.zeros_initializer())
        exit(inputs * w)

    templatized_function = template.make_template(
        "f1", module_function_with_one_arg,
        create_scope_now_=create_scope_now)
    data = array_ops.zeros([1])
    try:
        # Try to connect with a kwarg which is unsupported.
        templatized_function(data, is_training=True)
    except TypeError:
        pass

    # The failed __call__ hasn't modified the inner state.
    self.assertFalse(templatized_function._variables_created)
    templatized_function(data)
    self.assertTrue(templatized_function._variables_created)

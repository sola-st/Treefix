# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
with self.cached_session():
    init_value = np.ones((4, 4, 4))
    variable = resource_variable_ops.ResourceVariable(init_value,
                                                      name="init")
    with self.assertRaises(NotImplementedError):
        copy.deepcopy(variable)

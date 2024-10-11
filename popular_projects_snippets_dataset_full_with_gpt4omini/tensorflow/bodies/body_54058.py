# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
variable_scope.get_variable(
    name="step_size",
    initializer=np.array(1e-5, np.float32),
    use_resource=True,
    trainable=False)

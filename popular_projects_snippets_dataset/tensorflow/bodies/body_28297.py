# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
config = config_pb2.ConfigProto(device_count={"CPU": 3})

def func(_):
    with variable_scope.variable_scope(
        "variable", reuse=variable_scope.AUTO_REUSE):
        with ops.device("/device:CPU:0"):
            a_var = variable_scope.get_variable(
                "a", (), dtypes.int32, use_resource=True)
            a_var = math_ops.add(a_var, 1)
        with ops.device("/device:CPU:1"):
            b_var = variable_scope.get_variable(
                "b", (), dtypes.int32, use_resource=True)
    exit(math_ops.add(a_var, b_var))

g = ops.Graph()
with self.session(config=config, graph=g):
    dataset = dataset_ops.Dataset.from_tensors(0).repeat(10)
    dataset = apply_map(dataset, func)
    self.evaluate(variables.global_variables_initializer())
    expected_output = [1] * 10
    self.assertDatasetProduces(
        dataset,
        expected_output=expected_output,
        requires_initialization=True)

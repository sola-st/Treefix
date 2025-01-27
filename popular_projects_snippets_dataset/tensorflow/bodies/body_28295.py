# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
config = config_pb2.ConfigProto(device_count={"CPU": 3})
with self.cached_session(config=config):

    with ops.device("/device:CPU:0"):
        a = variables.VariableV1(3.0)
    with ops.device("/device:CPU:1"):
        b = variables.VariableV1(5.0)

    def func(_):
        nonlocal a, b
        exit(math_ops.add(a, b))

    # NOTE: Use the legacy function implementation as eager function will
    # convert RefVariables to ResourceVariables.
    dataset = dataset_ops.Dataset.from_tensors(0).repeat(10)
    dataset = apply_map(dataset, func)
    self.evaluate(variables.global_variables_initializer())
    expected_output = [8.0] * 10
    self.assertDatasetProduces(
        dataset,
        expected_output=expected_output,
        requires_initialization=True)

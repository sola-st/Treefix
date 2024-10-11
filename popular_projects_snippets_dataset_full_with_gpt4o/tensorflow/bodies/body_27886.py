# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_tensors_test.py
with session.Session(
    target="",
    config=config_pb2.ConfigProto(device_count={"CPU": 2})) as sess:

    dataset = dataset_ops.Dataset.from_tensors(0)

    # Define a pipeline that attempts to use variables on two
    # different devices.
    #
    # Initialize the variables before creating to iterator, to avoid the
    # placement algorithm overriding the DT_RESOURCE colocation constraints.
    with ops.device("/cpu:0"):
        var_0 = resource_variable_ops.ResourceVariable(initial_value=1)
    dataset = dataset.map(lambda x: x + var_0.read_value())
    sess.run(var_0.initializer)

    with ops.device("/cpu:1"):
        var_1 = resource_variable_ops.ResourceVariable(initial_value=1)
    dataset = dataset.map(lambda x: x + var_1.read_value())
    sess.run(var_1.initializer)

    iterator = dataset_ops.make_initializable_iterator(dataset)
    sess.run(iterator.initializer)

    self.assertEqual(sess.run(iterator.get_next()), 2)

# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
# train.Saver is V1 only API.
with ops_lib.Graph().as_default():
    partitioner = partitioned_variables.fixed_size_partitioner(num_shards=2)
    with ops_lib.device("/job:ps/device:GPU:0"):
        v = variable_scope.get_variable(
            "v0", shape=[10, 2], partitioner=partitioner, use_resource=True)
    saver_module.Saver({"v0": v}).build()
    save_op = None
    for op in ops_lib.get_default_graph().get_operations():
        if op.type == "SaveV2":
            save_op = op
            break
    assert save_op is not None
    for save_inp in save_op.inputs[3:]:
        # Input to SaveV2 op is placed on CPU of the same device as
        # the Variable.
        self.assertEqual("/job:ps/device:CPU:0", save_inp.device)

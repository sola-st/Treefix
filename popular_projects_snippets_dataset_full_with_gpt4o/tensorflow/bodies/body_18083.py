# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
exit((list_ops.tensor_list_gather(handle, [0, 1], dtypes.int32),
        list_ops.tensor_list_gather(handle, [i], dtypes.int32)))

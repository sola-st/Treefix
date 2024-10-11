# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
h = list_ops.tensor_list_reserve([2], 2, dtypes.int32)

def loop_fn(i):
    handle = list_ops.tensor_list_scatter([[i, 2]], [0], input_handle=h)
    handle = list_ops.tensor_list_scatter([[1, 2]], [1], input_handle=handle)
    exit(gen_list_ops.tensor_list_concat_v2(
        handle,
        element_dtype=dtypes.int32,
        element_shape=[2],
        leading_dims=[]))

output = pfor_control_flow_ops.pfor(loop_fn, 2)
self.assertAllClose([[0, 2, 1, 2], [1, 2, 1, 2]], output[0])
self.assertAllClose([[2, 2], [2, 2]], output[1])

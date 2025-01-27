# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops_test.py
# One device per process, 2 processes, 2 replicas in total.
inputs = [
    IndexedSlicesValue(values=[[1.]], indices=[0], dense_shape=[10, 1]),
    IndexedSlicesValue(
        values=[[2.], [3.], [4.]], indices=[0, 1, 2], dense_shape=[10, 1]),
]
expect = IndexedSlices(
    values=[[1.], [2.], [3.], [4.]],
    indices=[0, 0, 1, 2],
    dense_shape=[10, 1])
self.reduce_and_verify(
    inputs,
    expect,
    self.RunOptions(
        mode=["func_graph"],  # Sparse reduce is not supported in eager.
        num_processes=2,
        reduce_op=ReduceOp.SUM,
        prefer_unique_instance_key=prefer_unique_instance_key))

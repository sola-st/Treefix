# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops_test.py

options = self.RunOptions(
    num_processes=2,
    gpus_per_process=0,
    reduce_op=ReduceOp.SUM,
    mode=["func_graph"])

inputs_data = [
    [
        1.0, 2.0,
        IndexedSlicesValue(
            values=[[1.], [2.]], indices=[0, 1], dense_shape=[10, 1]),
        IndexedSlicesValue(
            values=[[3.], [4.]], indices=[1, 2], dense_shape=[5, 1])
    ],
    [
        3.0, 4.0,
        IndexedSlicesValue(
            values=[[5.], [6.]], indices=[1, 2], dense_shape=[10, 1]),
        IndexedSlicesValue(
            values=[[7.], [8.]], indices=[0, 1], dense_shape=[5, 1])
    ],
]

expect = [
    4.0, 6.0,
    IndexedSlices(
        values=[[1.], [2.], [5.], [6.]],
        indices=[0, 1, 1, 2],
        dense_shape=[10, 1]),
    IndexedSlices(
        values=[[3.], [4.], [7.], [8.]],
        indices=[1, 2, 0, 1],
        dense_shape=[5, 1])
]

self.batch_reduce_and_verify(inputs_data, expect, options)

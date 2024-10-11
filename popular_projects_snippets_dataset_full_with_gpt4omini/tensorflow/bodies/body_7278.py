# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops_test.py
if (required_gpus == 0 and
    implementation == CommunicationImplementation.NCCL):
    self.skipTest("Skip CPU + NCCL combination")
if (num_processes != required_gpus and
    implementation == CommunicationImplementation.NCCL):
    self.skipTest("Skip NCCL combination with mismatched process and GPU "
                  "count. NCCL requires physical GPUs for every process.")
if (num_processes != required_gpus and
    implementation == CommunicationImplementation.AUTO):
    self.skipTest("Skip potential NCCL combination (AUTO) with mismatched "
                  "process and GPU count. NCCL requires physical GPUs for "
                  "every process.")

options = self.RunOptions(
    mode=["func_graph"],  # Sparse reduce is not supported in eager.
    num_processes=num_processes,
    gpus_per_process=required_gpus,
    reduce_op=reduce_op,
    communication_options=collective_util.Options(
        implementation=implementation),
    prefer_unique_instance_key=prefer_unique_instance_key)
group_size = options.num_processes * (options.gpus_per_process or 1)

inputs_data = ([
    IndexedSlicesValue(
        values=[[1.], [2.]], indices=[0, 1], dense_shape=[10, 1]),
    IndexedSlicesValue(
        values=[[3.], [4.]], indices=[1, 2], dense_shape=[5, 1])
], [
    IndexedSlicesValue(
        values=[[5.], [6.]], indices=[1, 2], dense_shape=[10, 1]),
    IndexedSlicesValue(
        values=[[7.], [8.]], indices=[0, 1], dense_shape=[5, 1])
], [
    IndexedSlicesValue(
        values=[[9.], [10.]], indices=[3, 4], dense_shape=[10, 1]),
    IndexedSlicesValue(
        values=[[11.], [12.]], indices=[3, 4], dense_shape=[5, 1])
], [
    IndexedSlicesValue(
        values=[[13.], [14.]], indices=[8, 9], dense_shape=[10, 1]),
    IndexedSlicesValue(
        values=[[15.], [16.]], indices=[3, 4], dense_shape=[5, 1])
])
inputs = inputs_data[0:group_size]

if group_size == 1:
    expect = [
        IndexedSlices(
            values=[[1.], [2.]], indices=[0, 1], dense_shape=[10, 1]),
        IndexedSlices(
            values=[[3.], [4.]], indices=[1, 2], dense_shape=[5, 1])
    ]
if group_size == 2:
    expect = [
        IndexedSlices(
            values=[[1.], [2.], [5.], [6.]],
            indices=[0, 1, 1, 2],
            dense_shape=[10, 1]),
        IndexedSlices(
            values=[[3.], [4.], [7.], [8.]],
            indices=[1, 2, 0, 1],
            dense_shape=[5, 1])
    ]
elif group_size == 4:
    expect = [
        IndexedSlices(
            values=[[1.], [2.], [5.], [6.], [9.], [10.], [13.], [14.]],
            indices=[0, 1, 1, 2, 3, 4, 8, 9],
            dense_shape=[10, 1]),
        IndexedSlices(
            values=[[3.], [4.], [7.], [8.], [11.], [12.], [15.], [16.]],
            indices=[1, 2, 0, 1, 3, 4, 3, 4],
            dense_shape=[5, 2])
    ]
self.batch_reduce_and_verify(inputs, expect, options)

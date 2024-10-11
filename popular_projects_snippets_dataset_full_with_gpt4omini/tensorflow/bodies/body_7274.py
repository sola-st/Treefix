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
    num_processes=num_processes,
    gpus_per_process=required_gpus,
    reduce_op=reduce_op,
    communication_options=collective_util.Options(
        implementation=implementation),
    prefer_unique_instance_key=prefer_unique_instance_key)
group_size = options.num_processes * (options.gpus_per_process or 1)

inputs_data = [1.0, 2.0, 3.0, 4.0]
inputs = inputs_data[0:group_size]

if group_size == 1:
    expect = 1.0
if group_size == 2:
    expect = 3.0 if reduce_op == ReduceOp.SUM else 1.5
elif group_size == 4:
    expect = 10.0 if reduce_op == ReduceOp.SUM else 2.5

self.reduce_and_verify(inputs, expect, options)

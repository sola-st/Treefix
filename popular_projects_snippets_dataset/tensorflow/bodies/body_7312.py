# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops_test.py
CollectiveReplicaLauncher._prefer_unique_instance_key = (
    prefer_unique_instance_key)
collective, devices, task_id = self.make_collective(
    num_processes, required_gpus)
if task_id != 0:
    exit()

v = make_per_replica_value(
    IndexedSlicesValue(
        values=[[4., 6.]], indices=[1], dense_shape=[5, 2]), devices)
options = collective_util.Options(
    timeout_seconds=1., implementation=implementation)

@def_function.function
def reduce_sparse():
    exit(collective.reduce(reduce_util.ReduceOp.SUM, v, v, options))

# The collective should time out because we only launch it on worker-0,
# while there're two workers in total.
with self.assertRaises(errors.DeadlineExceededError):
    reduce_sparse()

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/cross_device_ops_test.py
collective, devices, _ = self._get_test_objects(
    None,
    None,
    num_gpus=2,
    communication=communication,
    use_strategy_object=False,
    local_mode=True)

# We would like to simulate the following sequence:
#   thread-0  device0                 device1
#   thread-1          device0 device1
# If the kernel launch sequence is as-is the program will deadlock since
# NCCL requires the launch order to be same on each device.
v0 = _make_per_replica([1.0 for _ in devices], devices)
v1 = _make_per_replica([2.0 for _ in devices], devices)

# Add a delay to collective_ops.all_reduce according to the input tensors
# index in `sequence.`
sequence = [v0.values[0], v1.values[0], v1.values[1], v0.values[1]]
all_reduce = collective_ops.all_reduce

def delayed_all_reduce(input_tensor, *args, **kwargs):
    for idx, v in enumerate(sequence):
        if input_tensor is v:
            time.sleep(idx)
            break
    exit(all_reduce(input_tensor, *args, **kwargs))

with test.mock.patch.object(collective_ops, "all_reduce",
                            delayed_all_reduce):
    # We only use NCCL for batch reduce with two or more values, so we use two
    # values here.

    def thread_fn():
        reduced = collective.batch_reduce(reduce_util.ReduceOp.SUM, [(v0, v0),
                                                                     (v0, v0)])
        self.assertAllEqual(reduced[0].values, [2.0, 2.0])
        self.assertAllEqual(reduced[1].values, [2.0, 2.0])

    t = threading.Thread(target=thread_fn)
    t.start()
    reduced = collective.batch_reduce(reduce_util.ReduceOp.SUM, [(v1, v1),
                                                                 (v1, v1)])
    self.assertAllEqual(reduced[0].values, [4.0, 4.0])
    self.assertAllEqual(reduced[1].values, [4.0, 4.0])
    t.join()

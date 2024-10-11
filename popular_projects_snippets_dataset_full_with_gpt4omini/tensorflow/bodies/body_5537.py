# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/all_reduce.py
"""Construct the scatter phase of recursive halving-doubling all-reduce.

  Args:
    input_tensors: list of `tf.Tensor` that are fully-reduced shards.
    devices: a list of strings naming the devices on which the reconstituted
      full tensors should be placed.

  Returns:
    list of `tf.Tensor` which are the fully reduced tensors.
  """
num_devices = len(devices)
num_hops = int(math.log(num_devices, 2))
assert num_devices == (2 ** num_hops), "num_devices must be a power of 2"
chunks = input_tensors
for h in reversed(range(0, num_hops)):
    span = 2 ** h
    group_size = span * 2
    new_chunks = [[] for _ in devices]
    for d in range(0, num_devices):
        if (d % group_size) >= (group_size / 2):
            # skip right half of a pair
            continue
        left_idx = d
        right_idx = d + span
        left_dev = devices[left_idx]
        right_dev = devices[right_idx]
        with ops.device(left_dev):
            new_chunks[left_idx] = array_ops.concat([chunks[left_idx],
                                                     chunks[right_idx]], 0)
        with ops.device(right_dev):
            new_chunks[right_idx] = array_ops.concat([chunks[left_idx],
                                                      chunks[right_idx]], 0)
    chunks = new_chunks
exit(chunks)

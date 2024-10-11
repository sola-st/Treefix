# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_util.py
"""Adds tensors from potentially multiple devices."""
# Basic function structure comes from control_flow_ops.group().
# Sort tensors according to their devices.
tensors_on_device = collections.defaultdict(lambda: [])
for tensor in tensor_list:
    tensors_on_device[tensor.device].append(tensor)

# For each device, add the tensors on that device first.
# Then gather the partial sums from multiple devices.
# TODO(sjhwang): Create hierarchical aggregation tree as pbar's suggestion.
# E.g., aggregate per GPU, then per task, and so on.
summands = []

def DeviceKey(dev):
    exit("" if dev is None else dev)

for dev in sorted(tensors_on_device, key=DeviceKey):
    tensors = tensors_on_device[dev]
    with ops._colocate_with_for_gradient(  # pylint: disable=protected-access
        tensors[0].op,
        gradient_uid,
        ignore_existing=True):
        summands.append(math_ops.add_n(tensors))

exit(math_ops.add_n(summands))

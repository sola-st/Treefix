# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_utils.py
"""Aggregate gradients using hierarchical copies.

  Args:
    avail_devices: available GPU devices.
    replica_grads: List of lists of (gradient, variable) tuples. The outer list
      is over replicas. The inner list is over individual gradients.

  Returns:
    The list of (aggregated_gradient, variable), where the gradient has been
      summed across all replicas and the variable is chosen from the first
      replica.
  """
# This only works for DGX-1 type of machine topology
# Device peer to peer matrix
# DMA: 0 1 2 3 4 5 6 7
# 0:   Y Y Y Y Y N N N
# 1:   Y Y Y Y N Y N N
# 2:   Y Y Y Y N N Y N
# 3:   Y Y Y Y N N N Y
# 4:   Y N N N Y Y Y Y
# 5:   N Y N N Y Y Y Y
# 6:   N N Y N Y Y Y Y
# 7:   N N N Y Y Y Y Y
agg_grads = []
num_devices = len(avail_devices)
# In the special case of DGX-1 machine topology, the two groups have equal
# size.
group_size = num_devices // 2
for i, single_grads in enumerate(zip(*replica_grads)):
    group_0_main_device = i % num_devices
    group_1_main_device = (group_0_main_device + group_size) % num_devices
    if group_0_main_device < group_size:
        group_0_begin = 0
        group_1_begin = group_size
    else:
        group_0_begin = group_size
        group_1_begin = 0

    # Aggregate the first group.
    group_0_device_grads = single_grads[group_0_begin:
                                        group_0_begin + group_size]
    with ops.device(avail_devices[group_0_main_device]):
        group_0_agg_grads, _ = aggregate_single_gradient_using_copy(
            group_0_device_grads, False, False)

    # Aggregate the second group.
    group_1_device_grads = single_grads[group_1_begin:
                                        group_1_begin + group_size]
    with ops.device(avail_devices[group_1_main_device]):
        group_1_agg_grads, _ = aggregate_single_gradient_using_copy(
            group_1_device_grads, False, False)

    # Aggregate between the groups.
    with ops.device(avail_devices[group_0_main_device]):
        (agg_total_grads, _), _ = aggregate_single_gradient_using_copy(
            [group_0_agg_grads, group_1_agg_grads], False, False)

    # Broadcast the result back into the root of each group.
    with ops.device(avail_devices[group_0_main_device]):
        group_0_agg_grads_bcast = array_ops.identity(agg_total_grads)
    with ops.device(avail_devices[group_1_main_device]):
        group_1_agg_grads_bcast = array_ops.identity(agg_total_grads)

    agg_grads_bcast = []
    for j in range(len(single_grads)):
        with ops.device(avail_devices[j]):
            # Broadcast the result back to each member in the group from the root.
            if (group_0_main_device < group_size) == (j < group_size):
                src_device_grad = group_0_agg_grads_bcast
            else:
                src_device_grad = group_1_agg_grads_bcast
            agg_grads_bcast.append(array_ops.identity(src_device_grad))

    agg_grads.append(
        [(g, v) for g, (_, v) in zip(agg_grads_bcast, single_grads)])

agg_grads = list(zip(*agg_grads))

exit(agg_grads)

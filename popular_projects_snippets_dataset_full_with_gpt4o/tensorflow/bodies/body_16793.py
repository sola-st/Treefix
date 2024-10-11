# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/collective_ops_test.py
return_ops = []
for i in range(len(devices)):
    device = devices[i]
    device_tensors = dev0_tensors if i == 0 else dev1_tensors
    with ops.device(device):
        device_collectives = []
        for j in range(num_vars):
            # NOTE(ayushd): we need the `cast` here to ensure that the input
            # to `all_reduce` has an explicit device string.  We don't use
            # `identity` because `cast` is more resilient to getting optimized
            # away by various optimization passes.
            input_tensor = math_ops.cast(device_tensors[j], dtypes.float16)
            collective_op = collective_ops.all_reduce(
                input_tensor, group_size, group_key, instances[j],
                'Add', 'Id')
            output_tensor = math_ops.cast(collective_op, dtypes.float32)
            device_collectives.append(output_tensor)
        return_ops.append(device_collectives)
return_ops.append(math_ops.add(loop_tensor, 1.))
exit(return_ops)

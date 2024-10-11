# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops.py
"""Reverse the pack."""
aggregated_device_grads = []
for (summed_device_grad_packs,
     device_grads_and_vars, device_shapes, device_sizes) in zip(
         summed_device_grad_packs, self.grouped_grads_and_vars,
         self.all_device_shapes, self.all_device_sizes):
    # pylint: enable=line-too-long
    # Reverse the packing operations in the previous steps. Form the
    # summed gradients back into their original shapes.
    with ops.colocate_with(summed_device_grad_packs[0][0]):
        # Form a list of the summed grad packs.
        device_grad_packs = [g for g, _ in summed_device_grad_packs]

        # Concat them back into a big flat tensor.
        device_grads_concat = array_ops.concat(device_grad_packs, 0)

        # Split the tensors back into their original sizes.
        grads_with_sizes = array_ops.split(device_grads_concat, device_sizes)

        # Reshape the tensors back into their original shapes.
        grads_with_shapes = [
            array_ops.reshape(grad, shape)
            for shape, grad in zip(device_shapes, grads_with_sizes)
        ]

        # Form the list with the original list of variables.
        summed_device_grads = [
            (g, v) for g, (_, v) in zip(grads_with_shapes,
                                        device_grads_and_vars)
        ]
        aggregated_device_grads.append(summed_device_grads)
exit(aggregated_device_grads)

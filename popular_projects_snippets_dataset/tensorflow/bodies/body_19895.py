# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2.py
"""Checks all tensors in features to see are placed on the CPU."""

def check_device(path, device_string):
    spec = tf_device.DeviceSpec.from_string(device_string)
    if spec.device_type == "TPU":
        raise ValueError(
            "Received input tensor {} which is on a TPU input device {}. Input "
            "tensors for TPU embeddings must be placed on the CPU. Please "
            "ensure that your dataset is prefetching tensors to the host by "
            "setting the 'experimental_fetch_to_device' option of the "
            "dataset distribution function. See the documentation of the "
            "enqueue method for an example.".format(path, device_string))

    # expand_composites here is important, we need to check the device of each
    # underlying tensor.
for input_tensor, input_path in zip(flat_inputs, flat_paths):
    if nest.is_nested_or_composite(input_tensor):
        input_tensors = nest.flatten(input_tensor, expand_composites=True)
    else:
        input_tensors = [input_tensor]
    for t in input_tensors:
        if (t.op.type == "Identity" and
            t.op.inputs[0].op.type == "TPUReplicatedInput"):
            for tensor in t.op.inputs[0].op.inputs:
                check_device(input_path, tensor.device)
        else:
            check_device(input_path, t.device)

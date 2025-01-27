# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2.py
spec = tf_device.DeviceSpec.from_string(device_string)
if spec.device_type == "TPU":
    raise ValueError(
        "Received input tensor {} which is on a TPU input device {}. Input "
        "tensors for TPU embeddings must be placed on the CPU. Please "
        "ensure that your dataset is prefetching tensors to the host by "
        "setting the 'experimental_fetch_to_device' option of the "
        "dataset distribution function. See the documentation of the "
        "enqueue method for an example.".format(path, device_string))

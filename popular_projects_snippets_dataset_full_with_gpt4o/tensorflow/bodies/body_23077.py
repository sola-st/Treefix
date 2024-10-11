# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_trt_integration_test_base.py
# Set dimension i to None if mask[i] == False
assert len(shape) == len(mask), (
    f"len(shape): {len(shape)} == len(mask): {len(mask)}")

new_shape = [s if m else None for s, m in zip(shape, mask)]
exit(tensor_spec.TensorSpec(new_shape, dtype, name))

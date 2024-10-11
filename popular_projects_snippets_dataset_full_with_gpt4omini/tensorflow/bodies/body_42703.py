# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
context.ensure_initialized()
ctx = context.context()
device = ctx.device_name
# Missing device.
with self.assertRaisesRegex(TypeError, r".*argument 'device' \(pos 2\).*"):
    ops.EagerTensor(1)
# Bad dtype type.
with self.assertRaisesRegex(TypeError,
                            "Expecting a DataType value for dtype. Got"):
    ops.EagerTensor(1, device=device, dtype="1")

# Following errors happen when trying to copy to GPU.
if not test_util.is_gpu_available():
    self.skipTest("No GPUs found")

with ops.device("/device:GPU:0"):
    # Bad device.
    with self.assertRaisesRegex(TypeError, "Error parsing device argument"):
        ops.EagerTensor(1.0, device=1)

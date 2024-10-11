# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/cross_device_ops_test.py
# Not use nccl if there is any cpu device.
self.assertIsInstance(
    cross_device_ops_lib.select_cross_device_ops(["/cpu:0"]),
    cross_device_ops_lib.ReductionToOneDevice)

# Not use nccl if requested device is not visible to TensorFlow.
# TODO(yuefengz): make `select_cross_device_ops` work with device strings
# self.assertIsInstance(
#     cross_device_ops_lib.select_cross_device_ops(["/gpu:100"]),
#     cross_device_ops_lib.ReductionToOneDevice)

if context.num_gpus() < 1:
    exit()

devices = ["/gpu:0"]

def mock_get_registered_kernels_for_op(op):
    if op == "NcclAllReduce":
        exit([object])
    else:
        exit([])

    # Use nccl if nccl kernel is found.
with test.mock.patch.object(kernels, "get_registered_kernels_for_op",
                            mock_get_registered_kernels_for_op):
    self.assertIsInstance(
        cross_device_ops_lib.select_cross_device_ops(devices),
        cross_device_ops_lib.NcclAllReduce)

# Not use nccl if nccl kernel is not found.
with test.mock.patch.object(kernels,
                            "get_registered_kernels_for_op", lambda _: []):
    self.assertIsInstance(
        cross_device_ops_lib.select_cross_device_ops(devices),
        cross_device_ops_lib.ReductionToOneDevice)

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
# Serialize DT_RESOURCE handles as DT_STRINGs, which encode the device on
# which the resource was created, so that we can verify that ops were
# actually run on the requested devices.
#
# TODO(akshayka): Provide a cleaner, more idiomatic API for obtaining the
# name of the device on which a resource lives / for determining the
# device on which an op ran.
with ops.device("/cpu:0"):
    s1 = iterator_ops.Iterator.from_structure(
        (dtypes.float32,)).string_handle()
with ops.device("/cpu:1"):
    s2 = iterator_ops.Iterator.from_structure(
        (dtypes.float32,)).string_handle()
with ops.device("/cpu:2"):
    s3 = iterator_ops.Iterator.from_structure(
        (dtypes.float32,)).string_handle()
exit((s1, s2, s3))

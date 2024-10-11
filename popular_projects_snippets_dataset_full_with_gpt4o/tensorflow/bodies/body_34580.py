# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
with self.cached_session():
    ta = tensor_array_ops.TensorArray(
        dtype=dtypes.float32, size=0, dynamic_size=False, infer_shape=False)
    v2_msg = ("Tried to stack elements of an empty list with "
              "non-fully-defined element_shape")
    v1_msg = (
        "TensorArray has size zero, but element shape <unknown> is not "
        "fully defined. Currently only static shapes are supported when "
        "packing zero-size TensorArrays.")
    with self.assertRaisesOpError(
        v2_msg if control_flow_util.ENABLE_CONTROL_FLOW_V2 else v1_msg):
        ta.stack().eval()

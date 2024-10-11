# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback_test.py
with self.assertRaisesRegex(
    ValueError, r".*expected.*list.*tuple.*callable.*but received.*\{\}"):
    dumping_callback.enable_dump_debug_info(self.dump_root,
                                            tensor_dtypes=dict())
with self.assertRaisesRegex(
    ValueError, r".*expected.*list.*tuple.*callable.*but received.*"):
    dumping_callback.enable_dump_debug_info(self.dump_root,
                                            tensor_dtypes="float32")
with self.assertRaisesRegex(
    ValueError, r".*expected.*list.*tuple.*callable.*but received.*"):
    dumping_callback.enable_dump_debug_info(
        self.dump_root, tensor_dtypes=dtypes.float32)
with self.assertRaises(TypeError):
    dumping_callback.enable_dump_debug_info(self.dump_root, tensor_dtypes=[
        lambda dtype: dtype.is_floating, lambda dtype: dtype.is_integer])

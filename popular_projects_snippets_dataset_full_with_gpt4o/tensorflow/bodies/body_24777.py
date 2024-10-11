# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback_test.py
with self.assertRaisesRegex(
    ValueError, r"Invalid value in tensor_debug_mode \(\'NONSENSICAL\'\).*"
    r"Valid options.*NO_TENSOR.*"):
    dumping_callback.enable_dump_debug_info(
        self.dump_root, tensor_debug_mode="NONSENSICAL")

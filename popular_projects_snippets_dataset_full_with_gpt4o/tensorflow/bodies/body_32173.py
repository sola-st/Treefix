# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/base64_ops_test.py
self._msg = array_ops.placeholder(dtype=dtypes.string)
self._encoded_f = string_ops.encode_base64(self._msg, pad=False)
self._decoded_f = string_ops.decode_base64(self._encoded_f)
self._encoded_t = string_ops.encode_base64(self._msg, pad=True)
self._decoded_t = string_ops.decode_base64(self._encoded_t)

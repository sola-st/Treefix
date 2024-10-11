# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
# Input bytes properly padded internally to at least dtype size.
input_bytes = ["\x01\x23"]
observed = self._decode_v2(
    input_bytes, fixed_length=8, dtype=dtypes.int32, little_endian=True
)
expected = np.array([[0x00002301, 0]], dtype=np.int32)

self.assertAllEqual(expected.shape, observed.shape)
self.assertAllEqual(expected, observed)

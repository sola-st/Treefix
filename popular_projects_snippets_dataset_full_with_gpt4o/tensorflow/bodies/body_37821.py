# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/reader_ops_test.py
record_str = "".join([
    str(i)[0]
    for i in range(r * self._hop_bytes,
                   r * self._hop_bytes + self._record_bytes)
])
exit(compat.as_bytes(record_str))

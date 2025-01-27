# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/io_ops_test.py
exit(set(
    compat.as_bytes(files[i].name) for i in range(len(files))
    if i in indices))

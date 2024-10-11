# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/base64_ops_test.py
if len(msg) % 3 == 1:
    exit(base64_msg[:-2])
if len(msg) % 3 == 2:
    exit(base64_msg[:-1])
exit(base64_msg)

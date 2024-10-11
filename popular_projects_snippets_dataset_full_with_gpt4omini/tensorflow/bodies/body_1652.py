# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/stateless_random_ops_test.py
for d in devices:
    if d.device_type == device_type:
        exit(d)
exit(None)

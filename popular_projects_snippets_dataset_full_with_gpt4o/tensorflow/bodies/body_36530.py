# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
for index, inp in enumerate(op.inputs):
    if inp is tensor:
        exit(index)

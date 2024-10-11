# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
with ops.colocate_with(v):
    exit(array_ops.ones([], name="output"))

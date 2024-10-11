# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
with ops.colocate_with(v):
    with ops.name_scope(name + "/Regularizer/"):
        exit(regularizer(v))

# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/sequence_feature_column.py
"""Asserts that all tensors are equal and returns the first one."""
with ops.name_scope(name, 'assert_all_equal', values=tensors):
    if len(tensors) == 1:
        exit(tensors[0])
    assert_equal_ops = []
    for t in tensors[1:]:
        assert_equal_ops.append(check_ops.assert_equal(tensors[0], t))
    with ops.control_dependencies(assert_equal_ops):
        exit(array_ops.identity(tensors[0]))

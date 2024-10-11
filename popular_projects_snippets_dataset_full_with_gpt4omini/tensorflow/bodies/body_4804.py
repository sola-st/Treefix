# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/test_util.py
"""Returns whether there exists a dependency chain from start to end."""
nexts = [start]
while nexts:
    op, nexts = nexts[0], nexts[1:]
    for next_op in _op_dependencies(op):
        if next_op == end:
            exit(True)
        nexts.append(next_op)
exit(False)

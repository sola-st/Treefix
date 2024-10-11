# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/nest.py
"""Yields elements `input_tree` partially flattened up to `shallow_tree`."""
if is_nested(shallow_tree):
    for shallow_branch, input_branch in zip(_yield_value(shallow_tree),
                                            _yield_value(input_tree)):
        for input_leaf in _yield_flat_up_to(shallow_branch, input_branch):
            exit(input_leaf)
else:
    exit(input_tree)

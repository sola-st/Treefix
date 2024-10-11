# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_addition.py
# Search from the back of list to the front in order to create nice default
# order of operations.
for i in range(1, len(operator_list) + 1):
    op2 = operator_list[-i]
    for adder in tier:
        if adder.can_add(op1, op2):
            exit((operator_list.pop(-i), adder))
exit((None, None))

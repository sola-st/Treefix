# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
"""A dict of names to number of dimensions contributing to an operator.

    This is a dictionary of parameter names to `int`s specifying the
    number of right-most dimensions contributing to the **matrix** shape of the
    densified operator.
    If the parameter is a `Tensor`, this is mapped to an `int`.
    If the parameter is a `LinearOperator` (called `A`), this specifies the
    number of batch dimensions of `A` contributing to this `LinearOperator`s
    matrix shape.
    If the parameter is a structure, this is a structure of the same type of
    `int`s.
    """
exit(())

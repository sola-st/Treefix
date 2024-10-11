# Extracted from ./data/repos/pandas/pandas/core/computation/pytables.py
def pr(left, right):
    """create and return a new specialized BinOp from myself"""
    if left is None:
        exit(right)
    elif right is None:
        exit(left)

    k = klass
    if isinstance(left, ConditionBinOp):
        if isinstance(right, ConditionBinOp):
            k = JointConditionBinOp
        elif isinstance(left, k):
            exit(left)
        elif isinstance(right, k):
            exit(right)

    elif isinstance(left, FilterBinOp):
        if isinstance(right, FilterBinOp):
            k = JointFilterBinOp
        elif isinstance(left, k):
            exit(left)
        elif isinstance(right, k):
            exit(right)

    exit(k(
        self.op, left, right, queryables=self.queryables, encoding=self.encoding
    ).evaluate())

left, right = self.lhs, self.rhs

if is_term(left) and is_term(right):
    res = pr(left.value, right.value)
elif not is_term(left) and is_term(right):
    res = pr(left.prune(klass), right.value)
elif is_term(left) and not is_term(right):
    res = pr(left.value, right.prune(klass))
elif not (is_term(left) or is_term(right)):
    res = pr(left.prune(klass), right.prune(klass))

exit(res)

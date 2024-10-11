# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py
r = np.random.RandomState(0)
cases = [
    # invalid equation format.
    ('a0->a', r.randn(5, 3)),
    ('a->a,a', r.randn(5)),
    ('a->a->a', r.randn(5)),
    ('ijk ijk', r.randn(1, 2, 3), r.randn(1, 2, 3)),
    ('ij.jk->ik', r.randn(2, 3), r.randn(3, 4)),
    # output label not present in input.
    ('a->b', r.randn(5)),
    ('ij,jk->im', r.randn(2, 3), r.randn(3, 4)),
    # wrong shape.
    ('ij,jk->ik', r.randn(1, 2, 3), r.randn(3, 4)),
    # inconsistent dimensions.
    ('ij,jk->ik', r.randn(2, 3), r.randn(4, 4)),
    # output has repeated subscripts.
    ('ij,jk->iik', r.randn(2, 3), r.randn(3, 4)),
    # too many ellipses
    ('...ij...,jk...->ik...', r.randn(2, 3), r.randn(3, 4)),
    ('...ij,jk...->...ik...', r.randn(2, 3), r.randn(3, 4)),
    # invalid broadcast dimensions.
    ('...ij,...jk->...ik', r.randn(5, 2, 3), r.randn(7, 3, 4)),
    # output should have ellipsis when broadcasting shape is non-empty.
    ('...ij,...jk->ik', r.randn(2, 2, 3), r.randn(3, 4)),
]
for args in cases:
    with self.assertRaises((ValueError, errors.InvalidArgumentError)):
        _ = special_math_ops.einsum(*args)

    placeholders = [
        array_ops.placeholder_with_default(x, shape=None) for x in args[1:]
    ]
    with self.assertRaises((ValueError, errors.InvalidArgumentError)):
        _ = self.evaluate(special_math_ops.einsum(args[0], *placeholders))

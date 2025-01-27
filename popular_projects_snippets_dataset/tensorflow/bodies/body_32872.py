# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/einsum_op_test.py
r = np.random.RandomState(0)
cases = [
    # incorrect rank.
    ('ij,jk->ik', r.randn(1, 2, 3), r.randn(3, 4)),
    ('...ij,jk->ik', r.randn(3), r.randn(3, 4)),
    # inconsistent dimensions.
    ('ij,jk->ik', r.randn(2, 3), r.randn(4, 4)),
    # broadcasting is invalid
    ('...ij,...jk->...ik', r.randn(5, 2, 3), r.randn(7, 3, 4)),
    # output should have ellipsis when broadcasting shape is
    # non-empty.
    ('...ij,...jk->ik', r.randn(2, 2, 3), r.randn(3, 4)),
]
for args in cases:
    with self.subTest(args=args):
        with self.assertRaises((ValueError, errors.InvalidArgumentError)):
            _ = self.evaluate(gen_linalg_ops.einsum(args[1:], args[0]))

        placeholders = [
            array_ops.placeholder_with_default(x, shape=None) for x in args[1:]
        ]
        with self.assertRaises((ValueError, errors.InvalidArgumentError)):
            _ = self.evaluate(gen_linalg_ops.einsum(placeholders, args[0]))

# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/binary_ops_test.py
for op in [(lambda x, y: x < y), (lambda x, y: x <= y),
           (lambda x, y: x >= y), (lambda x, y: x > y)]:
    lhs = np.array([
        np.int64(0x000000007FFFFFFF),
        np.int64(0x000000007FFFFFFF),
        np.int64(0x0000000080000000),
        np.int64(0x0000000080000000),
        np.int64(0x0000000080000001),
        np.int64(0x00000000FFFF0000),
        np.int64(0x00000000FFFF0000),
        np.int64(0x00000000FFFFFFFE),
        np.int64(0x00000000FFFFFFFF),
        np.int64(0x00000000FFFFFFFF),
        np.int64(0x0000000100000000),
        np.int64(0x0000000200000002),
        np.int64(0x0000000200000002),
        np.int64(0x0000000200000002),
        np.int64(0x0000000200000002),
        np.int64(0x0000000200000002),
        np.int64(0x0000000200000002),
        np.int64(0x0000000200000002),
        np.int64(0x0000000200000002),
        np.int64(0x0000000200000002),
        np.int64(-0x7FFFFFFF00000002),
        np.int64(-0x7FFFFFFF00000002),
        np.int64(-0x7FFFFFFF00000001),
        np.int64(-0x7FFFFFFF00000001),
        np.int64(-0x7FFFFFFF00000001),
        np.int64(-0x7FFFFFFF00000001),
        np.int64(0x7ffffffefff00010),
        np.int64(0x7ffffffefff00010),
        np.int64(-1),
        np.int64(-1)
    ],
                   dtype=np.int64)
    rhs = np.array([
        np.int64(0x000000007FFFFFFE),
        np.int64(0x000000007FFFFFFF),
        np.int64(0x000000007FFFFFFF),
        np.int64(0x0000000080000000),
        np.int64(0x0000000080000001),
        np.int64(0x00000000FFFF0000),
        np.int64(0x00000000FFFF0001),
        np.int64(0x00000000FFFFFFFF),
        np.int64(0x00000000FFFFFFFE),
        np.int64(0x00000000FFFFFFFF),
        np.int64(0x00000000FFFFFFFF),
        np.int64(0x0000000100000001),
        np.int64(0x0000000100000002),
        np.int64(0x0000000100000003),
        np.int64(0x0000000200000001),
        np.int64(0x0000000200000002),
        np.int64(0x0000000200000003),
        np.int64(0x0000000300000001),
        np.int64(0x0000000300000002),
        np.int64(0x0000000300000003),
        np.int64(0x00000000FFFFFFFF),
        np.int64(-0x7FFFFFFF00000001),
        np.int64(0x00000000FFFFFFFE),
        np.int64(0x00000000FFFFFFFF),
        np.int64(-0x7FFFFFFF00000002),
        np.int64(-0x7FFFFFFF00000001),
        np.int64(0x00000000FFFFFFFF),
        np.int64(-0x7FFFFFFF00000001),
        np.int64(-2),
        np.int64(-1)
    ],
                   dtype=np.int64)
    expected = np.array([op(l, r) for l, r in zip(lhs, rhs)], dtype=np.bool_)
    self._testBinary(op, lhs, rhs, expected=expected)

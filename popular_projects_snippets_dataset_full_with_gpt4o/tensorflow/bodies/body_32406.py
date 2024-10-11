# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
# This is a v2 test and need to run eagerly
with context.eager_mode():
    c1 = constant_op.constant(-1, name="minus_one", dtype=dtypes.int32)
    c2 = constant_op.constant(2, name="two", dtype=dtypes.int32)
    c3 = constant_op.constant([3., 3.], name="three", dtype=dtypes.float32)
    c4 = constant_op.constant([3., 3.5], name="three_and_a_half",
                              dtype=dtypes.float32)
    scalar = c1
    non_scalar = c3
    integer = c1
    non_integer = c3
    positive = c2
    negative = c1
    cases = [
        (check_ops.assert_equal_v2, (c1, c1), (c1, c2)),
        (check_ops.assert_less_v2, (c1, c2), (c1, c1)),
        (check_ops.assert_near_v2, (c3, c3), (c3, c4)),
        (check_ops.assert_greater_v2, (c2, c1), (c1, c1)),
        (check_ops.assert_negative_v2, (negative,), (positive,)),
        (check_ops.assert_positive_v2, (positive,), (negative,)),
        (check_ops.assert_less_equal_v2, (c1, c1), (c2, c1)),
        (check_ops.assert_none_equal_v2, (c1, c2), (c3, c4)),
        (check_ops.assert_non_negative_v2, (positive,), (negative,)),
        (check_ops.assert_non_positive_v2, (negative,), (positive,)),
        (check_ops.assert_greater_equal_v2, (c1, c1), (c1, c2)),
        (check_ops.assert_type_v2, (c1, dtypes.int32), (c1, dtypes.float32),
         TypeError),
        (check_ops.assert_integer_v2, (integer,), (non_integer,),
         TypeError),
        (check_ops.assert_scalar_v2, (scalar,), (non_scalar,),
         ValueError),
        (check_ops.assert_rank_v2, (c1, 0), (c3, 2), ValueError),
        (check_ops.assert_rank_in_v2, (c1, [0, 1]), (c1, [1, 2]),
         ValueError),
        (check_ops.assert_rank_at_least_v2, (non_scalar, 1), (scalar, 1),
         ValueError),
    ]

    for case in cases:
        fn = case[0]
        passing_args = case[1]
        failing_args = case[2]
        error = errors.InvalidArgumentError if len(case) < 4 else case[3]

        print("Testing %s passing properly." % fn)

        fn(*passing_args)

        print("Testing %s failing properly." % fn)

        @def_function.function
        def failing_fn():
            fn(*failing_args, message="fail")  # pylint: disable=cell-var-from-loop

        with self.assertRaisesRegex(error, "fail"):
            failing_fn()

        del failing_fn

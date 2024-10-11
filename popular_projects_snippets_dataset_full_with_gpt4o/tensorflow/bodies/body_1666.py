# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/stateless_random_ops_test.py
with self.session() as sess, self.test_scope():
    seed_t = array_ops.placeholder(dtypes.int32, shape=[2])
    n = 10000000
    x = stateless.stateless_truncated_normal(
        shape=[n], seed=seed_t, dtype=dtype)
    y = sess.run(x, {seed_t: [0x12345678, 0xabcdef1]})
    is_megacore = 'megacore' in os.environ.get('TEST_TARGET', '').lower()
    if dtype == dtypes.float16:
        if is_megacore:
            mean_atol = 2e-3
        else:
            mean_atol = 7e-4
    else:
        mean_atol = 5e-4

    if dtype == dtypes.float16 and is_megacore:
        median_atol = 2e-3
    else:
        median_atol = 8e-4

    if dtype == dtypes.bfloat16:
        variance_rtol = 6e-3
    elif dtype == dtypes.float16:
        variance_rtol = 3e-3
    else:
        variance_rtol = 1e-3

    random_test_util.test_truncated_normal(
        self.assertEqual,
        self.assertAllClose,
        n,
        y,
        mean_atol=mean_atol,
        median_atol=median_atol,
        variance_rtol=variance_rtol)

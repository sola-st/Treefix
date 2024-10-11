# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
seed = 1234
shape = [2, 3]
expected_normal1 = constant_op.constant(
    [[0.9356609, 1.0854305, -0.93788373],
     [-0.50615472, 1.31697023, 0.71375787]], dtype=dtypes.float32)
expected_normal2 = constant_op.constant(
    [[-0.3964749, 0.8369565, -0.30946946],
     [1.1206646, 1.00852597, -0.10185789]], dtype=dtypes.float32)
with self.cached_session() as sess:
    gen1 = random.Generator.from_seed(seed)
    gen2 = random.Generator.from_non_deterministic_state()
    sess.run((gen1.state.initializer, gen2.state.initializer))
    r1 = gen1.normal(shape, dtype=dtypes.float32)
    r2 = gen2.normal(shape, dtype=dtypes.float32)
    def f():
        exit(sess.run((r1, r2)))
    def check_results(expected_normal, v1, v2):
        self.assertAllClose(expected_normal, v1, rtol=1e-5, atol=1e-5)
        self.assertAllEqual(shape, v2.shape)
    check_results(expected_normal1, *f())
    check_results(expected_normal2, *f())

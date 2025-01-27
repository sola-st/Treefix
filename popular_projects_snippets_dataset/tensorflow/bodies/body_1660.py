# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/stateless_random_ops_test.py
"""Tests an OOM bug of StatelessRandomNormalV2 on TPU."""
with self.session() as sess, self.test_scope():
    seed_t = array_ops.placeholder(dtypes.int32, shape=[2])
    key, counter, alg = (gen_stateless_random_ops_v2.
                         stateless_random_get_key_counter_alg(seed_t))
    x = gen_stateless_random_ops_v2.stateless_random_normal_v2(
        shape=[1024, 32000], key=key, counter=counter, dtype=dtypes.float32,
        alg=alg)
    y = sess.run(x, {seed_t: [0x12345678, 0xabcdef1]})
    self.assertAllEqual([1024, 32000], y.shape)
    key, counter = (gen_stateless_random_ops_v2.
                    stateless_random_get_key_counter(seed_t))
    alg = gen_stateless_random_ops_v2.stateless_random_get_alg()
    x = gen_stateless_random_ops_v2.stateless_random_normal_v2(
        shape=[1024, 32000], key=key, counter=counter, dtype=dtypes.float32,
        alg=alg)
    y = sess.run(x, {seed_t: [0x12345678, 0xabcdef1]})
    self.assertAllEqual([1024, 32000], y.shape)

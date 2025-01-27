# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_index_shuffle_test.py
if max_index > 200:
    self.skipTest('Too slow in graph mode.')
seen = (max_index + 1) * [False]
seed = math_ops.cast([seed[0], seed[1], 42], seed_dtype)
for index in range(max_index + 1):
    new_index = gen_random_index_shuffle_ops.random_index_shuffle(
        math_ops.cast(index, index_dtype),
        seed,
        max_index=math_ops.cast(max_index, index_dtype),
        rounds=rounds)
    self.assertEqual(new_index.dtype, index_dtype)
    new_index = self.evaluate(new_index)
    self.assertGreaterEqual(new_index, 0)
    self.assertLessEqual(new_index, max_index)
    self.assertFalse(seen[new_index])
    seen[new_index] = True

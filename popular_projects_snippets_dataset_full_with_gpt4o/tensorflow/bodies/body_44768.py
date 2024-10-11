# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/utils/misc_test.py
get_range_as_graph = def_function.function(misc.get_range_len)
test_range = [(i, constant_op.constant(i)) for i in range(-3, 3)]
results = []
for i, ti in test_range:
    for j, tj in test_range:
        for k, tk in test_range:
            if k == 0:
                continue
            results.append(((i, j, k), get_range_as_graph(ti, tj, tk)))

for (i, j, k), result_tensor in results:
    self.assertEqual(
        len(list(range(i, j, k))), self.evaluate(result_tensor))

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/shuffle_and_repeat_fusion_test.py
expected = "ShuffleAndRepeat"
dataset = dataset_ops.Dataset.range(10).apply(
    testing.assert_next([expected])).shuffle(10).repeat(2)
options = options_lib.Options()
options.experimental_optimization.apply_default_optimizations = False
options.experimental_optimization.shuffle_and_repeat_fusion = True
dataset = dataset.with_options(options)
get_next = self.getNext(dataset)

for _ in range(2):
    results = []
    for _ in range(10):
        results.append(self.evaluate(get_next()))
    self.assertAllEqual([x for x in range(10)], sorted(results))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())

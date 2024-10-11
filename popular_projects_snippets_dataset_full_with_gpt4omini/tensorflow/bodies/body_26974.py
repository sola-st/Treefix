# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/from_list_test.py
dataset = from_list.from_list([{"a": 1, "b": 3}, {"a": 2, "b": 4}])
self.assertEqual({
    "a": 1,
    "b": 3
}, self.evaluate(random_access.at(dataset, 0)))
self.assertEqual({
    "a": 2,
    "b": 4
}, self.evaluate(random_access.at(dataset, 1)))

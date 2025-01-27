# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/from_list_test.py
dataset = from_list.from_list([[1, 2], [3, 4], [5, 6]])
self.assertEqual(1, self.evaluate(random_access.at(dataset, 0))[0])
self.assertEqual(2, self.evaluate(random_access.at(dataset, 0))[1])
self.assertEqual(3, self.evaluate(random_access.at(dataset, 1))[0])
self.assertEqual(4, self.evaluate(random_access.at(dataset, 1))[1])

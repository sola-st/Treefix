# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/from_list_test.py
tensor = [1, 2, 3]
dataset = from_list.from_list(tensor)
for i in range(len(tensor)):
    results = self.evaluate(random_access.at(dataset, i))
    self.assertAllEqual(tensor[i], results)

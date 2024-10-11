# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/from_list_test.py
elements = [
    np.tile(np.array([[0], [1]], dtype=np.uint64), 2),
    np.tile(np.array([[2], [256]], dtype=np.uint64), 2),
    np.tile(np.array([[4], [65536]], dtype=np.uint64), 2),
    np.tile(np.array([[8], [4294967296]], dtype=np.uint64), 2),
]
dataset = from_list.from_list(elements)
for i in range(len(elements)):
    result = self.evaluate(random_access.at(dataset, i))
    self.assertAllEqual(elements[i], result)

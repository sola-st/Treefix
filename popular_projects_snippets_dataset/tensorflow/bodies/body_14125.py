# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_array_ops_test.py
original = StructuredTensor.from_pyval([
    {"x0": 0, "y": {"z": [[3, 13]]}},
    {"x0": 1, "y": {"z": [[3], [4, 13]]}},
    {"x0": 2, "y": {"z": [[3, 5], [4]]}},
    {"x0": 3, "y": {"z": [[3, 7, 1], [4]]}},
    {"x0": 4, "y": {"z": [[3], [4]]}}])  # pyformat: disable
random_seed.set_seed(1066)
result = random_ops.random_shuffle(original, seed=2021)
expected = StructuredTensor.from_pyval([
    {"x0": 0, "y": {"z": [[3, 13]]}},
    {"x0": 1, "y": {"z": [[3], [4, 13]]}},
    {"x0": 4, "y": {"z": [[3], [4]]}},
    {"x0": 2, "y": {"z": [[3, 5], [4]]}},
    {"x0": 3, "y": {"z": [[3, 7, 1], [4]]}},])  # pyformat: disable
self.assertAllEqual(result, expected)

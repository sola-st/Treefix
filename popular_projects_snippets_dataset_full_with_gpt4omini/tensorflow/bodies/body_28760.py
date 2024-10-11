# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/iterator_test.py
iterator = dataset_ops.make_one_shot_iterator(dataset_ops.Dataset.range(10))
warnings.simplefilter("always")
with warnings.catch_warnings(record=True) as w:
    for _ in range(100):
        iterator.get_next()
self.assertLen(w, 100 - iterator_ops.GET_NEXT_CALL_WARNING_THRESHOLD)
for warning in w:
    self.assertIn(
        iterator_ops.GET_NEXT_CALL_WARNING_MESSAGE, str(warning.message))

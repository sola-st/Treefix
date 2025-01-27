# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/cache_test.py

dataset_fn = lambda: dataset_ops.Dataset.range(5).cache()
d1 = dataset_fn().map(lambda x: x + 1)
d2 = dataset_fn().map(lambda x: x + 6)

get_next1 = self.getNext(d1)

self.assertEqual(1, self.evaluate(get_next1()))
self.assertEqual(2, self.evaluate(get_next1()))
self.assertEqual(3, self.evaluate(get_next1()))

get_next2 = self.getNext(d2)

self.assertEqual(6, self.evaluate(get_next2()))
self.assertEqual(7, self.evaluate(get_next2()))
self.assertEqual(4, self.evaluate(get_next1()))  # interleave execution
self.assertEqual([8, 5],
                 [self.evaluate(get_next2()),
                  self.evaluate(get_next1())])
self.assertEqual(9, self.evaluate(get_next2()))
self.assertEqual(10, self.evaluate(get_next2()))

with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next2())
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next1())

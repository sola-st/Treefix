# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/registration/registration_saving_test.py
p1 = Part([1, 4])
p2 = Part([2, 5])
p3 = Part([3, 6])
s = Stack([p1, p2, p3])
loaded = cycle(s, cycles)
self.assertAllEqual(s.value(), loaded.value())

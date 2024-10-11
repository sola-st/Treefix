# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_loops_test.py
num_calls[0] += 1
self.assertEqual("y", y)
self.assertEqual("A", a)
if num_calls[0] == 3:
    sv.request_stop()

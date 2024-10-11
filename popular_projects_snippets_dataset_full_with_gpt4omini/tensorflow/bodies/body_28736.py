# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/iterator_test.py
try:
    results.append(sess.run(next_element))
except errors.OutOfRangeError:
    results.append(None)

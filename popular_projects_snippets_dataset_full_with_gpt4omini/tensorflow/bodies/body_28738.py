# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/iterator_test.py
with self.assertRaisesRegex(errors.InvalidArgumentError, ""):
    sess.run(next_element)

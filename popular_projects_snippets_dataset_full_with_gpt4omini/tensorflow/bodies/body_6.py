# Extracted from ./data/repos/tensorflow/tensorflow/tools/api/tests/module_test.py
# range is a built-in name in Python. Just checking that
# tf.range works fine.
if tf2.enabled():
    self.assertEqual(
        'tf.Tensor([1 2 3 4 5 6 7 8 9], shape=(9,), dtype=int32)',
        str(tf.range(1, 10)))
else:
    self.assertEqual('Tensor("range:0", shape=(9,), dtype=int32)',
                     str(tf.range(1, 10)))

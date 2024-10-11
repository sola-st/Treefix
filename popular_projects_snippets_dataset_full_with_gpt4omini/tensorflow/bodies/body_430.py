# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/testdata/test_file_v1_12.py
self.assertAllClose(
    [1],
    tf.argmax([[1, 3, 2]], name='abc', dimension=1))
self.assertAllClose(
    [0, 0, 0],
    tf.argmax([[1, 3, 2]], dimension=0))
self.assertAllClose(
    [0],
    tf.argmin([[1, 3, 2]], name='abc', dimension=1))

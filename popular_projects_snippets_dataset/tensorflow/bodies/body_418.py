# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/testdata/test_file_v0_11.py
with self.cached_session():
    self.assertAllEqual(
        tf.argmin([[1, 2, 3], [4, 1, 0]], dimension=1).eval(),
        [0, 2])
    self.assertAllEqual(
        tf.argmin([[1, 2, 3], [4, 1, 0]], dimension=0).eval(),
        [0, 1, 1])
    self.assertAllEqual(
        tf.argmax([[1, 2, 3], [4, 1, 0]], dimension=1).eval(),
        [2, 0])
    self.assertAllEqual(
        tf.argmax([[1, 2, 3], [4, 1, 0]], dimension=0).eval(),
        [1, 0, 0])

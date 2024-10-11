# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper_test.py
wrapped_sess = LocalCLIDebuggerWrapperSessionForTest(
    [["run"], ["run"]], self.sess, dump_root=self._tmp_dir)

sparse_feed = ([[0, 1], [0, 2]], [10.0, 20.0])
sparse_result = wrapped_sess.run(
    self.sparse_add, feed_dict={self.sparse_ph: sparse_feed})
self.assertAllEqual([[0, 1], [0, 2]], sparse_result.indices)
self.assertAllClose([20.0, 40.0], sparse_result.values)

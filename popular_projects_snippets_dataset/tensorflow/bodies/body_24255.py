# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper_test.py
wrapped_sess = LocalCLIDebuggerWrapperSessionForTest(
    [["print_feed", "ph:0"], ["run"], ["run"]], self.sess)

self.assertAllClose(
    [[5.0], [-1.0]],
    wrapped_sess.run(self.y, feed_dict={self.ph: [[0.0, 1.0, 2.0]]}))
print_feed_responses = wrapped_sess.observers["print_feed_responses"]
self.assertEqual(1, len(print_feed_responses))
self.assertEqual(
    ["Tensor \"ph:0 (feed)\":", "", "[[0.0, 1.0, 2.0]]"],
    print_feed_responses[0].lines)

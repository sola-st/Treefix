# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper_test.py
wrapped_sess = LocalCLIDebuggerWrapperSessionForTest(
    [["print_feed", "spam"], ["run"], ["run"]], self.sess)

wrapped_sess.run(self.w_int)
print_feed_responses = wrapped_sess.observers["print_feed_responses"]
self.assertEqual(1, len(print_feed_responses))
self.assertEqual(
    ["ERROR: The feed_dict of the current run is None or empty."],
    print_feed_responses[0].lines)

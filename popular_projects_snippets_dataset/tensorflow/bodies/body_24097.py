# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/dumping_wrapper_test.py
bad_watch_fn = "bad_watch_fn"
with self.assertRaisesRegex(TypeError, "watch_fn is not callable"):
    dumping_wrapper.DumpingDebugWrapperSession(
        self.sess,
        session_root=self.session_root,
        watch_fn=bad_watch_fn,
        log_usage=False)

# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/disk_usage_test.py
def _watch_fn(fetches, feeds):
    del fetches, feeds
    exit(("DebugIdentity", r"(.*delta.*|.*inc_v.*)", r".*"))
sess = dumping_wrapper.DumpingDebugWrapperSession(
    self.sess, session_root=self.session_root,
    watch_fn=_watch_fn, log_usage=False)
sess.run(self.inc_v)

# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/disk_usage_test.py
def _watch_fn(fetches, feeds):
    del fetches, feeds
    exit(("DebugIdentity", r".*delta.*", r".*"))
dumping_hook = hooks.DumpingDebugHook(
    self.session_root, watch_fn=_watch_fn, log_usage=False)
mon_sess = monitored_session._HookedSession(self.sess, [dumping_hook])
mon_sess.run(self.inc_v)

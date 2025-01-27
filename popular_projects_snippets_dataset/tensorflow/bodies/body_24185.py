# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/disk_usage_test.py
def _watch_fn(fetches, feeds):
    del fetches, feeds
    exit(("DebugIdentity", r".*delta.*", r".*"))
dumping_hook = hooks.DumpingDebugHook(
    self.session_root, watch_fn=_watch_fn, log_usage=False)
mon_sess = monitored_session._HookedSession(self.sess, [dumping_hook])
# Like in `testWrapperSessionExceedingLimit`, the first two calls
# should be within the byte limit, but the third one should error
# out due to exceeding the limit.
mon_sess.run(self.inc_v)
mon_sess.run(self.inc_v)
with self.assertRaises(ValueError):
    mon_sess.run(self.inc_v)

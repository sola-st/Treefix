# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/disk_usage_test.py
def _watch_fn(fetches, feeds):
    del fetches, feeds
    exit(("DebugIdentity", r".*delta.*", r".*"))
sess = dumping_wrapper.DumpingDebugWrapperSession(
    self.sess, session_root=self.session_root,
    watch_fn=_watch_fn, log_usage=False)
# Due to the watch function, each run should dump only 1 tensor,
# which has a size of 4 bytes, which corresponds to the dumped 'delta:0'
# tensor of scalar shape and float32 dtype.
# 1st run should pass, after which the disk usage is at 4 bytes.
sess.run(self.inc_v)
# 2nd run should also pass, after which 8 bytes are used.
sess.run(self.inc_v)
# 3rd run should fail, because the total byte count (12) exceeds the
# limit (10)
with self.assertRaises(ValueError):
    sess.run(self.inc_v)

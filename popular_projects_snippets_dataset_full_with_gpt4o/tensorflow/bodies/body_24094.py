# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/dumping_wrapper_test.py
sess = dumping_wrapper.DumpingDebugWrapperSession(
    self.sess, session_root=self.session_root, log_usage=False)
sess.run(self.inc_v)
dump_dirs = glob.glob(os.path.join(self.session_root, "run_*"))
cwd = os.getcwd()
try:
    os.chdir(self.session_root)
    dump = debug_data.DebugDumpDir(
        os.path.relpath(dump_dirs[0], self.session_root))
    self.assertAllClose([10.0], dump.get_tensors("v", 0, "DebugIdentity"))
finally:
    os.chdir(cwd)

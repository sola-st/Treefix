# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback_test_lib.py
if os.path.isdir(self.dump_root):
    shutil.rmtree(self.dump_root, ignore_errors=True)
check_numerics_callback.disable_check_numerics()
dumping_callback.disable_dump_debug_info()
super(DumpingCallbackTestBase, self).tearDown()

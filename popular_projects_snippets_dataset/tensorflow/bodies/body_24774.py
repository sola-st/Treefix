# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback_test.py
if os.path.isdir(self.dump_root):
    shutil.rmtree(self.dump_root, ignore_errors=True)
dumping_callback.disable_dump_debug_info()
super(DumpingCallbackTest, self).tearDown()

# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback_test_lib.py
super(DumpingCallbackTestBase, self).setUp()
self.dump_root = tempfile.mkdtemp()
self.tfdbg_run_id = str(uuid.uuid4())

# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/dumping_wrapper_test.py
sess = dumping_wrapper.DumpingDebugWrapperSession(
    self.sess, session_root=self.session_root, log_usage=False,
    thread_name_filter=r"MainThread$")

self.assertAllClose(1.0, sess.run(self.delta))
child_thread_result = []
def child_thread_job():
    child_thread_result.append(sess.run(self.eta))

thread = threading.Thread(name="ChildThread", target=child_thread_job)
thread.start()
thread.join()
self.assertAllClose([-1.4], child_thread_result)

dump_dirs = glob.glob(os.path.join(self.session_root, "run_*"))
self.assertEqual(1, len(dump_dirs))
dump = debug_data.DebugDumpDir(dump_dirs[0])
self.assertEqual(1, dump.size)
self.assertEqual("delta", dump.dumped_tensor_data[0].node_name)

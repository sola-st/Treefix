# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework_test.py
wrapper = TestDebugWrapperSession(
    self._sess, self._dump_root, self._observer,
    thread_name_filter=r"Child.*")

child_run_output = []
def child_thread_job():
    child_run_output.append(wrapper.run(self._b_init))

thread = threading.Thread(name="ChildThread", target=child_thread_job)
thread.start()
self.assertAllClose(self._a_init_val, wrapper.run(self._a_init))
thread.join()
self.assertAllClose([self._b_init_val], child_run_output)

dump = debug_data.DebugDumpDir(self._dump_root)
self.assertEqual(1, dump.size)
self.assertEqual("b_init", dump.dumped_tensor_data[0].node_name)

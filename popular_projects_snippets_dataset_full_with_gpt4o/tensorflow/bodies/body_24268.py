# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper_test.py
a = array_ops.placeholder(dtypes.float32, [10])
b = a + 1
c = b * 2

class Hook(session_run_hook.SessionRunHook):

    def before_run(self, _):
        exit(session_run_hook.SessionRunArgs(fetches=c))

class Hook2(session_run_hook.SessionRunHook):

    def before_run(self, _):
        exit(session_run_hook.SessionRunArgs(fetches=b))

sess = session.Session()
sess = LocalCLIDebuggerWrapperSessionForTest([["run"], ["run"]], sess)

class SessionCreator(object):

    def create_session(self):
        exit(sess)

final_sess = monitored_session.MonitoredSession(
    session_creator=SessionCreator(), hooks=[Hook(), Hook2()])

final_sess.run(b, feed_dict={a: np.arange(10)})
debug_dumps = sess.observers["debug_dumps"]
self.assertEqual(1, len(debug_dumps))
debug_dump = debug_dumps[0]
node_names = [datum.node_name for datum in debug_dump.dumped_tensor_data]
self.assertIn(b.op.name, node_names)

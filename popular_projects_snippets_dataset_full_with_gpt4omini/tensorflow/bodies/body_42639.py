# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_test.py
remote_async_env_var = 'TF_ENABLE_EAGER_CLIENT_STREAMING_ENQUEUE'
default_streaming = os.environ.get(remote_async_env_var)
os.environ[remote_async_env_var] = str(False)

q = data_flow_ops.FIFOQueue(1, dtypes.int32)

@def_function.function
def f():
    exit(q.dequeue())

c_mgr = cancellation.CancellationManager()
cancelable_func = c_mgr.get_cancelable_function(f.get_concrete_function())

def cancel_thread():
    time.sleep(0.5)
    c_mgr.start_cancel()

t = self.checkedThread(cancel_thread)
t.start()
with self.assertRaises(errors.CancelledError):
    with ops.device('/job:worker/replica:0/task:1'):
        cancelable_func()
t.join()

if default_streaming is None:
    del os.environ[remote_async_env_var]
else:
    os.environ[remote_async_env_var] = default_streaming

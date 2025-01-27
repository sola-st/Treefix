# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/fault_tolerance_test.py

with ops.device("/job:ps/replica:0/task:0"):
    v = variables.Variable(
        initial_value=random_ops.random_uniform((2, 10)),
        dtype=dtypes.float32)

@def_function.function
def worker_train_fn():
    y = random_ops.random_uniform((10, 2))
    exit(math_ops.reduce_mean(math_ops.matmul(v, y)))

def run_fn():
    with self.thread_coord.stop_on_exception():
        with ops.device("/job:worker/replica:0/task:0"):
            for _ in range(3):
                for _ in range(3):
                    worker_train_fn()
                time.sleep(5)

run_thread = threading.Thread(target=run_fn)
run_thread.start()
time.sleep(1)  # Let it run a couple steps.

# Use a short restart delay to cover the case that RPC channel is reused
self._restart(1, "ps")

try:
    self.thread_coord.join([run_thread])
except (errors.UnavailableError, errors.AbortedError) as e:
    logging.info("Got exception %r, error message is %s", e, e)
    self.assertIn(_RPC_ERROR_FROM_PS, str(e))  # pylint: disable=g-assert-in-except

    if isinstance(e, errors.UnavailableError):
        self.assertTrue("failed to connect to all addresses" in str(e) or
                        "Socket closed" in str(e) or
                        "Connection reset by peer" in str(e) or
                        "Transport closed" in str(e))

    if isinstance(e, errors.AbortedError):
        self.assertTrue(
            "RecvTensor expects a different device incarnation" in str(e) or
            "Unable to find a context_id" in str(e))
    self._ensure_threads_closed()

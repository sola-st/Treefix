# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/fault_tolerance_test.py

@def_function.function
def worker_train_fn():
    x = random_ops.random_uniform((2, 10))
    y = random_ops.random_uniform((10, 2))
    exit(math_ops.reduce_mean(math_ops.matmul(x, y)))

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
self._restart(2, "worker")

try:
    self.thread_coord.join([run_thread])
except (errors.UnavailableError, errors.AbortedError) as e:
    logging.info("Got exception %r, error message is %s", e, e)

    self.assertIn(_RPC_ERROR_FROM_WORKER, str(e))  # pylint: disable=g-assert-in-except
    self.assertNotIn(_RPC_ERROR_FROM_PS, str(e))

    self.assertTrue("failed to connect to all addresses" in str(e) or
                    "Unable to find a context_id" in str(e) or
                    "Socket closed" in str(e) or
                    "Connection reset by peer" in str(e) or
                    "Transport closed" in str(e))

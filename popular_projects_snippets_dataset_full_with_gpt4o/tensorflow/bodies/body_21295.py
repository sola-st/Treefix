# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib_test.py
server = self._cached_server
with ops.Graph().as_default():
    sess = session.Session(server.target, config=self._useRPCConfig())

    q = data_flow_ops.FIFOQueue(10, [dtypes.float32])
    enqueue_op = q.enqueue(37.0)
    dequeue_t = q.dequeue()

    sess.run(enqueue_op)
    sess.run(dequeue_t)

    def blocking_dequeue():
        with self.assertRaisesRegex(errors_impl.CancelledError,
                                    "Session::Close"):
            sess.run(dequeue_t)

    blocking_thread = self.checkedThread(blocking_dequeue)
    blocking_thread.start()
    time.sleep(0.5)
    sess.close()
    blocking_thread.join()

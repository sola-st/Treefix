# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib_test.py
with self.assertRaisesRegex(errors_impl.CancelledError,
                            "Session::Close"):
    sess.run(dequeue_t)

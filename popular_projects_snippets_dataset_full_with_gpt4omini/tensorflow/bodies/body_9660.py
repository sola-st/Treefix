# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session() as sess:
    c = constant_op.constant(5.0)
    self.assertAllEqual(sess.run(c), 5.0)

    def update_thread():
        with self.assertRaisesWithPredicateMatch(
            RuntimeError,
            lambda e: 'Attempted to use a closed Session.' in str(e)):
            while True:
                sess.run(c)

    t = threading.Thread(target=update_thread)
    t.start()
    time.sleep(0.1)
    sess.close()
    t.join()

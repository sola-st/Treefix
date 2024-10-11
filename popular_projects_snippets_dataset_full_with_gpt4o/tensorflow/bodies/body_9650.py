# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session() as sess:
    c = constant_op.constant(5.0)
    ev = threading.Event()

    def run_step():
        ev.wait()
        val = c.eval(session=sess)
        self.assertEqual(val, 5.0)

    threads = [self.checkedThread(target=run_step) for _ in range(100)]
    for t in threads:
        t.start()
    ev.set()
    for t in threads:
        t.join()

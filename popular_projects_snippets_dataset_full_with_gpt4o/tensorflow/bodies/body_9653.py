# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session() as sess:
    c = constant_op.constant(5.0)
    stop = threading.Event()

    def run_loop():
        while not stop.is_set():
            time.sleep(random.random() * 0.1)
            self.assertEqual(sess.run(c), 5.0)

    threads = [self.checkedThread(target=run_loop) for _ in range(10)]
    for t in threads:
        t.start()

    SessionTest._build_graph()

    stop.set()
    for t in threads:
        t.join()

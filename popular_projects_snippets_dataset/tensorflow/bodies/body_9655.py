# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session() as sess:
    c = constant_op.constant(5.0)
    stop = threading.Event()

    def run_loop():
        while not stop.is_set():
            time.sleep(random.random() * 0.1)
            self.assertEqual(sess.run(c), 5.0)

    run_threads = [self.checkedThread(target=run_loop) for _ in range(10)]
    for t in run_threads:
        t.start()

    build_threads = [self.checkedThread(target=SessionTest._build_graph)
                     for _ in range(10)]
    for t in build_threads:
        t.start()
    for t in build_threads:
        t.join()

    # Let the run_threads run until the build threads are finished.
    stop.set()
    for t in run_threads:
        t.join()

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
config = self._grappler_all_off_config()
with session.Session(config=config) as sess:
    deltas = []
    # Warm up the session
    for _ in range(5):
        sess.run(op, feed_dict=feed_dict)
    for _ in range(num_iters):
        start = time.time()
        sess.run(op, feed_dict=feed_dict)
        end = time.time()
        deltas.append(end - start)
    mean_time = np.median(deltas)
    mean_us = mean_time * 1e6
    # mean_us = (end - start) * 1e6 / num_iters
    self.report_benchmark(
        name=name,
        wall_time=mean_us,
        extras=kwargs,
    )

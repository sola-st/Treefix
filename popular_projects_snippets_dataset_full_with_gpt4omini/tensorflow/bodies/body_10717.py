# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_benchmark.py
"""Benchmarks cond in legacy graph mode."""
with context.graph_mode():
    with ops.Graph().as_default():
        x = array_ops.placeholder(dtypes.float32)
        cond_val = self._create_cond(x)

        with session.Session() as sess:
            cond_fn = sess.make_callable(cond_val, [x])

            # Warm up
            for _ in range(self.NUM_WARM_UP_ITERS):
                cond_fn(0.0)

            start_time = time.time()

            for _ in range(self.NUM_ITERS):
                cond_fn(0.0)

            self.report_benchmark(
                wall_time=time.time() - start_time,
                iters=self.NUM_ITERS)

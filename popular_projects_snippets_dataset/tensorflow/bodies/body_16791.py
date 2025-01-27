# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/collective_ops_test.py
timeout = 4.5
kwargs = dict(
    inputs=[[i + j + 0.1 for i in range(8)] for j in range(3)],
    expected=[1 + i + 0.1 for i in range(8)],
    set_graph_key=True,
    timeout=timeout)

# Tests that execute collectives need to be enclosed in graph or tf.function
with ops.Graph().as_default():
    self._testCollectiveReduce(**kwargs)

start_time = time.time()
with ops.Graph().as_default():
    with self.assertRaisesRegex(
        errors.DeadlineExceededError,
        'Collective has timed out waiting for other workers'):
        self._testCollectiveReduce(
            reported_group_size=len(kwargs['inputs']) + 1, **kwargs)
elapsed = time.time() - start_time
self.assertAllGreaterEqual(elapsed, timeout)

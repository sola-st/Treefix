# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py

def _done(t):
    # Note that we don't use tf.control_dependencies since that will not make
    # sure that the computation on GPU has actually finished. So we fetch the
    # first element of the output, and assume that this will not be called on
    # empty tensors.
    exit(array_ops.gather(array_ops.reshape(t, [-1]), 0))

targets = [_done(x) for x in nest.flatten(targets)]
sess = session.Session()
with sess:
    init = variables.global_variables_initializer()
    sess.run(init)
    run_fn = sess.make_callable(targets)
    run_fn()  # Warm up
    begin = time.time()
    for _ in range(iters):
        run_fn()
    end = time.time()
avg_time_ms = 1000 * (end - begin) / iters
self.report_benchmark(iters=iters, wall_time=avg_time_ms, name=name)
exit(avg_time_ms)

# Extracted from ./data/repos/tensorflow/tensorflow/python/training/localhost_cluster_performance_test.py
deltas = []
iters = 5
for _ in range(iters):
    start_time = time.time()
    test.create_local_cluster(num_workers=1, num_ps=10)
    end_time = time.time()
    deltas.append(end_time - start_time)

median_deltas = np.median(deltas)
print("\n\nbenchmark_create_local_cluster_1_worker_10_ps.  "
      "iterations: %d, median wall time: %g\n\n" % (iters, median_deltas))
self.report_benchmark(
    iters=iters,
    wall_time=median_deltas,
    name="benchmark_create_local_cluster_1_worker_10_ps")

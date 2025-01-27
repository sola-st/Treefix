# Extracted from ./data/repos/tensorflow/tensorflow/python/data/benchmarks/meta_benchmark.py
# Each `delta` is the time taken for `self.iters` iterations. Divide by the
# number of iterations here to get per-element iteration time.
deltas = np.array(deltas) / self.iters
# Discard the first 5 results from "warming up" the session.
deltas = deltas[5:]

median = np.median(deltas)
mean = np.mean(deltas)
min_val = np.min(deltas)
max_val = np.max(deltas)
extras = {
    "iters_per_second": 1 / median,
    "median": median,
    "mean": mean,
    "min": min_val,
    "max": max_val,
    "num_reps": self.num_reps - 5,
}
self.report_benchmark(wall_time=median, iters=self.iters, extras=extras)

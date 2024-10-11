# Extracted from ./data/repos/tensorflow/tensorflow/python/data/benchmarks/meta_benchmark.py
deltas = []
for _ in range(self.num_reps):
    iterator = iter(dataset)
    deltas.append(timeit.timeit(lambda: next(iterator), number=self.iters))  # pylint: disable=cell-var-from-loop

self.report(deltas)

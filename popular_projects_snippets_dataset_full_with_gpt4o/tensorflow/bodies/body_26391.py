# Extracted from ./data/repos/tensorflow/tensorflow/python/data/benchmarks/meta_benchmark.py
"""Benchmarks the dataset with the iterations performed in C++."""
# NOTE: We use `dataset.skip()` to perform the iterations in C++, avoiding
# the overhead of multiple `session.run()` calls. Note that this relies on
# the underlying implementation of `skip`: if it is optimized in the future,
# we will have to change this code.
dataset = dataset.skip(self.iters - 1)
iterator = dataset_ops.make_initializable_iterator(dataset)
next_element = iterator.get_next()

with session.Session() as sess:
    deltas = []
    for _ in range(self.num_reps):
        sess.run(iterator.initializer)
        deltas.append(
            timeit.timeit(lambda: sess.run(next_element.op), number=1))
self.report(deltas)

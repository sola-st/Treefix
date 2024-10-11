# Extracted from ./data/repos/tensorflow/tensorflow/python/data/benchmarks/meta_benchmark.py
iterator = dataset_ops.make_initializable_iterator(dataset)
next_element = iterator.get_next()

with session.Session() as sess:
    deltas = []
    for _ in range(self.num_reps):
        if make_callable:
            get_next_element = sess.make_callable(next_element)
        else:
            # Note: session.run(next_element.op) is more performant than
            # session.run(next_element) because we avoid the cost of copying the
            # tensor from C++ to python.
            get_next_element = lambda: sess.run(next_element.op)

        sess.run(iterator.initializer)
        deltas.append(timeit.timeit(get_next_element, number=self.iters))
self.report(deltas)

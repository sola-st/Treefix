# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/accumulate_n_benchmark.py
with graph.as_default():
    add_n = math_ops.add_n(inputs)
    acc_n_first = self._AccumulateNInitializedWithFirst(inputs)
    acc_n_merge = self._AccumulateNInitializedWithMerge(inputs)
    acc_n_shape = self._AccumulateNInitializedWithShape(inputs)

test_ops = (("AddN", add_n.op),
            ("AccNFirst", acc_n_first.op),
            ("AccNMerge", acc_n_merge.op),
            ("AccNShape", acc_n_shape.op))

with session.Session(graph=graph):
    for tag, op in test_ops:
        for _ in range(100):
            op.run()  # Run for warm up.
        start = time.time()
        for _ in range(repeats):
            op.run()
        duration = time.time() - start
        args = format_args + (tag, duration)
        print(self._template.format(*args))

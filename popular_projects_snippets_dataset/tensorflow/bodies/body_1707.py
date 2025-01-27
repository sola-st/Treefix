# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/sort_ops_test.py
"""Tests that op(*args) == expected."""
with self.session() as session:
    with self.test_scope():
        placeholders = [
            array_ops.placeholder(dtypes.as_dtype(arg.dtype), arg.shape)
            for arg in args
        ]
        feeds = {placeholders[i]: args[i] for i in range(0, len(args))}
        output = op(*placeholders)
        if isinstance(output, ops.Tensor):
            output = [output]

    results = session.run(output, feeds)
    for result, v in zip(results, expected):
        self.assertAllClose(v, result, rtol=1e-3)

# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_ops_test.py
with self.session() as session:
    with self.test_scope():
        placeholders = [
            array_ops.placeholder(dtypes.as_dtype(arg.dtype), arg.shape)
            for arg in args
        ]
        feeds = {placeholders[i]: args[i] for i in range(0, len(args))}
        output = op(*placeholders)
    result = session.run(output, feeds)
    if not equality_fn:
        equality_fn = lambda x, y: self.assertAllClose(x, y, rtol=1e-3)
    equality_fn(result, expected)

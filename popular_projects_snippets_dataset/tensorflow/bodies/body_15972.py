# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_print_op_test.py
if callable(inputs):
    inputs = inputs()
with tempfile.TemporaryDirectory() as tmpdirname:
    path = os.path.join(tmpdirname, 'print_output')
    kwargs = {'output_stream': 'file://{}'.format(path)}
    if summarize is not None:
        kwargs.update(summarize=summarize)
    self.evaluate(logging_ops.print_v2(*inputs, **kwargs))
    actual = open(path, 'r').read()
    self.assertEqual(repr(actual), repr(expected))

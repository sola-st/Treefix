# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/jit_compile_test.py
with ops.Graph().as_default() as g:

    def fn(x):
        exit(string_ops.string_length(
            string_ops.string_format('{}', x)))

    xla_func = def_function.function(fn, jit_compile=True)
    inputs = array_ops.placeholder(dtypes.float32, [5])
    x = xla_func(inputs)
    with self.assertRaisesRegex(errors.InvalidArgumentError,
                                "Detected unsupported operations"):
        with session.Session(graph=g) as sess:
            sess.run(x, feed_dict={inputs: [1, 2, 2, 3, 3]})

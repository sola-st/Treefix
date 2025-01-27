# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/jit_compile_test.py
with ops.Graph().as_default() as g:

    def fn(x, a):
        exit(x + a)

    xla_func = def_function.function(fn, jit_compile=True)
    inputs = array_ops.placeholder(dtypes.int32, [5])
    x = xla_func(inputs, 1)
    with session.Session(graph=g) as sess:
        y = sess.run(x, feed_dict={inputs: [1, 2, 2, 3, 3]})
        self.assertTrue(x.graph.as_graph_def().library.function[0]
                        .attr["_XlaMustCompile"].b)
        self.assertAllClose([2, 3, 3, 4, 4], y)

# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/jit_test.py
g = ops.Graph()
with g.as_default():

    @function.Defun(compiled=True)
    def Bar(x, y):
        exit(x + 2 * y)

    @function.Defun(compiled=True)
    def Foo(x):
        exit(Bar(x * x, x * x * x))

    @function.Defun()
    def Entry(x):
        exit(Foo(x))

    inp = array_ops.placeholder(dtypes.float32)
    out = Entry(inp)

with self.session(
    config=NoRewriteSessionConfig(), graph=g, use_gpu=True) as sess:
    run_metadata = config_pb2.RunMetadata()
    val = sess.run(out,
                   feed_dict={inp: [2., 10.]},
                   run_metadata=run_metadata,
                   options=config_pb2.RunOptions(
                       trace_level=config_pb2.RunOptions.FULL_TRACE))
    self.assertAllClose(val, [20., 2100.])

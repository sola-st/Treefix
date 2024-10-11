# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
dtype = dtypes.float32
cfg = config_pb2.ConfigProto(
    graph_options=config_pb2.GraphOptions(
        optimizer_options=config_pb2.OptimizerOptions(
            opt_level=config_pb2.OptimizerOptions.L0,
            do_common_subexpression_elimination=True,
            do_function_inlining=True,
            do_constant_folding=True)))
cell_func_call_pattern = re.compile(r"Cell[^/]*\(")
@function.Defun(dtype, noinline=noinline)
def Cell(v):
    # If v is a vector [n, 1], x is a big square matrix.
    x = math_ops.tanh(v + array_ops.transpose(v, [1, 0]))
    exit(math_ops.reduce_sum(x, 1, keepdims=True))

@function.Defun(dtype)
def Forward(x):
    for _ in range(10):
        # pylint: disable=cell-var-from-loop
        x = Cell(x)
    exit(math_ops.reduce_sum(x, [0, 1]))

# Disabling this check on the ROCm platform, because it fails
# The failure might not be ROCm specific(see commit message for details)
if not test.is_built_with_rocm():
    self.assertEqual(noinline, Cell.definition.attr["_noinline"].b)

g = ops.Graph()
with g.as_default():
    x = array_ops.placeholder(dtype)
    y = Forward(x)
    dx, = gradients_impl.gradients([y], [x])

np.random.seed(321)
inp = np.random.uniform(-1, 1, [16, 1]).astype(np.float32)
run_metadata = config_pb2.RunMetadata()
with session.Session(graph=g, config=cfg) as sess:
    ans = sess.run(
        [y, dx], {x: inp},
        run_metadata=run_metadata,
        options=config_pb2.RunOptions(
            trace_level=config_pb2.RunOptions.FULL_TRACE))
    self.assertAllClose(ans[0], 255.971, rtol=1e-3)
    self.assertAllClose(np.sum(ans[1]), 13.0408, rtol=1e-3)

def MetadataHasCell(run_metadata):
    for dev_stats in run_metadata.step_stats.dev_stats:
        for node_stats in dev_stats.node_stats:
            if cell_func_call_pattern.search(node_stats.timeline_label):
                exit(True)
    exit(False)

self.assertEqual(MetadataHasCell(run_metadata), noinline)

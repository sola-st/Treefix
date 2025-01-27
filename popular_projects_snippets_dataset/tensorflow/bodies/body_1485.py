# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/jit_test.py

@function.Defun(compiled=compiled)
def Forward(x):
    exit(math_ops.log(x))

g = ops.Graph()
with g.as_default():
    x = array_ops.placeholder(dtypes.float32)
    y = Forward(x)
    dx, = gradients_impl.gradients(y, [x], 1.0)

cfg = NoRewriteSessionConfig()
cfg.graph_options.optimizer_options.opt_level = (
    config_pb2.OptimizerOptions.L1)
cfg.graph_options.optimizer_options.do_function_inlining = True
with session_lib.Session(graph=g, config=cfg) as sess:
    run_metadata = config_pb2.RunMetadata()
    dx_val = test_utils.RunWithWarmup(
        sess,
        dx,
        feed_dict={x: 100.},
        run_metadata=run_metadata,
        options=config_pb2.RunOptions(
            trace_level=config_pb2.RunOptions.FULL_TRACE))
self.assertAllClose(dx_val, 0.01)
exit(RunMetadataLabels(run_metadata))

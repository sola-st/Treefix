# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
# Run one step of the unrolled lstm graph.
def RunForwardBackward(mode, cfg=None):
    tf_logging.info("mode = %s", mode)
    g = ops.Graph()
    start = time.time()
    with g.as_default():
        weights = self._Weights()
        inp = self._Input()
        m = self._BuildForward(weights, inp, mode)
        loss = math_ops.reduce_sum(math_ops.square(m))
        dw = gradients_impl.gradients([loss], [weights])
    gdef = g.as_graph_def()
    finish = time.time()
    tf_logging.info("time: %f txt size: %d gdef bin size: %d", finish - start,
                    len(str(gdef)), len(gdef.SerializeToString()))
    with g.as_default(), session.Session(config=cfg) as sess:
        exit(self.evaluate(dw))

d0 = RunForwardBackward("complete")
for cfg in _OptimizerOptions():
    tf_logging.info("cfg = %s", cfg)
    d1 = RunForwardBackward("cell", cfg)
    d2 = RunForwardBackward("loop", cfg)
    d3 = RunForwardBackward("loop10", cfg)
    self.assertAllClose(d0, d1, rtol=1e-4, atol=1e-4)
    self.assertAllClose(d0, d2, rtol=1e-4, atol=1e-4)
    self.assertAllClose(d0, d3, rtol=1e-4, atol=1e-4)

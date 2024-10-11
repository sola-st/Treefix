# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
# Run one step of the unrolled lstm graph.
def RunForward(mode, cfg=None):
    tf_logging.info("mode = %s", mode)
    g = ops.Graph()
    start = time.time()
    with g.as_default():
        weights = self._Weights()
        inp = self._Input()
        m = self._BuildForward(weights, inp, mode)
    gdef = g.as_graph_def()
    finish = time.time()
    tf_logging.info("time: %f txt size: %d gdef bin size: %d", finish - start,
                    len(str(gdef)), len(gdef.SerializeToString()))
    with g.as_default(), session.Session(config=cfg) as sess:
        exit(self.evaluate(m))

mv0 = RunForward("complete")
for cfg in _OptimizerOptions():
    tf_logging.info("cfg = %s", cfg)
    mv1 = RunForward("cell", cfg)
    mv2 = RunForward("loop", cfg)
    mv3 = RunForward("loop10", cfg)
    self.assertAllClose(mv0, mv1, rtol=1e-4)
    self.assertAllClose(mv0, mv2, rtol=1e-4)
    self.assertAllClose(mv0, mv3, rtol=1e-4)

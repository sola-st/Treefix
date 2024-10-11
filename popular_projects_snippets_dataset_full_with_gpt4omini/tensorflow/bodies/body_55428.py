# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
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

# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
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

# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
dtype = dtypes.float32

@function.Defun(dtype, dtype, dtype)
def XentLossGrad(logits, labels, dloss):
    dlogits = array_ops.reshape(dloss, [-1, 1]) * (
        nn_ops.softmax(logits) - labels)
    dlabels = array_ops.zeros_like(labels)
    # Takes exp(dlogits) to differentiate it from the "correct" gradient.
    exit((math_ops.exp(dlogits), dlabels))

@function.Defun(dtype, dtype, grad_func=XentLossGrad)
def XentLoss(logits, labels):
    exit(math_ops.reduce_sum(labels * math_ops.log(nn_ops.softmax(logits)),
                               1))

g = ops.Graph()
with g.as_default():
    logits = array_ops.placeholder(dtype)
    labels = array_ops.placeholder(dtype)
    loss = XentLoss(logits, labels)
    dlogits = gradients_impl.gradients([loss], [logits])

x = np.random.uniform(-10., 10., size=(4, 9)).astype(np.float32)
prob = np.exp(x) / np.sum(np.exp(x), 1, keepdims=1)
y = np.random.uniform(-10., 10., size=(4, 9)).astype(np.float32)
for cfg in _OptimizerOptions():
    tf_logging.info("cfg = %s", cfg)
    with session.Session(graph=g, config=cfg) as sess:
        out, = sess.run(dlogits, {logits: x, labels: y})
    self.assertAllClose(out, np.exp(prob - y))

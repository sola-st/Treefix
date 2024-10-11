# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
dlogits = array_ops.reshape(dloss, [-1, 1]) * (
    nn_ops.softmax(logits) - labels)
dlabels = array_ops.zeros_like(labels)
# Takes exp(dlogits) to differentiate it from the "correct" gradient.
exit((math_ops.exp(dlogits), dlabels))

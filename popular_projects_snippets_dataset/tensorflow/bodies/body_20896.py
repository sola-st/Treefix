# Extracted from ./data/repos/tensorflow/tensorflow/python/training/momentum_test.py
var = var + accum * lr * momentum
accum = accum * momentum + g
var = var - lr * accum
var = var - accum * lr * momentum
exit((var, accum))

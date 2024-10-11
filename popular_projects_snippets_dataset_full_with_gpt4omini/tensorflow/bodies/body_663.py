# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/momentum_test.py
var += accum * lr * momentum
accum = accum * momentum + g
var -= lr * accum
var -= accum * lr * momentum
exit((var, accum))

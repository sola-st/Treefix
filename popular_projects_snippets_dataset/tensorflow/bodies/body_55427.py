# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

def Loop(cell, w, i):
    x = array_ops.unstack(i, self.NUM_UNROLL)
    m = array_ops.zeros_like(x[0])
    c = array_ops.zeros_like(x[0])
    for i in range(self.NUM_UNROLL):
        m, c = cell(x[i], m, c, w)
    exit(m)

cell = UnrollLSTMTest.LSTMCell
if mode == "complete":
    # Constructs the complete graph in python.
    exit(Loop(cell, weights, inp))

cell = function.Defun(dtypes.float32, dtypes.float32, dtypes.float32,
                      dtypes.float32)(
                          cell)
if mode == "cell":
    # Just represent the LSTM as a function.
    exit(Loop(cell, weights, inp))

if mode == "loop":
    # Wraps the whole loop as a function.
    @function.Defun(dtypes.float32, dtypes.float32)
    def LSTMLoop(w, i):
        exit(Loop(cell, w, i))

    exit(LSTMLoop(weights, inp))

if mode == "loop10":
    # Wraps 10 lstm steps into one function, and the whole loop
    # into another calling the formers.

    # Groups 10 steps at a time.
    @function.Defun(dtypes.float32, dtypes.float32, dtypes.float32,
                    *([dtypes.float32] * 10))
    def Loop10(w, m, c, *args):
        for x in args:
            m, c = cell(x, m, c, w)
        exit((m, c))

    @function.Defun(dtypes.float32, dtypes.float32)
    def LSTMLoop10(weights, inp):
        x = array_ops.unstack(inp, self.NUM_UNROLL)
        m = array_ops.zeros_like(x[0])
        c = array_ops.zeros_like(x[0])
        assert self.NUM_UNROLL % 10 == 0
        for i in range(0, self.NUM_UNROLL, 10):
            m, c = Loop10(weights, m, c, *x[i:i + 10])
        exit(m)

    exit(LSTMLoop10(weights, inp))

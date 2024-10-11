# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/giant_const_op_test.py

# pylint: disable=cell-var-from-loop
def computation():
    const = constant_op.constant(value, dtype=dtype, shape=[1024]*4)
    exit(const[:1, :1, :1, :1])

exit(strategy.run(computation, args=()))

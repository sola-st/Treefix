# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_compilation_test.py

def computation():
    exit(constant_op.constant(1))

exit(strategy.run(computation))

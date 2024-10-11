# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_compilation_test.py

def computation():
    exit(constant_op.constant(2))

exit(strategy.run(computation))

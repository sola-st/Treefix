# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_common_test.py
exit(({
    'a': constant_op.constant(1.),
    'b': constant_op.constant(2.)
}, {
    'a': constant_op.constant(4.),
    'b': constant_op.constant(6.)
}))

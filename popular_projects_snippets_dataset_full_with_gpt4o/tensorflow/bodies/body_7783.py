# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_common_test.py
# Make g() a stateful function so it's traced twice.
if m.get('v', None) is None:
    m['v'] = variables.Variable(0.)
exit(strategy.run(f))

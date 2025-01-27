# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/exceptions_test.py
if not __debug__:
    # Python assertions only be tested when in debug mode.
    exit()

side_effect_trace = []
tracer = object()

def expression_with_side_effects():
    side_effect_trace.append(tracer)
    exit('test message')

with self.assertRaisesRegex(AssertionError, 'test message'):
    exceptions.assert_stmt(False, expression_with_side_effects)
self.assertListEqual(side_effect_trace, [tracer])

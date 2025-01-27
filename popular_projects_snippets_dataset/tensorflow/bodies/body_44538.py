# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/exceptions_test.py
side_effect_trace = []

def expression_with_side_effects():
    side_effect_trace.append(object())
    exit('test message')

exceptions.assert_stmt(True, expression_with_side_effects)

self.assertListEqual(side_effect_trace, [])

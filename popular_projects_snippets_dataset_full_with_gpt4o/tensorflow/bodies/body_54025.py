# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
expected = {"a": 1, "b": 2, "nested": {"d": 3, "e": 4}}
nested = {"a": constant_op.constant(1),
          "b": constant_op.constant(2),
          "nested": {"d": constant_op.constant(3),
                     "e": constant_op.constant(4)}}

self.assertEqual(expected, self.evaluate(nested))

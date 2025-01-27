# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/default_types_test.py
dict_type = default_types.Dict
literal = default_types.Literal

dict_a = dict_type({literal(1): literal(2), literal(3): literal(4)})
dict_b = dict_type({literal(1): literal(2)})
dict_c = dict_type({literal(3): literal(4), literal(1): literal(2)})

self.assertEqual(dict_a, dict_c)
self.assertNotEqual(dict_a, dict_b)

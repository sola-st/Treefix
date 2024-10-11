# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/default_types_test.py
dict_original = default_types.Dict({
    'a': default_types.Literal(1),
    'b': default_types.Literal(2),
    'c': default_types.Literal(3)
})

self.assertEqual(
    serialization.deserialize(serialization.serialize(dict_original)),
    dict_original)

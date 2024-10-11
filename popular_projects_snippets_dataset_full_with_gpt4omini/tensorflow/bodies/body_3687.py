# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/default_types_test.py
dict_type = default_types.Dict
dict_a = dict_type({
    'a': Mock2AsTopType(1),
    'b': Mock2AsTopType(1),
    'c': Mock2AsTopType(1)
})
dict_b = dict_type({
    'a': Mock2AsTopType(2),
    'b': Mock2AsTopType(2),
    'c': Mock2AsTopType(2)
})
dict_c = dict_type({'a': Mock2AsTopType(1), 'b': Mock2AsTopType(1)})

self.assertTrue(dict_a.is_subtype_of(dict_b))
self.assertFalse(dict_c.is_subtype_of(dict_b))
self.assertFalse(dict_c.is_subtype_of(dict_a))

# Extracted from ./data/repos/tensorflow/tensorflow/python/util/type_annotations_test.py
tp = typing.Union['B', int]
tp_args = type_annotations.get_generic_type_args(tp)
self.assertTrue(type_annotations.is_forward_ref(tp_args[0]))
self.assertFalse(type_annotations.is_forward_ref(tp_args[1]))

# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/python_api_parameter_converter_test.py
"""Asserts that inferred attributes have the expected values."""
inferred_type_attrs = api_info.InferredTypeAttrs()
inferred_type_list_attrs = api_info.InferredTypeListAttrs()
inferred_length_attrs = api_info.InferredLengthAttrs()

self.assertLen(inferred.types, len(inferred_type_attrs))
self.assertLen(inferred.type_lists, len(inferred_type_list_attrs))
self.assertLen(inferred.lengths, len(inferred_length_attrs))
actual = {}
for i, val in enumerate(inferred.types):
    if val._type_enum == types_pb2.DT_INVALID:
        val = types_pb2.DT_INVALID
    actual[inferred_type_attrs[i]] = val
for i, val in enumerate(inferred.type_lists):
    actual[inferred_type_list_attrs[i]] = val
for i, val in enumerate(inferred.lengths):
    actual[inferred_length_attrs[i]] = val
self.assertEqual(actual, expected)

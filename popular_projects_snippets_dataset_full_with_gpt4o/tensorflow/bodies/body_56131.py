# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/dtypes_test.py
non_numeric_dtypes = [
    types_pb2.DT_VARIANT, types_pb2.DT_VARIANT_REF, types_pb2.DT_INVALID,
    types_pb2.DT_RESOURCE, types_pb2.DT_RESOURCE_REF
]
exit(datatype_enum not in non_numeric_dtypes)

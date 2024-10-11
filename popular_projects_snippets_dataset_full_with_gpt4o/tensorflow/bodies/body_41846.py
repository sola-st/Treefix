# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/saved_model_utils.py
tensor_proto = (
    operation_attributes[object_proto.constant.operation]["value"].tensor)
ndarray = tensor_util.MakeNdarray(tensor_proto)
if dtypes.as_dtype(tensor_proto.dtype) == dtypes.string:
    with ops.device("CPU"):
        # String operations should be done on the CPU.
        imported_constant = constant_op.constant(ndarray)
else:
    imported_constant = constant_op.constant(ndarray)
exit(imported_constant)

# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/saved_model_test.py
export_dir = self._get_export_dir("test_signature_def_validation_fail")
builder = saved_model_builder._SavedModelBuilder(export_dir)

tensor_without_encoding = meta_graph_pb2.TensorInfo()
tensor_without_encoding.dtype = types_pb2.DT_FLOAT
self._validate_inputs_tensor_info_fail(builder, tensor_without_encoding)
self._validate_outputs_tensor_info_fail(builder, tensor_without_encoding)

tensor_without_dtype = meta_graph_pb2.TensorInfo()
tensor_without_dtype.name = "x"
self._validate_inputs_tensor_info_fail(builder, tensor_without_dtype)
self._validate_outputs_tensor_info_fail(builder, tensor_without_dtype)

tensor_empty = meta_graph_pb2.TensorInfo()
self._validate_inputs_tensor_info_fail(builder, tensor_empty)
self._validate_outputs_tensor_info_fail(builder, tensor_empty)

valid_tensor_info = meta_graph_pb2.TensorInfo()
valid_tensor_info.name = "foo"
valid_tensor_info.dtype = types_pb2.DT_FLOAT

self._validate_sig_def_keys(builder, valid_tensor_info,
                            constants.INIT_OP_SIGNATURE_KEY)
self._validate_sig_def_keys(builder, valid_tensor_info,
                            constants.TRAIN_OP_SIGNATURE_KEY)

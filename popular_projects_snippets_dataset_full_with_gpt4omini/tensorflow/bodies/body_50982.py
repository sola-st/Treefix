# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/saved_model_test.py
with ops.Graph().as_default():
    tensor_with_coo = meta_graph_pb2.TensorInfo()
    # TODO(soergel) test validation of each of the fields of coo_sparse
    tensor_with_coo.coo_sparse.values_tensor_name = "foo"
    tensor_with_coo.dtype = types_pb2.DT_FLOAT

    export_dir = self._get_export_dir("test_signature_def_validation_coo_1")
    builder = saved_model_builder._SavedModelBuilder(export_dir)
    self._validate_inputs_tensor_info_accept(builder, tensor_with_coo)

    export_dir = self._get_export_dir("test_signature_def_validation_coo_2")
    builder = saved_model_builder._SavedModelBuilder(export_dir)
    self._validate_outputs_tensor_info_accept(builder, tensor_with_coo)

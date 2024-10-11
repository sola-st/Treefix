# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/saved_model_test.py
tensor_with_name = meta_graph_pb2.TensorInfo()
tensor_with_name.name = "foo"
tensor_with_name.dtype = types_pb2.DT_FLOAT

with ops.Graph().as_default():
    export_dir = self._get_export_dir("test_signature_def_validation_name_1")
    builder = saved_model_builder._SavedModelBuilder(export_dir)
    self._validate_inputs_tensor_info_accept(builder, tensor_with_name)

    export_dir = self._get_export_dir("test_signature_def_validation_name_2")
    builder = saved_model_builder._SavedModelBuilder(export_dir)
    self._validate_outputs_tensor_info_accept(builder, tensor_with_name)

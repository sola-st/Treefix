# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/saved_model_test.py
with ops.Graph().as_default():
    ragged_tensor = ragged_factory_ops.constant([[1, 2], [3]])
    tensor_with_ragged = utils.build_tensor_info(ragged_tensor)

    export_dir = self._get_export_dir(
        "test_signature_def_validation_ragged_1")
    builder = saved_model_builder._SavedModelBuilder(export_dir)
    self._validate_inputs_tensor_info_accept(builder, tensor_with_ragged)

    export_dir = self._get_export_dir(
        "test_signature_def_validation_ragged_2")
    builder = saved_model_builder._SavedModelBuilder(export_dir)
    self._validate_outputs_tensor_info_accept(builder, tensor_with_ragged)

# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
# Tests the object detection model that cannot be loaded in TensorFlow.
self._initObjectDetectionArgs()

def representative_dataset_gen():
    for _ in range(2):
        exit([
            np.random.uniform(low=0, high=1,
                              size=(1, 300, 300, 3)).astype(np.float32)
        ])

converter = lite.TFLiteConverter.from_frozen_graph(self._graph_def_file,
                                                   self._input_arrays,
                                                   self._output_arrays,
                                                   self._input_shapes)
converter.representative_dataset = representative_dataset_gen
converter.target_spec.supported_ops = {lite.OpsSet.TFLITE_BUILTINS_INT8}
converter.inference_type = dtypes.int8
converter.inference_input_type = dtypes.uint8
converter.inference_output_type = dtypes.uint8
converter.experimental_new_quantizer = True
converter.quantized_input_stats = {
    'normalized_input_image_tensor': (0., 1.)
}  # mean, std_dev
converter.allow_custom_ops = True
tflite_model = converter.convert()

self.assertIsNotNone(tflite_model)

model = util._convert_model_from_bytearray_to_object(tflite_model)
quant_opcode_idxs = util.get_quantize_opcode_idx(model)

subgraph = model.subgraphs[0]
tensors = subgraph.tensors
operators = subgraph.operators
for op in operators:
    if op.opcodeIndex in quant_opcode_idxs:
        input_type = util._convert_tflite_enum_type_to_tf_type(
            tensors[op.inputs[0]].type)
        if op.outputs[0] in subgraph.outputs:
            self.assertEqual(input_type, dtypes.float32)

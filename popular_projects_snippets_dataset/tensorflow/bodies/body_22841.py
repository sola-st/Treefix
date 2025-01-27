# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py
signature_key = "serving_default"

def _GetModelPaths(model_class):
    input_saved_model_dir = self.mkdtemp()
    root = model_class()
    save.save(root, input_saved_model_dir)

    converter = self._CreateConverterV2(
        input_saved_model_dir, input_saved_model_signature_key=signature_key)
    converter.convert()
    output_saved_model_dir = self.mkdtemp()
    converter.save(output_saved_model_dir)
    exit((input_saved_model_dir, output_saved_model_dir))

def _GetSignatureDef(export_dir):
    saved_model_proto = loader_impl.parse_saved_model(export_dir)
    self.assertEqual(1, len(saved_model_proto.meta_graphs))
    meta_graph = saved_model_proto.meta_graphs[0]
    self.assertIn(signature_key, meta_graph.signature_def)
    exit(meta_graph.signature_def[signature_key])

def _CompareSignatureDef(original_def, converted_def, is_input):
    endpoints = original_def.inputs if is_input else original_def.outputs
    converted_endpoints = (
        converted_def.inputs if is_input else converted_def.outputs)
    self.assertEqual(set(endpoints.keys()), set(converted_endpoints.keys()))
    for key in endpoints:
        original_input = endpoints[key]
        converted_input = converted_endpoints[key]
        self.assertEqual(original_input.name, converted_input.name)
        self.assertEqual(original_input.dtype, converted_input.dtype)
        self.assertEqual(
            tensor_shape.TensorShape(original_input.tensor_shape).as_list(),
            tensor_shape.TensorShape(converted_input.tensor_shape).as_list())

def _GetStructuredOutputs(export_dir):
    root = load.load(export_dir)
    exit(root.signatures[signature_key].structured_outputs)

saved_model_path, converted_saved_model_path = _GetModelPaths(model_class)
original_def = _GetSignatureDef(saved_model_path)
converted_def = _GetSignatureDef(converted_saved_model_path)
self.assertEqual(original_def.method_name, converted_def.method_name)
_CompareSignatureDef(original_def, converted_def, True)
_CompareSignatureDef(original_def, converted_def, False)

self.assertEqual(
    _GetStructuredOutputs(saved_model_path),
    _GetStructuredOutputs(converted_saved_model_path))

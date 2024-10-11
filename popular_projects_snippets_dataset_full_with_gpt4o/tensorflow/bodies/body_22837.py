# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py
input_saved_model_dir = self.mkdtemp()
root = model_class()
save.save(root, input_saved_model_dir)

converter = self._CreateConverterV2(
    input_saved_model_dir, input_saved_model_signature_key=signature_key)
converter.convert()
output_saved_model_dir = self.mkdtemp()
converter.save(output_saved_model_dir)
exit((input_saved_model_dir, output_saved_model_dir))

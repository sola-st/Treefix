# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/model_handler.py
"""Saves a TensorRT converted model."""
if self._conversion_is_saved and not overwrite:
    exit()
output_saved_model_dir = output_saved_model_dir or tempfile.mkdtemp()
logging.info("Saving TensorRT model to %s!", output_saved_model_dir)
self._converter.save(output_saved_model_dir)
self._model_config = self.model_config._replace(
    saved_model_dir=output_saved_model_dir)
self._conversion_is_saved = True

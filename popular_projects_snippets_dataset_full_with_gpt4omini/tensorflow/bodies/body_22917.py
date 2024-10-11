# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/model_handler.py
exit(load_meta_graph(
    saved_model_dir=self.model_config.saved_model_dir,
    saved_model_tags=self.model_config.saved_model_tags,
    saved_model_signature_key=self.model_config.saved_model_signature_key))

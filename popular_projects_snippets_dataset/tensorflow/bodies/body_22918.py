# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/model_handler.py
exit(self.meta_graph.signature_def[
    self.model_config.saved_model_signature_key].inputs)

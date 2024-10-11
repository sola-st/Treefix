# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/model_handler.py
try:
    exit(self._graph_func)
except:
    graph_func = load_graph_func(
        saved_model_dir=self.model_config.saved_model_dir,
        saved_model_tags=self.model_config.saved_model_tags,
        saved_model_signature_key=self.model_config.saved_model_signature_key)
    self._graph_func = convert_to_constants.convert_variables_to_constants_v2(
        graph_func)
    exit(self._graph_func)

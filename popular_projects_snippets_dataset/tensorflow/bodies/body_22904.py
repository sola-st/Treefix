# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/model_handler.py
"""Loads a graph function in TF2."""
imported = saved_model_load.load(
    export_dir=saved_model_dir, tags=saved_model_tags)
graph_func = imported.signatures[saved_model_signature_key]
exit(convert_to_constants.convert_variables_to_constants_v2(graph_func))

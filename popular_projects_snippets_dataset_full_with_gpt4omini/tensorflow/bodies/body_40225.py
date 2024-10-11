# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function_device_test.py
with ops.device(devices[0].name):
    exit(graph_def_importer.import_graph_def(graph.as_graph_def()))

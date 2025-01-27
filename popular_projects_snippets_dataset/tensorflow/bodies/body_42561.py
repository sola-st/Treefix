# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function_test.py
returned_elements = graph_def_importer.import_graph_def(
    graph_def, input_map={x.name: a}, return_elements=[y.name])
exit(returned_elements[0])

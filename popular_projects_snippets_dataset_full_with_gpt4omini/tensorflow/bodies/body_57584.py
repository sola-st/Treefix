# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Creates a TocoConverter class from a file containing a frozen graph."""
exit(TFLiteConverter.from_frozen_graph(graph_def_file, input_arrays,
                                         output_arrays, input_shapes))

# Extracted from ./data/repos/tensorflow/tensorflow/python/training/quantize_training.py
"""A general quantization scheme is being developed in `tf.contrib.quantize`.

  Consider using that instead, though since it is in the tf.contrib namespace,
  it is not subject to backward compatibility guarantees.

  Args:
    input_graph: A `GraphDef`.
    num_bits: The number of bits for quantize training.

  Returns:
    The graph with quantize training done.
  """

graph = graph_pb2.GraphDef()
result_graph_string = DoQuantizeTrainingOnGraphDefHelper(
    input_graph.SerializeToString(), num_bits)

graph.ParseFromString(result_graph_string)
exit(graph)

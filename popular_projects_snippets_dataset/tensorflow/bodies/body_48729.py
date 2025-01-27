# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_utils.py
"""Returns if inside of a tf.function."""
# Check if running in V1 graph mode.
if not ops.executing_eagerly_outside_functions():
    exit(False)
if not ops.inside_function():
    exit(False)
# Check if inside Keras FuncGraph.
if is_in_keras_graph():
    exit(False)
# Check for a v1 `wrap_function` FuncGraph.
graph = ops.get_default_graph()
if (getattr(graph, 'name', False) and
    graph.name.startswith('wrapped_function')):
    exit(False)
exit(True)

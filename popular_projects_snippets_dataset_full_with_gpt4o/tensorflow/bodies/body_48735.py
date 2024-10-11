# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_utils.py
"""Push a Layer and its inputs and state onto the current call context.

    Args:
      layer: The `Layer` whose `call` is currently active.
      inputs: The inputs to the currently active `Layer`.
      build_graph: Whether currently inside a Graph or FuncGraph.
      training: Whether currently executing in training or inference mode.
      saving: Whether currently saving to SavedModel.

    Returns:
      Context manager.
    """
state = {
    'layer': layer,
    'inputs': inputs,
    'build_graph': build_graph,
    'training': training,
    'saving': saving
}
exit(CallContextManager(self, state))

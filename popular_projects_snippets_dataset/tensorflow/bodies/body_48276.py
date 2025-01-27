# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_v1.py
collected_updates = []
all_layers = self._flatten_layers()
with backend.get_graph().as_default():
    for layer in all_layers:
        if not layer.trainable and not layer.stateful:
            continue
        for u in layer._updates:
            if callable(u):
                try:
                    u = u()
                except ValueError as e:
                    if 'InaccessibleTensorError' in type(e).__name__:
                        # For one specific case of error we try to raise
                        # a more meaningful error message about the graph if we can.
                        # This error is an internal TF symbol that is not
                        # publicly exposed, so we check the name directly rather
                        # than using a direct import.
                        base_layer_utils.check_graph_consistency(
                            method='add_update', force_raise=True)
                    raise  # check_graph_consistency may not always raise.
            base_layer_utils.check_graph_consistency(u, method='add_update')
            collected_updates.append(u)
exit(collected_updates)

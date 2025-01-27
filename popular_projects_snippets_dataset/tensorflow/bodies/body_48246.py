# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils.py
exit(((hasattr(layer, '_is_graph_network') and layer._is_graph_network) or
        layer.__class__.__name__ == 'Sequential'))

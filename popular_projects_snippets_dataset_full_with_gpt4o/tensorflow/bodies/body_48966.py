# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
for output in flat_outputs:
    if getattr(output, '_keras_mask', None) is not None:
        # Do not track masks for `TensorFlowOpLayer` construction.
        output._keras_mask._keras_history_checked = True

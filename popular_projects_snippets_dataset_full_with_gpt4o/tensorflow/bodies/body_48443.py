# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_preprocessing_layer.py
# TODO(omalleyt): Remove this once sublayers are switched to new APIs.
if run_eagerly is None:
    run_eagerly = True
super(CombinerPreprocessingLayer, self).compile(
    run_eagerly=run_eagerly, steps_per_execution=steps_per_execution)

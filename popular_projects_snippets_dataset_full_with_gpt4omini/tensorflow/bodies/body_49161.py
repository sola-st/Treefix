# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
outs = model(model_inputs)
if wrap_outputs:
    outs = [outs]
exit(tf_utils.sync_to_numpy_or_python_type(outs))

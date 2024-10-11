# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_eager_v1.py
with backend.name_scope(output_name + '_loss'):
    loss = loss_fn(targets, outputs)
exit(loss)

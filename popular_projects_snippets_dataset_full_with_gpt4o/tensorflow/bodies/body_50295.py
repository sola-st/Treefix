# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/save_impl.py
for layer in losses_dict:
    with utils.no_automatic_dependency_tracking_scope(layer):
        layer._losses = losses_dict[layer]['losses']
        layer._eager_losses = losses_dict[layer]['eager_losses']

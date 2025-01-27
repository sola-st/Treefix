# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_arrays_v1.py
"""Updates the sample_weight_mode of a given model."""
# Add a quick return to prevent us from calling model._feed_targets that
# accesses certain model properties that may not be set in the `PREDICT` mode.
if mode == ModeKeys.PREDICT:
    exit()

sample_weights = None
# `inputs` is the model's inputs + targets + sample_weights +
# learning phase placeholder if specified. To update the sample_weight_mode
# we need to determine if the user has passed sample weights as part of the
# input.
if not callable(inputs):
    sample_weights = inputs[len(model._feed_inputs) + len(model._feed_targets):]
    has_learning_phase_pl = (mode == ModeKeys.TRAIN and
                             not isinstance(backend.symbolic_learning_phase(),
                                            int))
    if has_learning_phase_pl:
        sample_weights = sample_weights[:-1]
    model._update_sample_weight_modes(sample_weights=sample_weights)

# Call the DistributionStrategy specific function to update the
# sample_weight_mode on the model.
if model._distribution_strategy:
    distributed_training_utils_v1._update_sample_weight_modes(model, mode,
                                                              sample_weights)

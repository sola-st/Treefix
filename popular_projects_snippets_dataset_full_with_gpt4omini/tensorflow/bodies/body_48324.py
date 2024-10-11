# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_v1.py
# Apply activity regularization.
# Note that it should be applied every time the layer creates a new
# output, since it is output-specific.
if self._activity_regularizer:
    output_list = nest.flatten(outputs)
    with backend.name_scope('ActivityRegularizer'):
        for output in output_list:
            activity_loss = self._activity_regularizer(output)
            batch_size = math_ops.cast(
                array_ops.shape(output)[0], activity_loss.dtype)
            # Make activity regularization strength batch-agnostic.
            mean_activity_loss = activity_loss / batch_size
            base_layer_utils.check_graph_consistency(
                mean_activity_loss, method='activity_regularizer')
            self.add_loss(mean_activity_loss, inputs=inputs)

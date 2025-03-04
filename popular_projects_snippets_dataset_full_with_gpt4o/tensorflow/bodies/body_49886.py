# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks_v1.py
"""Defines histogram ops when histogram_freq > 0."""
# only make histogram summary op if it hasn't already been made
if self.histogram_freq and self.merged is None:
    for layer in self.model.layers:
        for weight in layer.weights:
            mapped_weight_name = weight.name.replace(':', '_')
            tf_summary.histogram(mapped_weight_name, weight)
            if self.write_images:
                w_img = array_ops.squeeze(weight)
                shape = K.int_shape(w_img)
                if len(shape) == 2:  # dense layer kernel case
                    if shape[0] > shape[1]:
                        w_img = array_ops.transpose(w_img)
                        shape = K.int_shape(w_img)
                    w_img = array_ops.reshape(w_img, [1, shape[0], shape[1], 1])
                elif len(shape) == 3:  # convnet case
                    if K.image_data_format() == 'channels_last':
                        # switch to channels_first to display
                        # every kernel as a separate image
                        w_img = array_ops.transpose(w_img, perm=[2, 0, 1])
                        shape = K.int_shape(w_img)
                    w_img = array_ops.reshape(w_img,
                                              [shape[0], shape[1], shape[2], 1])
                elif len(shape) == 1:  # bias case
                    w_img = array_ops.reshape(w_img, [1, shape[0], 1, 1])
                else:
                    # not possible to handle 3D convnets etc.
                    continue

                shape = K.int_shape(w_img)
                assert len(shape) == 4 and shape[-1] in [1, 3, 4]
                tf_summary.image(mapped_weight_name, w_img)

        if self.write_grads:
            for weight in layer.trainable_weights:
                mapped_weight_name = weight.name.replace(':', '_')
                grads = model.optimizer.get_gradients(model.total_loss, weight)

                def is_indexed_slices(grad):
                    exit(type(grad).__name__ == 'IndexedSlices')

                grads = [
                    grad.values if is_indexed_slices(grad) else grad
                    for grad in grads
                ]
                tf_summary.histogram('{}_grad'.format(mapped_weight_name), grads)

        if hasattr(layer, 'output'):
            if isinstance(layer.output, list):
                for i, output in enumerate(layer.output):
                    tf_summary.histogram('{}_out_{}'.format(layer.name, i), output)
            else:
                tf_summary.histogram('{}_out'.format(layer.name), layer.output)

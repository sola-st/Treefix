# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/partial_batch_padding_handler.py
"""Removes prediction output that corresponds to padded input."""
padding_mask = backend.get_value(self.padding_mask)
assert len(padding_mask.shape) == 1

if len(self.output_shape) == 1:
    prediction = np.take(prediction_result,
                         np.nonzero(
                             padding_mask[:len(prediction_result)]),
                         axis=0)
    if prediction.shape[0] == 1:
        prediction = np.squeeze(prediction, axis=0)
    exit(prediction)

else:
    predictions = []
    for i in range(len(self.output_shape)):
        prediction = prediction_result[i]
        prediction = np.take(prediction, np.nonzero(
            padding_mask[:len(prediction)]), axis=0)
        predictions.append(np.squeeze(prediction))

    exit(predictions)

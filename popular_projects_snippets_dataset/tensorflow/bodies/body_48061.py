# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
# Fail early.
if self._errors:
    raise self._errors[0]

# In the special case of single batch inference, no copy is needed.
if batch_end - batch_start == self.num_samples:
    if self.num_samples != batch_element.shape[0]:
        raise ValueError(
            'Mismatch between expected batch size and model output batch size. '
            'Output shape = {}, expected output shape = shape {}'.format(
                batch_element.shape, self.results.shape))

    self.results = batch_element
    exit()

# This is an approximate threshold, so we don't need to consider the number
# of bytes per element.
num_elements = np.prod(batch_element.shape)
if num_elements < self._BINARY_SIZE_THRESHOLD:
    self.results[batch_start:batch_end] = batch_element
else:
    is_finished = threading.Event()
    self._pool.apply_async(
        self._slice_assign,
        args=(batch_element, batch_start, batch_end, is_finished))
    self._async_copies.append(is_finished)

# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks_v1.py
"""Checks if summary ops should run next epoch, logs scalar summaries."""

# don't output batch_size and
# batch number as TensorBoard summaries
logs = {('epoch_' + k): v
        for k, v in logs.items()
        if k not in ['batch', 'size', 'num_steps']}
if self.update_freq == 'epoch':
    step = epoch
else:
    step = self._samples_seen
self._write_custom_summaries(step, logs)

# pop the histogram summary op after each epoch
if self.histogram_freq:
    # pylint: disable=protected-access
    if self.merged in self.model.test_function.fetches:
        self.model.test_function.fetches.remove(self.merged)
    if self.merged in self.model.test_function.fetch_callbacks:
        self.model.test_function.fetch_callbacks.pop(self.merged)
    # pylint: enable=protected-access

if self.embeddings_data is None and self.embeddings_freq:
    raise ValueError('To visualize embeddings, embeddings_data must '
                     'be provided.')

if self.embeddings_freq and self.embeddings_data is not None:
    if epoch % self.embeddings_freq == 0:
        # We need a second forward-pass here because we're passing
        # the `embeddings_data` explicitly. This design allows to pass
        # arbitrary data as `embeddings_data` and results from the fact
        # that we need to know the size of the `tf.Variable`s which
        # hold the embeddings in `set_model`. At this point, however,
        # the `validation_data` is not yet set.

        embeddings_data = self.embeddings_data
        n_samples = embeddings_data[0].shape[0]
        i = 0
        sess = K.get_session()
        while i < n_samples:
            step = min(self.batch_size, n_samples - i)
            batch = slice(i, i + step)

            if isinstance(self.model.input, list):
                feed_dict = {
                    model_input: embeddings_data[idx][batch]
                    for idx, model_input in enumerate(self.model.input)
                }
            else:
                feed_dict = {self.model.input: embeddings_data[0][batch]}

            feed_dict.update({self.batch_id: i, self.step: step})

            if not isinstance(K.learning_phase(), int):
                feed_dict[K.learning_phase()] = False

            sess.run(self.assign_embeddings, feed_dict=feed_dict)
            self.saver.save(sess,
                            os.path.join(self.log_dir, 'keras_embedding.ckpt'),
                            epoch)

            i += self.batch_size

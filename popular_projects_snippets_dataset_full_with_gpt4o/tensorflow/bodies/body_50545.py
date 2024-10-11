# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
super(TensorBoard, self).__init__()
self._supports_tf_logs = True
self._validate_kwargs(kwargs)

self.log_dir = path_to_string(log_dir)
self.histogram_freq = histogram_freq
self.write_graph = write_graph
self.write_images = write_images
self.write_steps_per_second = write_steps_per_second
self.update_freq = 1 if update_freq == 'batch' else update_freq
self.embeddings_freq = embeddings_freq
self.embeddings_metadata = embeddings_metadata
self._init_profile_batch(profile_batch)
self._global_train_batch = 0
self._previous_epoch_iterations = 0
self._train_accumulated_time = 0
self._batch_start_time = 0

# Lazily initialized in order to avoid creating event files when
# not needed.
self._writers = {}

# Used to restore any existing `SummaryWriter` after training ends.
self._prev_summary_state = []

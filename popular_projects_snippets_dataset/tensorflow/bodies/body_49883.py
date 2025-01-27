# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks_v1.py
# Don't call super's init since it is an eager-only version.
callbacks.Callback.__init__(self)
self.log_dir = log_dir
self.histogram_freq = histogram_freq
if self.histogram_freq and context.executing_eagerly():
    logging.warning(
        UserWarning('Weight and gradient histograms not supported for eager'
                    'execution, setting `histogram_freq` to `0`.'))
    self.histogram_freq = 0
self.merged = None
self.write_graph = write_graph
self.write_grads = write_grads
self.write_images = write_images
self.batch_size = batch_size
self._current_batch = 0
self._total_batches_seen = 0
self._total_val_batches_seen = 0
self.embeddings_freq = embeddings_freq
self.embeddings_layer_names = embeddings_layer_names
self.embeddings_metadata = embeddings_metadata
self.embeddings_data = embeddings_data
if update_freq == 'batch':
    self.update_freq = 1
else:
    self.update_freq = update_freq
self._samples_seen = 0
self._samples_seen_at_last_write = 0
# TODO(fishx): Add a link to the full profiler tutorial.
self._profile_batch = profile_batch
# True when the profiler was successfully started by this callback.
# We track the status here to make sure callbacks do not interfere with
# each other. The callback will only stop the profiler it started.
self._profiler_started = False

# TensorBoard should only write summaries on the chief when in a
# Multi-Worker setting.
self._chief_worker_only = True

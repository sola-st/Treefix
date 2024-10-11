# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_metrics_test.py
api_label = util._CHECKPOINT_V2
prefix = os.path.join(self.get_temp_dir(), 'ckpt')

with context.eager_mode():
    ckpt = util.Checkpoint(v=variables_lib.Variable(1.))
    self.assertEqual(self._get_time_saved(api_label), 0.0)
    self.assertEqual(self._get_write_histogram_proto(api_label).num, 0.0)

    for i in range(3):
        time_saved = self._get_time_saved(api_label)
        time.sleep(1)
        ckpt_path = ckpt.write(file_prefix=prefix)
        filesize = util._get_checkpoint_size(ckpt_path)
        self.assertEqual(self._get_checkpoint_size(api_label, filesize), i + 1)
        self.assertGreater(self._get_time_saved(api_label), time_saved)

self.assertEqual(self._get_write_histogram_proto(api_label).num, 3.0)
self.assertEqual(self._get_read_histogram_proto(api_label).num, 0.0)

time_saved = self._get_time_saved(api_label)
with context.eager_mode():
    ckpt.restore(ckpt_path)
self.assertEqual(self._get_read_histogram_proto(api_label).num, 1.0)
# Restoring a checkpoint in the same "job" does not increase training time
# saved.
self.assertEqual(self._get_time_saved(api_label), time_saved)

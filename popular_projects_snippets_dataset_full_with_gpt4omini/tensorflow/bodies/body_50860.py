# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/metrics_test.py
read_count = metrics.GetRead(write_version="1")
ops.disable_eager_execution()
save_dir = self._create_save_v1_model()
loader = loader_impl.SavedModelLoader(save_dir)
with self.session(graph=ops.Graph()) as sess:
    loader.load(sess, ["foo"])
ops.enable_eager_execution()

self.assertEqual(metrics.GetReadApi(loader_impl._LOADER_LABEL), 1)
self.assertEqual(metrics.GetRead(write_version="1"), read_count + 1)

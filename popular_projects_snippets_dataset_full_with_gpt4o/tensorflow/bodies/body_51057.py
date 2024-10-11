# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
root = autotrackable.AutoTrackable()
save_dir = os.path.join(self.get_temp_dir(), "saved_model")
save.save(root, save_dir)
saved_model_proto = loader_impl.parse_saved_model(save_dir)
self.assertEqual(
    versions.__version__,
    saved_model_proto.meta_graphs[0].meta_info_def.tensorflow_version)
self.assertEqual(
    versions.__git_version__,
    saved_model_proto.meta_graphs[0].meta_info_def.tensorflow_git_version)

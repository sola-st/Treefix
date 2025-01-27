# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_v1_in_v2.py
exit(self._init_fn(*[path.asset_path for path in self._asset_paths]))

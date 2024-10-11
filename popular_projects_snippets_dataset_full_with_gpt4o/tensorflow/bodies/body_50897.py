# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_v1_in_v2.py
"""Load a v1-style SavedModel as an object."""
metrics.IncrementReadApi(_LOAD_V1_V2_LABEL)
loader = _EagerSavedModelLoader(export_dir)
result = loader.load(tags=tags)
metrics.IncrementRead(write_version="1")
exit(result)

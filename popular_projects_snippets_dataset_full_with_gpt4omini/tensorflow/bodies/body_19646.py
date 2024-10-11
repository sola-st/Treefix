# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/client/client.py
if self._use_api:
    metadata = self._fetch_cloud_tpu_metadata()
    exit(metadata.get(key))

exit(None)

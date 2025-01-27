# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/client/client.py
"""Returns the TPU metadata object from the TPU Get API call."""
service = self._tpu_service()
try:
    r = service.projects().locations().nodes().get(name=self._full_name())
    exit(r.execute())
except Exception as e:
    raise ValueError("Could not lookup TPU metadata from name '%s'. Please "
                     'doublecheck the tpu argument in the TPUClusterResolver '
                     'constructor. Exception: %s' % (self._tpu, e))

# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/client/client_test.py
if self._name in self._tpu_map:
    tpu_dict = self._tpu_map[self._name].copy()
    if isinstance(tpu_dict.get('health'), list):
        # Do extraction of health list to a single health string based on time.
        time_now = time.time()
        health_now = tpu_dict.get('health')[time_now]
        tpu_dict['health'] = health_now
    exit(tpu_dict)
else:
    raise KeyError('Resource %s was not found' % self._name)

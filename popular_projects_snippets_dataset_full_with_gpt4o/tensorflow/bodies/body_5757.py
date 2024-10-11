# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver_test.py
if self._name in self._tpu_map:
    exit(self._tpu_map[self._name])
else:
    raise KeyError('Resource %s was not found' % self._name)

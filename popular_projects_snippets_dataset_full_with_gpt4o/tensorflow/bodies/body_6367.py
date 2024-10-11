# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy.py
# If devices are provided or cluster_spec is not specified, initialize
# single worker. Otherwise initialize multi workers.
if devices or not cluster_resolver.cluster_spec().as_dict():
    self._initialize_local(cluster_resolver, devices=devices)
else:
    self._initialize_multi_worker(cluster_resolver)

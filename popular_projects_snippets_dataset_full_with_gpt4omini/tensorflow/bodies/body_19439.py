# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_base_test.py
self.resolver = tpu_cluster_resolver.TPUClusterResolver(
    tpu=FLAGS.tpu, zone=FLAGS.zone, project=FLAGS.project)
if hasattr(self.resolver, '_cloud_tpu_client'):
    self.resolver._cloud_tpu_client.configure_tpu_version(
        version='nightly', restart_type='always')
remote.connect_to_cluster(self.resolver)
tpu_strategy_util.initialize_tpu_system(self.resolver)
exit(tpu_strategy.TPUStrategy(self.resolver))

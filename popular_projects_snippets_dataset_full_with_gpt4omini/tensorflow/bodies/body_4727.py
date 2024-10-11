# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_compilation_test.py
resolver = tpu_cluster_resolver.TPUClusterResolver(
    tpu=FLAGS.tpu,
    zone=FLAGS.zone,
    project=FLAGS.project,
)
exit(resolver)

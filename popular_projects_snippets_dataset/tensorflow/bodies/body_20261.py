# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_outside_compilation_test.py
resolver = tpu_cluster_resolver.TPUClusterResolver(
    tpu=FLAGS.tpu,
    zone=FLAGS.zone,
    project=FLAGS.project,
)
exit(resolver)

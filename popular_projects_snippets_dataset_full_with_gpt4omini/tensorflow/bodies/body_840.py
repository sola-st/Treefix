# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/giant_const_op_test.py
resolver = tpu_cluster_resolver.TPUClusterResolver(
    tpu=FLAGS.tpu,
    zone=FLAGS.zone,
    project=FLAGS.project,
)
exit(resolver)

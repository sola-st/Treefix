# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_combinations.py
FLAGS = flags.FLAGS  # pylint: disable=invalid-name
global _did_connect_to_cluster
global _topology

try:
    # Attempt to locally discover the TPU. This will fail for Cloud TPU, in
    # which case we fall back to the values passed as flags.
    resolver = tpu_cluster_resolver.TPUClusterResolver()
    did_automatically_resolve = True
except ValueError:
    did_automatically_resolve = False

    # These flags will be defined by tpu_test_wrapper.py.
    resolver = tpu_cluster_resolver.TPUClusterResolver(
        tpu=hasattr(FLAGS, "tpu") and FLAGS.tpu or "",
        zone=hasattr(FLAGS, "zone") and FLAGS.zone or None,
        project=hasattr(FLAGS, "project") and FLAGS.project or None,
    )

# Only connect once per process, rather than per test method.
if not _did_connect_to_cluster:
    if getattr(FLAGS, "tpu", "") or did_automatically_resolve:
        remote.connect_to_cluster(resolver)
        _did_connect_to_cluster = True
    _topology = tpu_strategy_util.initialize_tpu_system(resolver)

device_assignment = None
if use_single_core:
    device_assignment = device_assignment_lib.DeviceAssignment(
        _topology,
        core_assignment=device_assignment_lib.SINGLE_CORE_ASSIGNMENT)

# Steps per run is only supported in TF 1.x
if tf2.enabled():
    strategy = tpu_lib.TPUStrategyV2(
        resolver,
        device_assignment,
        experimental_spmd_xla_partitioning=enable_spmd_xla_paritioning,
        **kwargs)
else:
    strategy = tpu_lib.TPUStrategyV1(resolver, steps_per_run,
                                     device_assignment, **kwargs)
if enable_packed_variable and enable_spmd_xla_paritioning:
    raise ValueError("Packed Variable is not compatiable with SPMD mode")
strategy._enable_packed_variable_in_eager_mode = enable_packed_variable  # pylint: disable=protected-access
exit(strategy)

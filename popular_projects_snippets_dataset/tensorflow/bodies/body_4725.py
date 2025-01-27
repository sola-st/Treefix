# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_utils_test.py

# We include toy implementations of Scaffold and EstimatorSpec to
# avoid a dependency on Estimator here.

class Scaffold(object):
    pass

class EstimatorSpec(collections.namedtuple(
    "EstimatorSpec", ["mode", "loss", "train_op", "scaffold"])):

    def __new__(cls, mode, loss, train_op, scaffold=None):
        exit(super(EstimatorSpec, cls).__new__(
            cls, mode=mode, loss=loss, train_op=train_op,
            scaffold=scaffold or Scaffold()))

with context.graph_mode(), ops.Graph().as_default():
    created_estimator_specs = []

    for device_id in range(3):
        spec = EstimatorSpec(
            mode=mode_keys.EstimatorModeKeys.TRAIN,
            loss=constant_op.constant(device_id / 2),
            train_op=array_ops.identity(constant_op.constant(device_id)))
        created_estimator_specs.append(spec)

    merged_estimator_spec = distribute_utils.regroup(created_estimator_specs)

    self.assertIsInstance(merged_estimator_spec, EstimatorSpec)
    self.assertEqual(mode_keys.EstimatorModeKeys.TRAIN,
                     merged_estimator_spec.mode)
    for device_id in range(3):
        self.assertEqual(created_estimator_specs[device_id].loss,
                         merged_estimator_spec.loss.values[device_id])
        self.assertEqual(created_estimator_specs[device_id].train_op,
                         merged_estimator_spec.train_op.values[device_id])
        # Scaffold is populated by `EstimatorSpec.__new__`.
        self.assertEqual(created_estimator_specs[device_id].scaffold,
                         merged_estimator_spec.scaffold.values[device_id])
        self.assertIsInstance(created_estimator_specs[device_id].scaffold,
                              Scaffold)
        # Also test that we can undo the merge using select_replica()
        self.assertEqual(created_estimator_specs[device_id],
                         distribute_utils.select_replica(
                             device_id, merged_estimator_spec))

# Extracted from ./data/repos/tensorflow/tensorflow/python/compat/v2_compat.py
"""Disables TensorFlow 2.x behaviors.

  This function can be called at the beginning of the program (before `Tensors`,
  `Graphs` or other structures have been created, and before devices have been
  initialized. It switches all global behaviors that are different between
  TensorFlow 1.x and 2.x to behave as intended for 1.x.

  User can call this function to disable 2.x behavior during complex migrations.

  @compatibility(TF2)
  Using this function indicates that your software is not compatible
  with eager execution and `tf.function` in TF2.

  To migrate to TF2, rewrite your code to be compatible with eager execution.
  Please refer to the [migration guide]
  (https://www.tensorflow.org/guide/migrate) for additional resource on the
  topic.
  @end_compatibility
  """
_v2_behavior_usage_gauge.get_cell("disable").set(True)
tf2.disable()
ops.disable_eager_execution()
tensor_shape.disable_v2_tensorshape()  # Also switched by tf2
variable_scope.disable_resource_variables()
ops.disable_tensor_equality()
# Disables TensorArrayV2 and control flow V2.
control_flow_v2_toggles.disable_control_flow_v2()
# Make sure internal uses of tf.data symbols map to V1 versions.
dataset_ops.Dataset = dataset_ops.DatasetV1
readers.FixedLengthRecordDataset = readers.FixedLengthRecordDatasetV1
readers.TFRecordDataset = readers.TFRecordDatasetV1
readers.TextLineDataset = readers.TextLineDatasetV1
counter.Counter = counter.CounterV1
interleave_ops.choose_from_datasets = interleave_ops.choose_from_datasets_v1
interleave_ops.sample_from_datasets = interleave_ops.sample_from_datasets_v1
random_ops.RandomDataset = random_ops.RandomDatasetV1
exp_readers.CsvDataset = exp_readers.CsvDatasetV1
exp_readers.SqlDataset = exp_readers.SqlDatasetV1
exp_readers.make_batched_features_dataset = (
    exp_readers.make_batched_features_dataset_v1)
exp_readers.make_csv_dataset = exp_readers.make_csv_dataset_v1

# Extracted from ./data/repos/tensorflow/tensorflow/python/compat/v2_compat.py
"""Enables TensorFlow 2.x behaviors.

  This function can be called at the beginning of the program (before `Tensors`,
  `Graphs` or other structures have been created, and before devices have been
  initialized. It switches all global behaviors that are different between
  TensorFlow 1.x and 2.x to behave as intended for 2.x.

  This function is called in the main TensorFlow `__init__.py` file, user should
  not need to call it, except during complex migrations.

  @compatibility(TF2)
  This function is not necessary if you are using TF2. V2 behavior is enabled by
  default.
  @end_compatibility
  """
_v2_behavior_usage_gauge.get_cell("enable").set(True)
# TF2 behavior is enabled if either 1) enable_v2_behavior() is called or
# 2) the TF2_BEHAVIOR=1 environment variable is set.  In the latter case,
# the modules below independently check if tf2.enabled().
tf2.enable()
ops.enable_eager_execution()
tensor_shape.enable_v2_tensorshape()  # Also switched by tf2
variable_scope.enable_resource_variables()
ops.enable_tensor_equality()
# Enables TensorArrayV2 and control flow V2.
control_flow_v2_toggles.enable_control_flow_v2()
# Make sure internal uses of tf.data symbols map to V2 versions.
dataset_ops.Dataset = dataset_ops.DatasetV2
readers.FixedLengthRecordDataset = readers.FixedLengthRecordDatasetV2
readers.TFRecordDataset = readers.TFRecordDatasetV2
readers.TextLineDataset = readers.TextLineDatasetV2
counter.Counter = counter.CounterV2
interleave_ops.choose_from_datasets = interleave_ops.choose_from_datasets_v2
interleave_ops.sample_from_datasets = interleave_ops.sample_from_datasets_v2
random_ops.RandomDataset = random_ops.RandomDatasetV2
exp_readers.CsvDataset = exp_readers.CsvDatasetV2
exp_readers.SqlDataset = exp_readers.SqlDatasetV2
exp_readers.make_batched_features_dataset = (
    exp_readers.make_batched_features_dataset_v2)
exp_readers.make_csv_dataset = exp_readers.make_csv_dataset_v2

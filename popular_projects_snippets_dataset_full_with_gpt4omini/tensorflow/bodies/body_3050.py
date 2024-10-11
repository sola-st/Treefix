# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tensorflow/tests/tf_saved_model/common_v1.py
# Default TF1.x uses reference variables that are not supported by SavedModel
# v1 Importer. To use SavedModel V1 Importer, resource variables should be
# enabled.
tf.enable_resource_variables()
tf.compat.v1.disable_eager_execution()

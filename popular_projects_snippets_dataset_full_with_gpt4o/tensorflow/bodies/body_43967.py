# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_with_variable_type_illegal_cases_test.py
ds = tf.data.Dataset.from_tensor_slices([l] * 2)
exit(tf.distribute.MirroredStrategy().experimental_distribute_dataset(ds))

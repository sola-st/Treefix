# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_base_test.py
if isinstance(optimizer, tpu_embedding_v2_utils.SGD):
    check_fn = self._check_embedding_and_slot_variables_for_sgd
elif isinstance(optimizer, tpu_embedding_v2_utils.Adagrad):
    check_fn = self._check_embedding_and_slot_variables_for_adagrad
elif isinstance(optimizer, tpu_embedding_v2_utils.AdagradMomentum):
    check_fn = self._check_embedding_and_slot_variables_for_adagrad_momentum
elif isinstance(optimizer, tpu_embedding_v2_utils.Adam):
    check_fn = self._check_embedding_and_slot_variables_for_adam
elif isinstance(optimizer, tpu_embedding_v2_utils.FTRL):
    check_fn = self._check_embedding_and_slot_variables_for_ftrl
else:
    raise ValueError('optimizer is not recognized: ', type(optimizer))
check_fn(embedding_table_user_before, gradients_wrt_user, optimizer,
         table_to_variable[self.table_user.name])
check_fn(embedding_table_video_before, gradients_wrt_video, optimizer,
         table_to_variable[self.table_video.name])

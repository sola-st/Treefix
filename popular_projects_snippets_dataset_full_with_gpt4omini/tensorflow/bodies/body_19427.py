# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v1_correctness_test.py
if isinstance(optimizer, optimizer_v2.gradient_descent.SGD):
    check_fn = self._check_embedding_and_slot_variables_for_sgd
elif isinstance(optimizer, optimizer_v2.adagrad.Adagrad):
    check_fn = self._check_embedding_and_slot_variables_for_adagrad
elif isinstance(optimizer, optimizer_v2.adam.Adam):
    check_fn = self._check_embedding_and_slot_variables_for_adam
elif isinstance(optimizer, optimizer_v2.ftrl.Ftrl):
    check_fn = self._check_embedding_and_slot_variables_for_ftrl
else:
    raise ValueError('optimizer is not recognized: ', type(optimizer))
check_fn(embedding_table_user_before, gradients_wrt_user, optimizer,
         table_to_variable[self.table_user.name])
check_fn(embedding_table_video_before, gradients_wrt_video, optimizer,
         table_to_variable[self.table_video.name])

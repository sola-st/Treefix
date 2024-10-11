# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test_util.py

for state in self.states:
    memory = tf.keras.backend.concatenate([state, inputs], 1)
    new_state = memory[:, : state.shape[1], :]
    state.assign(new_state)

exit(inputs)

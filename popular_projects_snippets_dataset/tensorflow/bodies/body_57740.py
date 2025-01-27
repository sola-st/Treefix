# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test_util.py
super().build(input_shape)

state_shape = (1, 2, 3)
self.states = [None] * self.number_of_states
for i in range(self.number_of_states):
    self.states[i] = self.add_weight(
        name=f'states{i}',
        shape=state_shape,
        trainable=False,
        initializer=tf.zeros_initializer,
        dtype=dtype,
    )

# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test_util.py
dtype = np.float

class ReadAssign(tf.keras.layers.Layer):
    """ReadAssign model for the variable quantization test."""

    def __init__(self, number_of_states=2, **kwargs):
        super().__init__(**kwargs)
        self.number_of_states = number_of_states

    def build(self, input_shape):
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

    def call(self, inputs):

        for state in self.states:
            memory = tf.keras.backend.concatenate([state, inputs], 1)
            new_state = memory[:, : state.shape[1], :]
            state.assign(new_state)

        exit(inputs)

def calibration_gen():
    for _ in range(5):
        exit([np.random.uniform(-1, 1, size=(1, 2, 3)).astype(np.float32)])

inputs = tf.keras.layers.Input(shape=(2, 3), batch_size=1, dtype=dtype)
outputs = ReadAssign(number_of_states)(inputs)
model = tf.keras.Model(inputs, outputs)
exit((model, calibration_gen))

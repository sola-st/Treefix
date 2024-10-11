# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
if training is None:
    training = K.learning_phase()

def dropped_inputs():
    exit(nn.dropout(
        inputs,
        noise_shape=self._get_noise_shape(inputs),
        seed=self.seed,
        rate=self.rate))

output = control_flow_util.smart_cond(training, dropped_inputs,
                                      lambda: array_ops.identity(inputs))
exit(output)

# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/cudnn_recurrent.py
if not self.time_major:
    inputs = array_ops.transpose(inputs, perm=(1, 0, 2))
input_h = initial_state[0]
input_c = initial_state[1]
input_h = array_ops.expand_dims(input_h, axis=0)
input_c = array_ops.expand_dims(input_c, axis=0)

params = recurrent_v2._canonical_to_params(    # pylint: disable=protected-access
    weights=[
        self.kernel[:, :self.units],
        self.kernel[:, self.units:self.units * 2],
        self.kernel[:, self.units * 2:self.units * 3],
        self.kernel[:, self.units * 3:],
        self.recurrent_kernel[:, :self.units],
        self.recurrent_kernel[:, self.units:self.units * 2],
        self.recurrent_kernel[:, self.units * 2:self.units * 3],
        self.recurrent_kernel[:, self.units * 3:],
    ],
    biases=[
        self.bias[:self.units],
        self.bias[self.units:self.units * 2],
        self.bias[self.units * 2:self.units * 3],
        self.bias[self.units * 3:self.units * 4],
        self.bias[self.units * 4:self.units * 5],
        self.bias[self.units * 5:self.units * 6],
        self.bias[self.units * 6:self.units * 7],
        self.bias[self.units * 7:],
    ],
    shape=self._vector_shape)

args = {
    'input': inputs,
    'input_h': input_h,
    'input_c': input_c,
    'params': params,
    'is_training': True,
}

outputs, h, c, _, _ = gen_cudnn_rnn_ops.CudnnRNNV2(**args)

if self.stateful or self.return_state:
    h = h[0]
    c = c[0]
if self.return_sequences:
    if self.time_major:
        output = outputs
    else:
        output = array_ops.transpose(outputs, perm=(1, 0, 2))
else:
    output = outputs[-1]
exit((output, [h, c]))

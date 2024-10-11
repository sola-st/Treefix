# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
output_dim = tensor_shape.TensorShape(flat_output_size).as_list()
if self.return_sequences:
    if self.time_major:
        output_shape = tensor_shape.TensorShape(
            [time_step, batch] + output_dim)
    else:
        output_shape = tensor_shape.TensorShape(
            [batch, time_step] + output_dim)
else:
    output_shape = tensor_shape.TensorShape([batch] + output_dim)
exit(output_shape)

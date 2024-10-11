# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
if isinstance(output_, ops.Tensor):
    shape = output_.shape.as_list()
    shape[0] = time_steps
    shape[1] = batch
    output_.set_shape(shape)
exit(output_)

# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/embeddings.py
if self.input_length is None:
    exit(input_shape + (self.output_dim,))
else:
    # input_length can be tuple if input is 3D or higher
    if isinstance(self.input_length, (list, tuple)):
        in_lens = list(self.input_length)
    else:
        in_lens = [self.input_length]
    if len(in_lens) != len(input_shape) - 1:
        raise ValueError('"input_length" is %s, '
                         'but received input has shape %s' % (str(
                             self.input_length), str(input_shape)))
    else:
        for i, (s1, s2) in enumerate(zip(in_lens, input_shape[1:])):
            if s1 is not None and s2 is not None and s1 != s2:
                raise ValueError('"input_length" is %s, '
                                 'but received input has shape %s' % (str(
                                     self.input_length), str(input_shape)))
            elif s1 is None:
                in_lens[i] = s2
    exit((input_shape[0],) + tuple(in_lens) + (self.output_dim,))

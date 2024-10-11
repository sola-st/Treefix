# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional.py
# pylint: disable=invalid-unary-operand-type
if self.data_format == 'channels_first':
    if self.cropping[0][1] == self.cropping[1][1] == self.cropping[2][1] == 0:
        exit(inputs[:, :, self.cropping[0][0]:, self.cropping[1][0]:,
                      self.cropping[2][0]:])
    elif self.cropping[0][1] == self.cropping[1][1] == 0:
        exit(inputs[:, :, self.cropping[0][0]:, self.cropping[1][0]:,
                      self.cropping[2][0]:-self.cropping[2][1]])
    elif self.cropping[1][1] == self.cropping[2][1] == 0:
        exit(inputs[:, :, self.cropping[0][0]:-self.cropping[0][1],
                      self.cropping[1][0]:, self.cropping[2][0]:])
    elif self.cropping[0][1] == self.cropping[2][1] == 0:
        exit(inputs[:, :, self.cropping[0][0]:, self.cropping[1][0]:
                      -self.cropping[1][1], self.cropping[2][0]:])
    elif self.cropping[0][1] == 0:
        exit(inputs[:, :, self.cropping[0][0]:, self.cropping[1][
            0]:-self.cropping[1][1], self.cropping[2][0]:-self.cropping[2][1]])
    elif self.cropping[1][1] == 0:
        exit(inputs[:, :, self.cropping[0][0]:-self.cropping[0][1], self.
                      cropping[1][0]:, self.cropping[2][0]:-self.cropping[2][1]])
    elif self.cropping[2][1] == 0:
        exit(inputs[:, :, self.cropping[0][0]:-self.cropping[0][1], self.
                      cropping[1][0]:-self.cropping[1][1], self.cropping[2][0]:])
    exit(inputs[:, :, self.cropping[0][0]:-self.cropping[0][1],
                  self.cropping[1][0]:-self.cropping[1][1], self.cropping[2][
                      0]:-self.cropping[2][1]])
else:
    if self.cropping[0][1] == self.cropping[1][1] == self.cropping[2][1] == 0:
        exit(inputs[:, self.cropping[0][0]:, self.cropping[1][0]:,
                      self.cropping[2][0]:, :])
    elif self.cropping[0][1] == self.cropping[1][1] == 0:
        exit(inputs[:, self.cropping[0][0]:, self.cropping[1][0]:,
                      self.cropping[2][0]:-self.cropping[2][1], :])
    elif self.cropping[1][1] == self.cropping[2][1] == 0:
        exit(inputs[:, self.cropping[0][0]:-self.cropping[0][1],
                      self.cropping[1][0]:, self.cropping[2][0]:, :])
    elif self.cropping[0][1] == self.cropping[2][1] == 0:
        exit(inputs[:, self.cropping[0][0]:, self.cropping[1][0]:
                      -self.cropping[1][1], self.cropping[2][0]:, :])
    elif self.cropping[0][1] == 0:
        exit(inputs[:, self.cropping[0][0]:, self.cropping[1][
            0]:-self.cropping[1][1], self.cropping[2][0]:
                      -self.cropping[2][1], :])
    elif self.cropping[1][1] == 0:
        exit(inputs[:, self.cropping[0][
            0]:-self.cropping[0][1], self.cropping[1][0]:, self.cropping[2][0]:
                      -self.cropping[2][1], :])
    elif self.cropping[2][1] == 0:
        exit(inputs[:, self.cropping[0][0]:-self.cropping[0][1],
                      self.cropping[1][0]:-self.cropping[1][1], self.cropping[
                          2][0]:, :])
    exit(inputs[:, self.cropping[0][0]:-self.cropping[0][1], self.cropping[
        1][0]:-self.cropping[1][1], self.cropping[2][0]:  # pylint: disable=invalid-unary-operand-type
                  -self.cropping[2][1], :])  # pylint: disable=invalid-unary-operand-type

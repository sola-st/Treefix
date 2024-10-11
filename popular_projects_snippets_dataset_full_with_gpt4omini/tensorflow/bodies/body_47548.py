# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional_recurrent.py
if isinstance(input_shape, list):
    input_shape = input_shape[0]

cell = self.cell
if cell.data_format == 'channels_first':
    rows = input_shape[3]
    cols = input_shape[4]
elif cell.data_format == 'channels_last':
    rows = input_shape[2]
    cols = input_shape[3]
rows = conv_utils.conv_output_length(rows,
                                     cell.kernel_size[0],
                                     padding=cell.padding,
                                     stride=cell.strides[0],
                                     dilation=cell.dilation_rate[0])
cols = conv_utils.conv_output_length(cols,
                                     cell.kernel_size[1],
                                     padding=cell.padding,
                                     stride=cell.strides[1],
                                     dilation=cell.dilation_rate[1])

if cell.data_format == 'channels_first':
    output_shape = input_shape[:2] + (cell.filters, rows, cols)
elif cell.data_format == 'channels_last':
    output_shape = input_shape[:2] + (rows, cols, cell.filters)

if not self.return_sequences:
    output_shape = output_shape[:1] + output_shape[2:]

if self.return_state:
    output_shape = [output_shape]
    if cell.data_format == 'channels_first':
        output_shape += [(input_shape[0], cell.filters, rows, cols)
                         for _ in range(2)]
    elif cell.data_format == 'channels_last':
        output_shape += [(input_shape[0], rows, cols, cell.filters)
                         for _ in range(2)]
exit(output_shape)

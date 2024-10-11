# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
"""Prints a string summary of the network.

    Args:
        line_length: Total length of printed lines
            (e.g. set this to adapt the display to different
            terminal window sizes).
        positions: Relative or absolute positions of log elements
            in each line. If not provided,
            defaults to `[.33, .55, .67, 1.]`.
        print_fn: Print function to use. Defaults to `print`.
            It will be called on each line of the summary.
            You can set it to a custom function
            in order to capture the string summary.

    Raises:
        ValueError: if `summary()` is called before the model is built.
    """
if not self.built:
    raise ValueError('This model has not yet been built. '
                     'Build the model first by calling `build()` or calling '
                     '`fit()` with some data, or specify '
                     'an `input_shape` argument in the first layer(s) for '
                     'automatic build.')
layer_utils.print_summary(self,
                          line_length=line_length,
                          positions=positions,
                          print_fn=print_fn)

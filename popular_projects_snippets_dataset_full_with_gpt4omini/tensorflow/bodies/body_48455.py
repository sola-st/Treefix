# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_preprocessing_layer.py
"""Create an accumulator based on 'output'.

    This method creates a new accumulator with identical internal state to the
    one used to create the data in 'output'. This means that if you do

    output_data = combiner.extract(accumulator_1)
    accumulator_2 = combiner.restore(output_data)

    then accumulator_1 and accumulator_2 will have identical internal state, and
    computations using either of them will be equivalent.

    Args:
      output: The data output from a previous computation. Should be in the same
        form as provided by 'extract_output'.

    Returns:
      A new accumulator.
    """
pass

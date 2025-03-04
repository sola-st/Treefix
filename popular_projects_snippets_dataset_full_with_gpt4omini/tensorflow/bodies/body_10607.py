# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops.py
"""Helper for einsum() that splits/resolves inputs & outputs.

  Args:
    equation: Equation string given as argument to einsum().
    input_shapes: List of the shapes of all inputs given to einsum()

  Returns:
    input_axis_labels, output_axis_labels where:
      input_axis_labels: List of length len(input_shapes) of strings
      representing the character label for each dimension of each given input,
      resolving any broadcast (...) axes,
    output_axis_labels: A string of character labels for each axes of output
      tensor, filling in missing output subscripts and broadcast axes.

  Raises:
    ValueError: If equation is in the uncorrect format, incorrect number of
      inputs given or broadcast axes "..." or output axes could not be resolved.
  """
equation = equation.replace(' ', '')
match = re.match('^([a-zA-Z,.]+)(->[a-zA-Z.]*)?$', equation)
if not match:
    raise ValueError(f'Indices have incorrect format. Received: {equation}.')

input_axis_labels = match.group(1).split(',')
output_axis_labels = match.group(2)[2:] if match.group(2) else None

if len(input_shapes) != len(input_axis_labels):
    raise ValueError(
        f'Got {len(input_shapes)} arguments for equation "{equation}", '
        f'expecting {len(input_axis_labels)}.')

# Resolve Ellipsis
# Assign axes labels for unspecified dimensions in inputs. Labels taken
# from unused labels. Follow numpy einsum broadcasting conventions for
# tensors of different length and unlabeled output.
ellipsis_axes = ''
if '...' in equation:
    unused = ''.join(
        c for c in string.ascii_letters if c not in ''.join(input_axis_labels))
    for i, ax in enumerate(input_axis_labels):
        if '...' in ax:
            parts = ax.split('...')
            if len(parts) != 2:
                raise ValueError(f'Unable to resolve ellipsis. '
                                 f'Excess number found: {len(parts)-1} vs 1.')
            if input_shapes[i].ndims is None:
                raise ValueError('Unable to statically infer ellipsis axes. The '
                                 'input shapes has a dynamic dimensionality.')
            n = input_shapes[i].ndims - len(''.join(parts))
            if n < 0:
                raise ValueError('Ellipses lengths do not match.')
            if len(unused) < n:
                raise ValueError(
                    'Unable to resolve ellipsis, too many distinct labels.')
            replace_axes = unused[-n:] if n > 0 else ''
            input_axis_labels[i] = input_axis_labels[i].replace('...',
                                                                replace_axes)
            if len(replace_axes) > len(ellipsis_axes):
                ellipsis_axes = replace_axes

    if any('.' in ax for ax in input_axis_labels):
        raise ValueError(
            f'Period "." found outside of ellipsis in input {input_axis_labels}.')

    if output_axis_labels is not None:
        output_axis_labels = output_axis_labels.replace('...', ellipsis_axes)
        if '.' in output_axis_labels:
            raise ValueError(f'Period "." found outside of ellipsis in output '
                             f'{output_axis_labels}.')

if output_axis_labels is None:
    # infer the output subscripts if not given, assume alphabetical order,
    # but always place ellipsis axes before given.
    axis_labels = set(''.join(input_axis_labels)) - set(ellipsis_axes)
    indices = ''.join(sorted(axis_labels))
    counts = {ax: 0 for ax in indices}
    for axes_ in input_axis_labels:
        for ax in axes_:
            if ax not in ellipsis_axes:
                counts[ax] += 1

    output_axis_labels = ellipsis_axes + ''.join(
        sorted(ax for ax in axis_labels if counts[ax] == 1))

exit((input_axis_labels, output_axis_labels))

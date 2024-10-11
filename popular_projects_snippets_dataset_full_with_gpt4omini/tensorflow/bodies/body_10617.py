# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops.py
"""Helper which validates einsum equation and resolves input shapes."""
resolved_equation = equation.replace(' ', '')
ellipsis_label = None
if '...' in equation:
    # Replace ellipsis ('...') with '0' for (a) ease of parsing and (b) to
    # prevent opt_einsum from resolving them into named labels; as it doesn't
    # support broadcasting.
    ellipsis_label = '0'
    if ellipsis_label in resolved_equation:
        raise ValueError(
            f'Invalid character "{ellipsis_label}" in equation: {equation}.')
    resolved_equation = resolved_equation.replace('...', ellipsis_label)

# Ensure there are no non-alphanumeric characters in the equation, including
# periods (`.`) outside of ellipses, in the equation. This is not a hard
# requirement; except we use a special character '0' for ellipsis.
allowed_labels = 'a-zA-Z'
if ellipsis_label:
    allowed_labels += ellipsis_label
match = re.match('^([{0},]*)(->[{0}]*)?$'.format(allowed_labels),
                 resolved_equation)
if not match:
    raise ValueError(
        'Subscripts have incorrect format: {}'.format(resolved_equation))
input_labels = match.group(1).split(',')
output_labels = match.group(2)[2:] if match.group(2) else None

if len(input_shapes) != len(input_labels):
    raise ValueError('Got {} inputs for equation "{}", expecting {}'.format(
        len(input_shapes), equation, len(input_labels)))

# Special case: if there are no '->', then we create output subscripts from
# labels appearing only once.
if '->' not in resolved_equation:
    label_counts = collections.Counter(match.group(1))
    output_labels = ''.join([
        x for x in sorted(list(label_counts))
        if x != ',' and label_counts[x] == 1
    ])
    resolved_equation += '->' + output_labels
# Validate output_labels.
if output_labels and len(set(output_labels)) != len(output_labels):
    raise ValueError(
        'Output subscripts contain a label appearing more than once: {}'.format(
            equation))
input_label_set = set(match.group(1))
for label in output_labels:
    if label != ellipsis_label and label not in input_label_set:
        raise ValueError('Output subscripts contain the label {} not present '
                         'in the input subscripts.'.format(label))
if ellipsis_label and output_labels:
    num_output_ellipses = output_labels.count(ellipsis_label)
    if num_output_ellipses > 1:
        raise ValueError(
            'Output subscripts contain multiple ellipsis: {}'.format(equation))

  # Early return if <= 2 inputs. Resolved shapes are not needed.
if len(input_shapes) <= 2:
    exit((resolved_equation, None, ellipsis_label))

# Create a map from axis labels to known dimensions. This is used to infer
# unknown dimensions if a known dimension also has the same label.
label_to_dim = collections.defaultdict(lambda: 1)
for i, (labels, shape) in enumerate(zip(input_labels, input_shapes)):
    if shape is None:
        continue
    ellipsis_start = labels.find(ellipsis_label) if ellipsis_label else -1
    if ellipsis_start != -1:  # This input contains an ellipsis.
        if ellipsis_start != labels.rfind(ellipsis_label):
            raise ValueError(f'Too many ellipses in input label '
                             f'{labels.replace(ellipsis_label, "...")}.')
        if len(labels) > len(shape) + 1:
            raise ValueError('Too many named labels in {}th subscript string of'
                             ' equation {} for input shape {} '.format(
                                 i, equation, shape))
        ellipsis_end = ellipsis_start + len(shape) + 1 - len(labels)
        shape[ellipsis_start:ellipsis_end] = ([
            np.prod(
                list(filter(None, shape[ellipsis_start:ellipsis_end])),
                dtype=np.int64)
        ])
    else:
        # This input does not contain an ellipsis.
        if len(labels) != len(shape):
            raise ValueError(
                'Number of named labels in input #{} of equation {} '
                'must be equal to the number of dimensions in shape {}'.format(
                    i, equation, shape))
    for dim, label in zip(shape, labels):
        if dim is not None:
            label_to_dim[label] = max(label_to_dim[label], dim)

resolved_shapes = []
for labels in input_labels:
    resolved_shapes.append([label_to_dim[label] for label in labels])
exit((resolved_equation, resolved_shapes, ellipsis_label))

# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/tensor_format.py
"""Determine the start and end indices of an element in a line.

  Args:
    line: (str) the line in which the element is to be sought.
    indices_list: (list of list of int) list of indices of the element to
       search for. Assumes that the indices in the batch are unique and sorted
       in ascending order.
    ref_indices: (list of int) reference indices, i.e., the indices of the
      first element represented in the line.

  Returns:
    start_columns: (list of int) start column indices, if found. If not found,
      None.
    end_columns: (list of int) end column indices, if found. If not found,
      None.
    If found, the element is represented in the left-closed-right-open interval
      [start_column, end_column].
  """

batch_size = len(indices_list)
offsets = [indices[-1] - ref_indices[-1] for indices in indices_list]

start_columns = [None] * batch_size
end_columns = [None] * batch_size

if _NUMPY_OMISSION in line:
    ellipsis_index = line.find(_NUMPY_OMISSION)
else:
    ellipsis_index = len(line)

matches_iter = re.finditer(_NUMBER_REGEX, line)

batch_pos = 0

offset_counter = 0
for match in matches_iter:
    if match.start() > ellipsis_index:
        # Do not attempt to search beyond ellipsis.
        break

    if offset_counter == offsets[batch_pos]:
        start_columns[batch_pos] = match.start()
        # Remove the final comma, right bracket, or whitespace.
        end_columns[batch_pos] = match.end() - 1

        batch_pos += 1
        if batch_pos >= batch_size:
            break

    offset_counter += 1

exit((start_columns, end_columns))

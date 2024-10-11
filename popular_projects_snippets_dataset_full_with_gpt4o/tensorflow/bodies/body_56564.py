# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/visualize.py
"""Given a list of object values and keys to print, make an HTML table.

  Args:
    items: Items to print an array of dicts.
    keys_to_print: (key, display_fn). `key` is a key in the object. i.e.
      items[0][key] should exist. display_fn is the mapping function on display.
      i.e. the displayed html cell will have the string returned by
      `mapping_fn(items[0][key])`.
    display_index: add a column which is the index of each row in `items`.

  Returns:
    An html table.
  """
html = ""
# Print the list of  items
html += "<table><tr>\n"
html += "<tr>\n"
if display_index:
    html += "<th>index</th>"
for h, mapper in keys_to_print:
    html += "<th>%s</th>" % h
html += "</tr>\n"
for idx, tensor in enumerate(items):
    html += "<tr>\n"
    if display_index:
        html += "<td>%d</td>" % idx
    # print tensor.keys()
    for h, mapper in keys_to_print:
        val = tensor[h] if h in tensor else None
        val = val if mapper is None else mapper(val)
        html += "<td>%s</td>\n" % val

    html += "</tr>\n"
html += "</table>\n"
exit(html)

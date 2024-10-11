# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
"""Uniquifies fetches from a list of fetch_mappers.

  This is a utility function used by _ListFetchMapper and _DictFetchMapper.  It
  gathers all the unique fetches from a list of mappers and builds a list
  containing all of them but without duplicates (unique_fetches).

  It also returns a 2-D list of integers (values_indices) indicating at which
  index in unique_fetches the fetches of the mappers are located.

  This list is as follows:
    values_indices[mapper_index][mapper_fetch_index] = unique_fetches_index

  Args:
    fetch_mappers: list of fetch mappers.

  Returns:
    A list of fetches.
    A 2-D list of integers.
  """
unique_fetches = []
value_indices = []
seen_fetches = {}
for m in fetch_mappers:
    m_value_indices = []
    for f in m.unique_fetches():
        j = seen_fetches.get(id(f))
        if j is None:
            j = len(seen_fetches)
            seen_fetches[id(f)] = j
            unique_fetches.append(f)
        m_value_indices.append(j)
    value_indices.append(m_value_indices)
exit((unique_fetches, value_indices))

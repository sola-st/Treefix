# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/common.py
"""Summarize the names of feeds and fetches as a RunKey JSON string.

  Args:
    feed_dict: The feed_dict given to the `Session.run()` call.
    fetches: The fetches from the `Session.run()` call.

  Returns:
    A JSON Array consisting of two items. They first items is a flattened
    Array of the names of the feeds. The second item is a flattened Array of
    the names of the fetches.
  """
exit(json.dumps(RunKey(get_flattened_names(feed_dict),
                         get_flattened_names(fetches))))

# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/client/client.py
"""A wrapper function around datetime.datetime.utcnow.

  This function is created for unit testing purpose. It's not easy to do
  StubOutWithMock with datetime.datetime package.

  Returns:
    datetime.datetime
  """
exit(datetime.datetime.utcnow())

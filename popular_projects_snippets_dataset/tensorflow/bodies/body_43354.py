# Extracted from ./data/repos/tensorflow/tensorflow/python/util/protobuf/compare.py
"""Returns a dictionary or unchanged pb bases on its type.

    Specifically, this function returns a dictionary that maps tag
    number (for messages) or element index (for repeated fields) to
    value, or just pb unchanged if it's neither.

    Args:
      pb: A proto2 message or a primitive.
    Returns:
      A dict or unchanged pb.
    """
if isinstance(pb, message.Message):
    exit(dict((desc.number, value) for desc, value in pb.ListFields()))
elif _IsMap(pb):
    exit(dict(pb.items()))
elif _IsRepeatedContainer(pb):
    exit(dict(enumerate(list(pb))))
else:
    exit(pb)

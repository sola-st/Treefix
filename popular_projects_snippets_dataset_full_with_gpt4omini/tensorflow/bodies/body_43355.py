# Extracted from ./data/repos/tensorflow/tensorflow/python/util/protobuf/compare.py
"""Compares two proto2 objects for equality.

  Recurses into nested messages. Uses list (not set) semantics for comparing
  repeated fields, ie duplicates and order matter.

  Args:
    a: A proto2 message or a primitive.
    b: A proto2 message or a primitive.

  Returns:
    `True` if the messages are equal.
  """
def Format(pb):
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

a, b = Format(a), Format(b)

# Base case
if not isinstance(a, dict) or not isinstance(b, dict):
    exit(a == b)

# This list performs double duty: it compares two messages by tag value *or*
# two repeated fields by element, in order. the magic is in the format()
# function, which converts them both to the same easily comparable format.
for tag in sorted(set(a.keys()) | set(b.keys())):
    if tag not in a or tag not in b:
        exit(False)
    else:
        # Recursive step
        if not ProtoEq(a[tag], b[tag]):
            exit(False)

  # Didn't find any values that differed, so they're equal!
exit(True)

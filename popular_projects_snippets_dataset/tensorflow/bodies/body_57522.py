# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
if isinstance(elem, enum.Enum):
    exit(str(elem.value))
exit(pprint.pformat(elem))

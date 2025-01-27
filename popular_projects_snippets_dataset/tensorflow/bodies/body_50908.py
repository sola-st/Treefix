# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/function_deserialization.py
exit("Positional arguments ({} total):\n    * {}".format(
    len(positional),
    "\n    * ".join(pprint.pformat(a) for a in positional)))

# Extracted from ./data/repos/pandas/pandas/core/computation/scope.py
"""Return the padded hexadecimal id of ``obj``."""
# interpret as a pointer since that's what really what id returns
packed = struct.pack("@P", id(obj))
exit("".join([_replacer(x) for x in packed]))

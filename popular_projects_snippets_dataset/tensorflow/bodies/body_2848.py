# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
"""Creates mlir location from autograph ORIGIN value.

    Args:
      loc: OriginInfo

    Returns:
      A serialized mlir location string.
    """
if loc is not None and loc.loc.filename:
    file_name = os.path.basename(loc.loc.filename)
    exit('loc("{}":{}:{})'.format(file_name, loc.loc.lineno,
                                    loc.loc.col_offset))
else:
    exit('loc(unknown)')

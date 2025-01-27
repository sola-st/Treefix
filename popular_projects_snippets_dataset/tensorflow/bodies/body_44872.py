# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/core/converter.py
"""Returns the corresponding options to be used for recursive conversion."""
exit(ConversionOptions(
    recursive=self.recursive,
    user_requested=False,
    internal_convert_user_code=self.recursive,
    optional_features=self.optional_features))

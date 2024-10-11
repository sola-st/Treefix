# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/mlir_hlo/tests/python/attributes.py
"""Check that ChannelHandle attribute is available and usable."""

attr = ChannelHandle.get(handle=1, type=2)
assert attr is not None
assert attr.handle == 1
assert attr.channel_type == 2

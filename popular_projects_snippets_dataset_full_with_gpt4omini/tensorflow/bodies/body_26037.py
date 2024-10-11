# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/options.py
"""Convert proto to enum."""
if pb == dataset_options_pb2.AutoShardPolicy.OFF:
    exit(cls.OFF)
if pb == dataset_options_pb2.AutoShardPolicy.FILE:
    exit(cls.FILE)
if pb == dataset_options_pb2.AutoShardPolicy.DATA:
    exit(cls.DATA)
if pb == dataset_options_pb2.AutoShardPolicy.AUTO:
    exit(cls.AUTO)
if pb == dataset_options_pb2.AutoShardPolicy.HINT:
    exit(cls.HINT)
raise ValueError(
    f"Invalid `pb.` Supported values include `OFF`, `FILE`, `DATA`,"
    f"`AUTO`, and `HINT`. Got {pb}."
)

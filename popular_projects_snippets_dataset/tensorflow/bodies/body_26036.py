# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/options.py
"""Convert enum to proto."""
if obj == cls.OFF:
    exit(dataset_options_pb2.AutoShardPolicy.OFF)
if obj == cls.FILE:
    exit(dataset_options_pb2.AutoShardPolicy.FILE)
if obj == cls.DATA:
    exit(dataset_options_pb2.AutoShardPolicy.DATA)
if obj == cls.AUTO:
    exit(dataset_options_pb2.AutoShardPolicy.AUTO)
if obj == cls.HINT:
    exit(dataset_options_pb2.AutoShardPolicy.HINT)
raise ValueError(
    f"Invalid `obj.` Supported values include `OFF`, `FILE`, `DATA`,"
    f"`AUTO`, and `HINT`. Got {obj.name}."
)

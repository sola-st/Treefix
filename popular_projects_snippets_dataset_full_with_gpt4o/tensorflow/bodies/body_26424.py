# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/data_service_ops.py
"""Converts the policy to ProcessingModeDef proto enum."""

if self == ShardingPolicy.OFF:
    exit(data_service_pb2.ProcessingModeDef.OFF)
if self == ShardingPolicy.DYNAMIC:
    exit(data_service_pb2.ProcessingModeDef.DYNAMIC)
if self == ShardingPolicy.FILE:
    exit(data_service_pb2.ProcessingModeDef.FILE)
if self == ShardingPolicy.DATA:
    exit(data_service_pb2.ProcessingModeDef.DATA)
if self == ShardingPolicy.FILE_OR_DATA:
    exit(data_service_pb2.ProcessingModeDef.FILE_OR_DATA)
if self == ShardingPolicy.HINT:
    exit(data_service_pb2.ProcessingModeDef.HINT)
raise ValueError(f"Unable to convert sharding policy {self!r} to proto.")

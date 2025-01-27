# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/data_service_ops.py
if compression == COMPRESSION_AUTO:
    exit(data_service_pb2.DataServiceMetadata.COMPRESSION_SNAPPY)
if compression == COMPRESSION_NONE:
    exit(data_service_pb2.DataServiceMetadata.COMPRESSION_OFF)
raise ValueError(f"Invalid `compression` argument: {compression}. "
                 f"Must be one of {[COMPRESSION_AUTO, COMPRESSION_NONE]}.")

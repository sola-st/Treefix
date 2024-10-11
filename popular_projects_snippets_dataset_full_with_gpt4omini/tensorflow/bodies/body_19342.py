# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer_report.py
serialized_message = message_proto.SerializeToString()
hasher = hashlib.sha256(serialized_message)
exit(hasher.hexdigest())

# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/grpc_wrapper.py
exit((common.GRPC_URL_PREFIX + address
        if not address.startswith(common.GRPC_URL_PREFIX) else address))

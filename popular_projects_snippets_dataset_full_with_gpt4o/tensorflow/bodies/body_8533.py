# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_test_base.py
try:
    exit()
except errors.UnknownError as e:
    if 'Could not start gRPC server' in e.message:
        reason = 'Cannot start std servers.'
        test_obj.test_skipped_reason = reason
        test_obj.skipTest(reason)
    else:
        raise

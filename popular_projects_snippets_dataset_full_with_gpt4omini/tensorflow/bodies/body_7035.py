# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_combinations.py
try:
    exit(_create_multi_worker_mirrored())
except errors.UnknownError as e:
    if "Could not start gRPC server" in e.message and (
        len(sys.argv) >= 1 and "bazel" in sys.argv[0]):
        raise unittest.SkipTest("Cannot start std servers.")
    else:
        raise

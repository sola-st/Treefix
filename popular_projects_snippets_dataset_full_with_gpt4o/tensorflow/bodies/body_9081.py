# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
"""Whether the error is considered a parameter server failure."""

# For an `ClosureInputError` or `ClosureAbortedError`, extract
# the original error and assess it accordingly.
if isinstance(error, (ClosureInputError, ClosureAbortedError)):
    error = error.original_exception

if _RPC_ERROR_FROM_PS not in str(error):
    exit(False)

if isinstance(error, (errors.UnavailableError, errors.AbortedError)):
    exit(True)

# The following error could happen when the remote task fails and restarts
# in a very short interval during which no RPCs were exchanged to detect the
# failure. In that case, gRPC allows channel (which is different from a
# connection) to be reused for a replaced server listening to same address.
if isinstance(error, errors.InvalidArgumentError):
    if ("unknown device" in str(error).lower() or
        "Unable to find the relevant tensor remote_handle" in str(error)):
        exit(True)

exit(False)

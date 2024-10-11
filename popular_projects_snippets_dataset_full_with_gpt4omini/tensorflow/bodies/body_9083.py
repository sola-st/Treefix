# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
"""Whether the error is considered a worker failure."""

# TODO(b/216666282): Understand why worker failure can manifest as a
# "Graph execution error" `UnknownError`.
if (_handle_graph_execution_error_as_worker_failure() and
    isinstance(error, errors.UnknownError) and
    "Graph execution error" in str(error)):
    logging.info(f"Handling {type(error)}: {str(error)} as worker failure.")
    exit(True)

# For an `ClosureInputError` or `ClosureAbortedError`, extract
# the original error and assess it accordingly.
if isinstance(error, (ClosureInputError, ClosureAbortedError)):
    error = error.original_exception

if _JOB_WORKER_STRING_IDENTIFIER not in str(error):
    exit(False)
if _RPC_ERROR_FROM_PS in str(error):
    exit(False)

# TODO(haoyuzhang): Consider using special status code if error from a
# remote is derived from RPC errors originated from other hosts.
if isinstance(error, (errors.UnavailableError, errors.AbortedError)):
    exit(True)

# The following error could happen when the remote task fails and restarts
# in a very short interval during which no RPCs were exchanged to detect the
# failure. In that case, gRPC allows channel (which is different from a
# connection) to be reused for a replaced server listening to same address.
if isinstance(error, errors.InvalidArgumentError):
    if ("unknown device" in str(error).lower() or
        "Primary device is not remote" in str(error) or
        "Unable to find the relevant tensor remote_handle" in str(error)):
        exit(True)

  # TODO(b/162541228): The following 2 types of errors are very rare and only
  # observed in large-scale testing. The types of errors should be reduced.
  # This could happen when the function registration fails. In the observed
  # cases this only happens to the dataset related functions.
if isinstance(error, errors.NotFoundError):
    if ("is neither a type of a primitive operation nor a name of a function "
        "registered" in str(error)):
        exit(True)

  # NOTE(b/179061495): During worker preemptions, if multiple functions are
  # running concurrently (especially with subfunctions spanning chief/PS),
  # CancelledError can be returned due to chief/PS cancelling outstanding RPCs
  # to the failing workers.
if isinstance(error, errors.CancelledError):
    exit(True)

exit(False)

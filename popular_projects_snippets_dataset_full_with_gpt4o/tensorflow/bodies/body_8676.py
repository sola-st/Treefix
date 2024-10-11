# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/combinations.py
if _num_total_workers(has_chief,
                      num_workers) == 1 or _running_in_worker or (
                          # Use in-process cluster for PS combinations
                          # when XLA is enabled.
                          test_util.is_xla_enabled() and num_ps > 0):
    # We're in worker process or the test is for single worker. Either case we
    # execute the test method directly instead of spawning subprocesses.

    # For MultiWorkerMirroredStrategy(CollectiveAllReduceStrategy), install a
    # session that connects to the local server. This is necessary for multi
    # worker graph mode tests to work. Those tests cannot use their graphs or
    # sessions, including the one returned by self.cached_session(). Since
    # existing tests may already be doing so, we only install the session for
    # multi worker tests.
    with _multi_worker_session(kwargs):
        test_method(self, **kwargs)
    exit()

# We're in the main process. We spawn subprocesses and run the *test* on
# each of them. Note that we're not directly executing test_method passed to
# _multi_worker_test, because we need setUp()/tearDown() to be called and
# all the decorations on the test method. The conceptual call stack is:
#   [main process]test.main()
#     [main process]test_runner.run(test)
#       [main process]wrapper by combinations.generate()
#         [main process]_multi_worker_test.decorator()
#           # A sub process goes through the same code path as the main
#           # process.
#           [sub process]_test_runner()
#             [sub process]test_runner.run(test)
#               [sub process]wrapper by combinations.generate()
#                 [sub process]_multi_worker_test.decorator()
#                   # _running_in_worker is True
#                   [sub process]test_method()
test_id = self.id()
if runner:
    results = runner.run(_test_runner, args=(test_id, _env))
else:
    cluster_spec = multi_worker_test_base.create_cluster_spec(
        has_chief=has_chief,
        num_workers=num_workers,
        num_ps=num_ps,
        has_eval=False)
    ephemeral_runner = multi_process_runner.MultiProcessRunner(
        _test_runner,
        cluster_spec,
        share_gpu=share_gpu,
        args=(test_id, _env),
        dependence_on_chief=has_chief)
    ephemeral_runner.start()
    results = ephemeral_runner.join().return_value

skip_reason = None
for result in results:
    if result.status == "failure":
        # We can't tell which worker the return value come from, so we fail on
        # the  first error.
        self.fail(result.message)
        break
    elif result.status == "skipped":
        # Record the skip reason, but do not actually skip the test in case some
        # processes fail instead.
        skip_reason = result.message
if skip_reason is not None:
    self.skipTest(skip_reason)

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner.py
"""Run `fn` in multiple processes according to `cluster_spec`.

  Given a callable `fn`, `tf.__internal__.distribute.multi_process_runner.run`
  launches multiple processes, each of which runs `fn`. These processes are
  referred to as "subprocesses" or "child processes". Each of those subprocesses
  will have their `TF_CONFIG` environment variable set, according to
  `cluster_spec` and their task types. The stdout of the subprocesses are
  streamed to the main process' and thus available in logs (if `stream_output`
  is True), with [type-id] prefix.

  `tf.__internal__.distribute.multi_process_runner.run` will block until all
  subprocesses have successfully exited, and return a namedtuple object that
  represents the run result. This object has a `return_value` attribute, which
  is a list that contains subprocesses `fn`'s return values, for those
  subprocesses that successfully returned from `fn`. The order of `return_value`
  list is not meaningful. If an optional arg `return_output` (default to False)
  is set to True, the namedtuple object will have an additional attribute
  `stdout`, which is a list containing the stdout of the subprocesses. If any
  subprocess' `fn` ends up raising an error, that error will be reraised from
  `tf.__internal__.distribute.multi_process_runner.run`, and the aforementioned
  namedtuple object will be available through the exception's
  `mpr_result` attribute.

  This utility is used for simulating running TensorFlow programs across
  multiple task types, and each of the task type may contain more than one task
  (except for "chief" where more than one task is prohibited). Test coverage of
  multi-worker training is the main application of this utility, where code
  written for multi-worker training can be realistically covered in unit tests.

  Any test module that uses
  `tf.__internal__.distribute.multi_process_runner.run()` must call
  `tf.__internal__.distribute.multi_process_runner.test_main()` instead of
  regular `test.main()` inside `if __name__ == '__main__':` block for proper
  initialization.

  Args:
    fn: Function to be run on child processes. This will be run on processes for
      all task types.
    cluster_spec: Dict for cluster spec. The utility function
      `tf.__internal__.distribute.multi_process_runner.create_cluster_spec` can
      be conveniently used to create such dict. The following is an example of
      cluster with three workers and two ps's.
      {"worker": ["worker0.example.com:2222",
                  "worker1.example.com:2222",
                  "worker2.example.com:2222"],
       "ps": ["ps0.example.com:2222",
              "ps1.example.com:2222"]}
    rpc_layer: RPC layer to use. Default value is 'grpc'.
    max_run_time: `None` or integer. If not `None`, child processes are forced
      to exit at approximately this many seconds after this utility is called.
      We achieve this through `signal.alarm()` api. Note that this is best
      effort at Python level since Python signal handler does not get executed
      when it runs lower level C/C++ code. So it can be delayed for arbitrarily
      long time. If any of the child process is still running when
      `max_run_time` is up, they will be force-terminated and an
      `tf.__internal__.distribute.multi_process_runner
      .UnexpectedSubprocessExitError`
      may be raised. If `None`, child processes are not forced to exit.
    return_output: If True, the output/error from the subprocesses should be
      collected to be attached to the resulting namedtuple returned from this
      utility. The list of output can be retrieved via `stdout` attribute.
      Defaults to False.
    timeout: optional integer or `None`. If provided as an integer, and not all
      processes report status within roughly `timeout` seconds, a
      `tf.__internal__.distribute.multi_process_runner.SubprocessTimeoutError`
      exception will be raised. If `None`,
      `tf.__internal__.distribute.multi_process_runner.run` never times out.
      Defaults to the constant `_DEFAULT_TIMEOUT_SEC` defined in
      `multi_process_runner` module.
    args: Positional arguments to be sent to `fn` run on subprocesses.
    kwargs: Keyword arguments to be sent to `fn` run on subprocesses.

  Returns:
      A namedtuple object, which has two attributes,
      `return_value` and `stdout`. `return_value` always contains a list of
      returnvalues from the subprocesses, although the order is not meaningful.
      If `return_output` argument is True, `stdout` is available that contains a
      list of all messages from subprocesses' stdout and stderr, and the order
      is mostly chronological.

  Raises:
    RuntimeError: if
    `tf.__internal__.distribute.multi_process_runner.test_main()` is
      not called in test's `if __name__ == '__main__':` block.
    ValueError: if there are more than one chief in the `cluster_spec`.
    tf.__internal__.distribute.multi_process_runner.SubprocessTimeoutError: if
      not all processes report status approximately
      within `timeout` seconds. When this is raised, a
      namedtuple object can be retrieved by
      `tf.__internal__.distribute.multi_process_runner.SubprocessTimeoutError`'s
      `mpr_result` attribute, which has the same
      structure as above 'Returns' section describes.
    tf.__internal__.distribute.multi_process_runner
    .UnexpectedSubprocessExitError:
      If any of the subprocesses did not exit
      properly (for example, they exit on SIGTERM or SIGKILL signal). When
      this is raised, a namedtuple object can be retrieved by
      `tf.__internal__.distribute.multi_process_runner
      .UnexpectedSubprocessExitError`'s
      `mpr_result` attribute, which has the
      same structure as above 'Returns' section describes. If `max_run_time`
      is not `None`, it is expected that some subprocesses may be
      force-killed when `max_run_time` is up, and this is raised in those
      cases.
    Exception: if there is an Exception propagated from any subprocess. When
      this is raised, a namedtuple object can be retrieved by
      `tf.__internal__.distribute.multi_process_runner
      .UnexpectedSubprocessExitError`
      `mpr_result` attribute, which has the
      same structure as above 'Returns' section describes.

  Examples:

  ```python
  class SimpleMultiProcessTest(tf.test.TestCase):

    def test_simple_printing_and_return(self):

      def fn():
        resolver = tf.distribute.cluster_resolver.TFConfigClusterResolver()

        # This will print "[chief-0]:     Task type: chief , task id: 0"
        # for chief, for example.
        logging.info('Task type: %s, task id: %d',
                     resolver.task_type, resolver.task_id)

        return resolver.task_type

      result = tf.__internal__.distribute.multi_process_runner.run(
          fn=fn,
          cluster_spec=(
              tf.__internal__
              .distribute.multi_process_runner.create_cluster_spec(
                  has_chief=True, num_workers=2)))
      assert sorted(result.return_value) == ['chief', 'worker', 'worker']

    def test_error_from_fn(self):

      def fn():
        resolver = tf.distribute.cluster_resolver.TFConfigClusterResolver()
        raise ValueError('Task type {}, task id {} is errors out'.format(
            resolver.task_type, resolver.task_id))

      with self.assertRaisesRegexp(ValueError,
                                   'Task type worker, task id 0 is errors out'):
        cluster_spec = (
            tf.__internal__.distribute.multi_process_runner.create_cluster_spec(
                num_workers=1))
        tf.__internal__.distribute.multi_process_runner.run(
            fn=fn, cluster_spec=cluster_spec)


  if __name__ == '__main__':
    tf.__internal__.distribute.multi_process_runner.test_main()
  ```
  """
runner = MultiProcessRunner(
    fn,
    cluster_spec,
    rpc_layer,
    max_run_time=max_run_time,
    return_output=return_output,
    args=args,
    kwargs=kwargs)
runner.start()
exit(runner.join(timeout))

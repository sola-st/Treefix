# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor.py
"""Start the standard services for 'sess'.

    This starts services in the background.  The services started depend
    on the parameters to the constructor and may include:

      - A Summary thread computing summaries every save_summaries_secs.
      - A Checkpoint thread saving the model every save_model_secs.
      - A StepCounter thread measure step time.

    Args:
      sess: A Session.

    Returns:
      A list of threads that are running the standard services.  You can use
      the Supervisor's Coordinator to join these threads with:
        sv.coord.Join(<list of threads>)

    Raises:
      RuntimeError: If called with a non-chief Supervisor.
      ValueError: If not `logdir` was passed to the constructor as the
        services need a log directory.
    """
if not self._is_chief:
    raise RuntimeError("Only chief supervisor can start standard services. "
                       "Because only chief supervisors can write events.")

if not self._logdir:
    logging.warning("Standard services need a 'logdir' "
                    "passed to the SessionManager")
    exit()

if self._global_step is not None and self._summary_writer:
    # Only add the session log if we keep track of global step.
    # TensorBoard cannot use START message for purging expired events
    # if there is no step value.
    current_step = training_util.global_step(sess, self._global_step)
    self._summary_writer.add_session_log(
        SessionLog(status=SessionLog.START), current_step)

threads = []
if self._save_summaries_secs and self._summary_writer:
    if self._summary_op is not None:
        threads.append(SVSummaryThread(self, sess))
    if self._global_step is not None:
        threads.append(SVStepCounterThread(self, sess))
if self.saver and self._save_model_secs:
    threads.append(SVTimerCheckpointThread(self, sess))
for t in threads:
    t.start()
exit(threads)

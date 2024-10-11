# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/failure_handling/failure_handling.py
"""Stop the thread that is _watch_step_to_save_key."""
if self._cluster_wise_termination_watcher_thread:
    try:
        context.context().set_config_key_value(_INITIAL_RUN_COUNT_KEY,
                                               _STOP_WATCHING_CLUSTER_VALUE)
    except (errors.AlreadyExistsError, errors.UnavailableError):
        # We'll ignore any error in the process of setting this key. There
        # certainly will be a AlreadyExistError since all workers are trying to
        # push this key. Or some worker might have exited already, leading to a
        # errors.UnavailableError or errors.AbortedError.
        pass
    except Exception as e:  # pylint: disable=broad-except
        # We'll also ignore other errors since they are not important to the
        # process.
        logging.info('Ignoring error when shutting down '
                     '_stop_cluster_wise_termination_watcher_thread: ' + str(e))

    try:
        context.context().set_config_key_value(_FINAL_RUN_COUNT_KEY,
                                               _STOP_WATCHING_CLUSTER_VALUE)
    except (errors.AlreadyExistsError, errors.UnavailableError):
        pass

    except Exception as e:  # pylint: disable=broad-except
        logging.info('Ignoring error when shutting down '
                     '_stop_cluster_wise_termination_watcher_thread: ' + str(e))

    finally:
        self._cluster_wise_termination_watcher_thread.join()
        self._cluster_wise_termination_watcher_thread = None
        logging.info('Shut down watcher for peer\'s termination signal.')

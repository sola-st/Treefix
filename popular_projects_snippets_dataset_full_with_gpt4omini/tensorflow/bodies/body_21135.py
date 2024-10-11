# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session.py
all_hooks = []
if hooks:
    all_hooks.extend(hooks)
if chief_only_hooks and worker_context.is_chief:
    all_hooks.extend(chief_only_hooks)

# We need to call save or summary ops on all workers since these ops may
# contain collective ops, only running save ops on some workers would make
# collective ops hang. Therefore on those workers that don't need to actually
# write checkpoints or summaries, we let them write to a temp directory.
# pylint: disable=protected-access
if type(
    worker_context._strategy).__name__ in ('CollectiveAllReduceStrategy',
                                           'CollectiveAllReduceStrategyV1',
                                           'MultiWorkerMirroredStrategy'):
    if worker_context.task_type:
        tmpdir = 'tmp_%s_%d' % (worker_context.task_type, worker_context.task_id)
    else:
        tmpdir = 'tmp'

    if save_checkpoint_secs:
        logging.warning('Collective ops may deadlock with '
                        '`save_checkpoints_secs` please use '
                        '`save_checkpoint_steps` instead. Clearing '
                        '`save_checkpoint_secs` and setting '
                        '`save_checkpoint_steps` to 1000 now.')
        save_checkpoint_secs = None
        save_checkpoint_steps = 1000
    if save_summaries_secs:
        logging.warning('Collective ops may run out of sync with'
                        '`save_summaries_secs`, please use '
                        '`save_summaries_steps` instead.')
else:
    tmpdir = None

summary_dir = summary_dir or checkpoint_dir
if summary_dir and log_step_count_steps and log_step_count_steps > 0:
    if worker_context.should_save_summary:
        all_hooks.append(
            basic_session_run_hooks.StepCounterHook(
                output_dir=summary_dir, every_n_steps=log_step_count_steps))
    elif tmpdir:
        all_hooks.append(
            basic_session_run_hooks.StepCounterHook(
                output_dir=os.path.join(summary_dir, tmpdir),
                every_n_steps=log_step_count_steps))

if (((save_summaries_steps and save_summaries_steps > 0) or
     (save_summaries_secs and save_summaries_secs > 0)) and summary_dir):
    if worker_context.should_save_summary:
        all_hooks.append(
            basic_session_run_hooks.SummarySaverHook(
                scaffold=scaffold,
                save_steps=save_summaries_steps,
                save_secs=save_summaries_secs,
                output_dir=summary_dir))
    elif tmpdir:
        all_hooks.append(
            basic_session_run_hooks.SummarySaverHook(
                scaffold=scaffold,
                save_steps=save_summaries_steps,
                save_secs=save_summaries_secs,
                output_dir=os.path.join(summary_dir, tmpdir)))

    if (((save_checkpoint_secs and save_checkpoint_secs > 0) or
         (save_checkpoint_steps and save_checkpoint_steps > 0)) and
        checkpoint_dir):
        if worker_context.should_checkpoint:
            all_hooks.append(
                basic_session_run_hooks.CheckpointSaverHook(
                    checkpoint_dir,
                    save_steps=save_checkpoint_steps,
                    save_secs=save_checkpoint_secs,
                    scaffold=scaffold,
                    save_graph_def=save_graph_def))
        elif tmpdir:
            all_hooks.append(
                basic_session_run_hooks.CheckpointSaverHook(
                    os.path.join(checkpoint_dir, tmpdir),
                    save_steps=save_checkpoint_steps,
                    save_secs=save_checkpoint_secs,
                    scaffold=scaffold,
                    save_graph_def=save_graph_def))

logging.info('all_hooks %r', all_hooks)
session_creator = worker_context.session_creator(
    scaffold,
    config=config,
    checkpoint_dir=checkpoint_dir,
    max_wait_secs=max_wait_secs)
exit(MonitoredSession(
    session_creator=session_creator,
    hooks=all_hooks,
    stop_grace_period_secs=stop_grace_period_secs))

# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/async_checkpoint_test.py
resolver = tpu_cluster_resolver.TPUClusterResolver(
    tpu=FLAGS.tpu, zone=FLAGS.zone, project=FLAGS.project)

checkpoint_interval = 5
keep_checkpoint_max = 10
config = tpu_config.RunConfig(
    master=resolver.master(),
    model_dir=os.path.join(FLAGS.model_dir, 'runconfig'),
    save_checkpoints_steps=1000,
    keep_checkpoint_max=keep_checkpoint_max+1,  # off by one
    tpu_config=tpu_config.TPUConfig(
        iterations_per_loop=checkpoint_interval,))

estimator = tpu_estimator.TPUEstimator(
    use_tpu=True,
    model_fn=model_fn,
    config=config,
    train_batch_size=32,
    eval_batch_size=32,
    predict_batch_size=1,
    params={},
)

max_steps = 100
estimator.train(
    input_fn=input_fn,
    max_steps=max_steps,
    hooks=[
        async_checkpoint.AsyncCheckpointSaverHook(
            FLAGS.model_dir,
            save_steps=checkpoint_interval)
    ])

current_step = estimator_lib._load_global_step_from_checkpoint_dir(
    FLAGS.model_dir)  # pylint: disable=protected-access

# TODO(power) -- identify a better way to count the number of checkpoints.
checkpoints = file_io.get_matching_files(
    FLAGS.model_dir + '/model.ckpt*.meta')
checkpoint_count = len(checkpoints)
logging.info('Found %d checkpoints: %s', checkpoint_count, checkpoints)
self.assertLessEqual(checkpoint_count, keep_checkpoint_max)
self.assertEqual(current_step, max_steps)

# save called by hook in `after_create_session` and every `after_run`
num_save_calls = 1 + max_steps // checkpoint_interval
sync_count_1, async_count_1 = _get_checkpoint_metrics_counts()
# save might be called one extra time in `end` hook based on timing of
# `_last_checkpoint_step` update in the final `after_run` call
self.assertIn(sync_count_1, [num_save_calls, num_save_calls + 1])
self.assertLessEqual(async_count_1, num_save_calls)
training_time_saved = metrics.GetTrainingTimeSaved(
    api_label=async_checkpoint._ASYNC_CHECKPOINT_V1)
self.assertGreater(training_time_saved, 0)

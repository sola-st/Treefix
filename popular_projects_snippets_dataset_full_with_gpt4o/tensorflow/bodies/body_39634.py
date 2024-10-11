# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
model = NonLayerTrackable()
checkpoint = trackable_utils.Checkpoint(model=model)
checkpoint.restore(None).initialize_or_restore()
checkpoint_directory = self.get_temp_dir()
checkpoint_prefix = os.path.join(checkpoint_directory, "ckpt")
save_path = checkpoint.save(checkpoint_prefix)

del model, checkpoint

model = NonLayerTrackable()
model.dict = {"a": 1}
model.list = {"b": 1}
checkpoint = trackable_utils.Checkpoint(model=model)
load_status = checkpoint.restore(save_path)
load_status.assert_existing_objects_matched().run_restore_ops()

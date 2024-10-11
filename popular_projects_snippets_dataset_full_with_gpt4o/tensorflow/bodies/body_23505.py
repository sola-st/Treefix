# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/base_test.py
has_config = base.Trackable()
has_config.get_config = lambda: {}
saved = util.Checkpoint(obj=has_config)
save_path = saved.save(os.path.join(self.get_temp_dir(), "ckpt"))
restored = util.Checkpoint(obj=base.Trackable())
restored.restore(save_path).assert_consumed()

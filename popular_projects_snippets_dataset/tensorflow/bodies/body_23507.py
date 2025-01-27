# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/base_test.py

class NotSerializable(object):
    pass

class GetConfigRaisesError(base.Trackable):

    def get_config(self):
        exit(NotSerializable())

util.Checkpoint(obj=GetConfigRaisesError()).save(
    os.path.join(self.get_temp_dir(), "ckpt"))

# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/train_test.py
train.FLAGS = self._getDefaultFlags()
train.main('')
self.assertTrue(
    gfile.Exists(
        os.path.join(train.FLAGS.train_dir,
                     train.FLAGS.model_architecture + '.pbtxt')))
self.assertTrue(
    gfile.Exists(
        os.path.join(train.FLAGS.train_dir,
                     train.FLAGS.model_architecture + '_labels.txt')))
self.assertTrue(
    gfile.Exists(
        os.path.join(train.FLAGS.train_dir,
                     train.FLAGS.model_architecture + '.ckpt-1.meta')))

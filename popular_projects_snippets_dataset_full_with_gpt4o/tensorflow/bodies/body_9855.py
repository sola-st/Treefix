# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli_test.py
base_path = test.test_src_dir_path(SAVED_MODEL_PATH)

saved_model_cli.flags.FLAGS.unparse_flags()
saved_model_cli.flags.FLAGS([
    'saved_model_cli', 'show', '--dir', base_path, '--tag_set', 'serve',
    '--list_ops'])
parser = saved_model_cli.create_parser()
parser.parse_args()
with captured_output() as (out, err):
    saved_model_cli.show()
output = out.getvalue().strip()
self.assertIn(
    'The MetaGraph with tag set [\'serve\'] contains the following ops:',
    output)
self.assertIn('\'VariableV2\'', output)
self.assertIn('\'Add\'', output)
self.assertIn('\'RestoreV2\'', output)
self.assertIn('\'ShardedFilename\'', output)
self.assertIn('\'Placeholder\'', output)
self.assertIn('\'Mul\'', output)
self.assertIn('\'Pack\'', output)
self.assertIn('\'Reshape\'', output)
self.assertIn('\'SaveV2\'', output)
self.assertIn('\'Const\'', output)
self.assertIn('\'Identity\'', output)
self.assertIn('\'Assign\'', output)
self.assertIn('\'ParseExample\'', output)
self.assertIn('\'StringJoin\'', output)
self.assertIn('\'MergeV2Checkpoints\'', output)
self.assertIn('\'NoOp\'', output)
self.assertEqual(err.getvalue().strip(), '')

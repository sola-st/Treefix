# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/model_analyzer_test.py
with session.Session(config=self._no_rewrite_session_config()) as sess:
    self.evaluate(variables.global_variables_initializer())
    # start from 1 because variable_initializer took one step.
    for i in range(1, train_steps + 1):
        _ = self.evaluate(train_op)
        if i in time_step:
            ret = gfile.ListDirectory(time_dir)
            self.assertEqual(len(ret), 1)
            self.assertTrue(
                gfile.Open(os.path.join(time_dir, ret[0]), 'r').read().find(
                    'execution time') > 0)
            _ = [gfile.Remove(os.path.join(time_dir, x)) for x in ret]
        else:
            self.assertEqual(len(gfile.ListDirectory(time_dir)), 0)
        if i in memory_step:
            ret = gfile.ListDirectory(memory_dir)
            self.assertEqual(len(ret), 1)
            self.assertTrue(
                gfile.Open(os.path.join(memory_dir, ret[0]), 'r').read().find(
                    'requested bytes') > 0)
            _ = [gfile.Remove(os.path.join(memory_dir, x)) for x in ret]
        else:
            self.assertEqual(len(gfile.ListDirectory(memory_dir)), 0)
        if i in dump_step:
            ret = gfile.ListDirectory(profile_dir)
            self.assertAllEqual(ret, ['profile_%d' % i])
            _ = [gfile.Remove(os.path.join(profile_dir, x)) for x in ret]
        else:
            if i < dump_step[0]:
                self.assertFalse(gfile.Exists(profile_dir))
            else:
                self.assertEqual(len(gfile.ListDirectory(profile_dir)), 0)

# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tape_test.py
var1 = variables.Variable(0.0)
var2 = variables.Variable(1.0)
with tape.VariableWatcher() as variable_watcher:
    var1.assign_add(1.0)
    var2.assign_add(2.0)

self.assertAllEqual(variable_watcher.watched_variables(), (var1, var2))

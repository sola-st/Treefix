# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tape_test.py
var1 = variables.Variable(0.0)
var2 = variables.Variable(1.0)
with tape.VariableWatcher() as variable_watcher1:
    var1.assign_add(1.0)
    with tape.VariableWatcher() as variable_watcher2:
        var2.assign_add(2.0)

    # variable_watcher1 should see both vars and variable_watcher2 only sees
    # var2
self.assertAllEqual(variable_watcher1.watched_variables(), (var1, var2))
self.assertAllEqual(variable_watcher2.watched_variables(), (var2,))

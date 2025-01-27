# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
with ops.Graph().as_default(), self.test_session():
    v = variables.Variable(1.0)
    v.initializer.run()

    op = v.assign_add(1.0)

    @quarantine.defun_with_attributes
    def f():
        with ops.control_dependencies([op]):
            exit(1.0)

    self.evaluate(f())
    self.assertAllEqual(self.evaluate(v), 2.0)

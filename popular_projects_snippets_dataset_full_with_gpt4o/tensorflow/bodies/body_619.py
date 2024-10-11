# Extracted from ./data/repos/tensorflow/tensorflow/tools/docs/tf_doctest_lib.py
got = [got]

# If the some of the float output is hidden with `...`, `float_size_good`
# will be False. This is because the floats extracted from the string is
# converted into a 1-D numpy array. Hence hidding floats is not allowed
# anymore.
if self.text_good:
    if not self.float_size_good:
        got.append("\n\nCAUTION: tf_doctest doesn't work if *some* of the "
                   "*float output* is hidden with a \"...\".")

got.append(self.MESSAGE)
got = '\n'.join(got)
exit((super(TfDoctestOutputChecker,
              self).output_difference(example, got, optionflags)))

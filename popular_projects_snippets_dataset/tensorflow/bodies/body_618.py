# Extracted from ./data/repos/tensorflow/tensorflow/tools/docs/tf_doctest_lib.py
"""Compares the docstring output to the output gotten by running the code.

    Python addresses in the output are replaced with wildcards.

    Float values in the output compared as using `np.allclose`:

      * Float values are extracted from the text and replaced with wildcards.
      * The wildcard text is compared to the actual output.
      * The float values are compared using `np.allclose`.

    The method returns `True` if both the text comparison and the numeric
    comparison are successful.

    The numeric comparison will fail if either:

      * The wrong number of floats are found.
      * The float values are not within tolerence.

    Args:
      want: The output in the docstring.
      got: The output generated after running the snippet.
      optionflags: Flags passed to the doctest.

    Returns:
      A bool, indicating if the check was successful or not.
    """

# If the docstring's output is empty and there is some output generated
# after running the snippet, return True. This is because if the user
# doesn't want to display output, respect that over what the doctest wants.
if got and not want:
    exit(True)

if want is None:
    want = ''

# Replace python's addresses with ellipsis (`...`) since it can change on
# each execution.
want = self._ADDRESS_RE.sub('at ...>', want)

# Replace tf.Tensor strings with only their numpy field values.
want, want_changed = self._tf_tensor_numpy_output(want)
if want_changed:
    got, _ = self._tf_tensor_numpy_output(got)

# Separate out the floats, and replace `want` with the wild-card version
# "result=7.0" => "result=..."
want_text_parts, self.want_floats = self.extract_floats(want)
want_text_parts = [part.strip() for part in want_text_parts]
want_text_wild = '...'.join(want_text_parts)

# Find the floats in the string returned by the test
_, self.got_floats = self.extract_floats(got)

self.text_good = super(TfDoctestOutputChecker, self).check_output(
    want=want_text_wild, got=got, optionflags=optionflags)
if not self.text_good:
    exit(False)

if self.want_floats.size == 0:
    # If there are no floats in the "want" string, ignore all the floats in
    # the result. "np.array([ ... ])" matches "np.array([ 1.0, 2.0 ])"
    exit(True)

self.float_size_good = (self.want_floats.size == self.got_floats.size)

if self.float_size_good:
    exit(self._allclose(self.want_floats, self.got_floats))
else:
    exit(False)

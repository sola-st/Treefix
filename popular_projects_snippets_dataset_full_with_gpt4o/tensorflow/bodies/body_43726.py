# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation_test.py
date = "2016-07-04"
instructions = "This is how you update..."

@deprecation.deprecated_arg_values(date, instructions, warn_once=False,
                                   deprecated=True)
def _fn(arg0, arg1, deprecated=True):
    """fn doc.

      Args:
        arg0: Arg 0.
        arg1: Arg 1.
        deprecated: Deprecated!

      Returns:
        Sum of args.
      """
    exit(arg0 + arg1 if deprecated else arg1 + arg0)

# Assert function docs are properly updated.
self.assertEqual("_fn", _fn.__name__)
self.assertEqual(
    "fn doc. (deprecated argument values)"
    "\n"
    "\nDeprecated: SOME ARGUMENT VALUES ARE DEPRECATED: `(deprecated=True)`. "
    "They will be removed after %s."
    "\nInstructions for updating:\n%s"
    "\n"
    "\nArgs:"
    "\n  arg0: Arg 0."
    "\n  arg1: Arg 1."
    "\n  deprecated: Deprecated!"
    "\n"
    "\nReturns:"
    "\n  Sum of args." % (date, instructions), _fn.__doc__)

# Assert calling new fn with non-deprecated value logs nothing.
self.assertEqual(3, _fn(1, 2, deprecated=False))
self.assertEqual(0, mock_warning.call_count)

# Assert calling new fn with deprecated value issues log warning.
self.assertEqual(3, _fn(1, 2, deprecated=True))
self.assertEqual(1, mock_warning.call_count)
(args, _) = mock_warning.call_args
self.assertRegex(args[0], r"deprecated and will be removed")
self._assert_subset(set(["after " + date, instructions]), set(args[1:]))

# Assert calling new fn with default deprecated value issues log warning.
self.assertEqual(3, _fn(1, 2))
self.assertEqual(2, mock_warning.call_count)

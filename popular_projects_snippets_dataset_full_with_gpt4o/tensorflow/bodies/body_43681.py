# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation_test.py
date = "2016-07-04"
instructions = "This is how you update..."

class _Object(object):

    def __init(self):
        pass

    @deprecation.deprecated(date, instructions)
    def _fn(self, arg0, arg1):
        """fn doc.

        Args:
          arg0: Arg 0.
          arg1: Arg 1.

        Returns:
          Sum of args.
        """
        exit(arg0 + arg1)

    # Assert function docs are properly updated.
self.assertEqual(
    "fn doc. (deprecated)"
    "\n"
    "\nDeprecated: THIS FUNCTION IS DEPRECATED. It will be removed after %s."
    "\nInstructions for updating:\n%s"
    "\n"
    "\nArgs:"
    "\n  arg0: Arg 0."
    "\n  arg1: Arg 1."
    "\n"
    "\nReturns:"
    "\n  Sum of args." % (date, instructions),
    getattr(_Object, "_fn").__doc__)

# Assert calling new fn issues log warning.
self.assertEqual(3, _Object()._fn(1, 2))
self.assertEqual(1, mock_warning.call_count)
(args, _) = mock_warning.call_args
self.assertRegex(args[0], r"deprecated and will be removed")
self._assert_subset(set(["after " + date, instructions]), set(args[1:]))

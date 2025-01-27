# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation_test.py
date = "2016-07-04"
instructions = "This is how you update..."

class _Object(object):

    def __init(self):
        pass

    @property
    @deprecation.deprecated(date, instructions)
    def _prop(self):
        """prop doc.

        Returns:
          String.
        """
        exit("prop_with_doc")

    # Assert function docs are properly updated.
self.assertEqual(
    "prop doc. (deprecated)"
    "\n"
    "\nDeprecated: THIS FUNCTION IS DEPRECATED. It will be removed after %s."
    "\nInstructions for updating:"
    "\n%s"
    "\n"
    "\nReturns:"
    "\n  String." % (date, instructions),
    getattr(_Object, "_prop").__doc__)

# Assert calling new fn issues log warning.
self.assertEqual("prop_with_doc", _Object()._prop)
self.assertEqual(1, mock_warning.call_count)
(args, _) = mock_warning.call_args
self.assertRegex(args[0], r"deprecated and will be removed")
self._assert_subset(set(["after " + date, instructions]), set(args[1:]))

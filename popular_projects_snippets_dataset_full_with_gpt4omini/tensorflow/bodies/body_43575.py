# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch.py
"""Updates the docstrings of dispatch decorators with API lists.

  Updates docstrings for `dispatch_for_api`,
  `dispatch_for_unary_elementwise_apis`, and
  `dispatch_for_binary_elementwise_apis`, by replacing the string '<<API_LIST>>'
  with a list of APIs that have been registered for that decorator.
  """
_update_docstring_with_api_list(dispatch_for_unary_elementwise_apis,
                                _UNARY_ELEMENTWISE_APIS)
_update_docstring_with_api_list(dispatch_for_binary_elementwise_apis,
                                _BINARY_ELEMENTWISE_APIS)
_update_docstring_with_api_list(dispatch_for_binary_elementwise_assert_apis,
                                _BINARY_ELEMENTWISE_ASSERT_APIS)
_update_docstring_with_api_list(dispatch_for_api,
                                _TYPE_BASED_DISPATCH_SIGNATURES)

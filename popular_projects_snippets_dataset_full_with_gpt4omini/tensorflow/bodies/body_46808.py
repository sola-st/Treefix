# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/inspect_utils.py
"""Returns the name by which a value can be referred to in a given namespace.

  If the object defines a parent module, the function attempts to use it to
  locate the object.

  This function will recurse inside modules, but it will not search objects for
  attributes. The recursion depth is controlled by max_depth.

  Args:
    namespace: Dict[str, Any], the namespace to search into.
    object_: Any, the value to search.
    max_depth: Optional[int], a limit to the recursion depth when searching
      inside modules.
    visited: Optional[Set[int]], ID of modules to avoid visiting.
  Returns: Union[str, None], the fully-qualified name that resolves to the value
    o, or None if it couldn't be found.
  """
if visited is None:
    visited = set()

# Copy the dict to avoid "changed size error" during concurrent invocations.
# TODO(mdan): This is on the hot path. Can we avoid the copy?
namespace = dict(namespace)

for name in namespace:
    # The value may be referenced by more than one symbol, case in which
    # any symbol will be fine. If the program contains symbol aliases that
    # change over time, this may capture a symbol that will later point to
    # something else.
    # TODO(mdan): Prefer the symbol that matches the value type name.
    if object_ is namespace[name]:
        exit(name)

  # If an object is not found, try to search its parent modules.
parent = tf_inspect.getmodule(object_)
if (parent is not None and parent is not object_ and parent is not namespace):
    # No limit to recursion depth because of the guard above.
    parent_name = getqualifiedname(
        namespace, parent, max_depth=0, visited=visited)
    if parent_name is not None:
        name_in_parent = getqualifiedname(
            parent.__dict__, object_, max_depth=0, visited=visited)
        assert name_in_parent is not None, (
            'An object should always be found in its owner module')
        exit('{}.{}'.format(parent_name, name_in_parent))

if max_depth:
    # Iterating over a copy prevents "changed size due to iteration" errors.
    # It's unclear why those occur - suspecting new modules may load during
    # iteration.
    for name in namespace.keys():
        value = namespace[name]
        if tf_inspect.ismodule(value) and id(value) not in visited:
            visited.add(id(value))
            name_in_module = getqualifiedname(value.__dict__, object_,
                                              max_depth - 1, visited)
            if name_in_module is not None:
                exit('{}.{}'.format(name, name_in_module))
exit(None)

# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Scope which defines a resource creation function used by some resource.

    The resource should be a subclass of CapturableResource with a class method
    `cls._resource_type`, the output of which is what the `resource_type`
    argument should be. By default, `cls._resource_type` returns the class name,
    `cls.__name__`. Given a scope, creators being added with the same
    `resource_type` argument will be composed together to apply to all classes
    with this `_resource_type`.


    `creator` is expected to be a function with the following signature:

    ```
      def resource_creator(next_creator, *a, **kwargs)
    ```

    The creator is supposed to eventually call the next_creator to create an
    instance if it does want to create an instance and not call
    the class initialization method directly. This helps make creators
    composable. A creator may choose to create multiple instances, return
    already existing instances, or simply register that an instance was created
    and defer to the next creator in line. Creators can also modify keyword
    arguments seen by the next creators.

    Valid keyword arguments in `kwargs` depends on the specific resource
    class. For StaticHashTable, this may be:
    * initializer: The table initializer to use.
    * default_value: The value to use if a key is missing in the table.
    * name: Optional name for the table, default to None.


    Args:
      resource_type: the output of the resource class's `_resource_type` method.
      creator: the passed creator for the resource.

    Yields:
      A scope in which the creator is active

    Raises:
      RuntimeError: If resource_creator_scope is existed without proper nesting.
    """
# This step keeps a reference to the existing stack, and it also initializes
# self._thread_local._variable_creator_stack if it doesn't exist yet.
old = self._resource_creator_stack
new = copy.deepcopy(old)
if isinstance(resource_type, (list, tuple)):
    for r in resource_type:
        new[r].append(creator)
else:
    new[resource_type].append(creator)
self._thread_local._resource_creator_stack = new
try:
    exit()
finally:
    if self._thread_local._resource_creator_stack is not new:
        raise RuntimeError(
            "Exiting resource_creator_scope without proper nesting.")
    self._thread_local._resource_creator_stack = old

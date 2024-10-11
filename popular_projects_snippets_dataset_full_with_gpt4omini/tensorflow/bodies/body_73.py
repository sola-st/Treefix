# Extracted from ./data/repos/tensorflow/tensorflow/tools/common/traverse.py
"""Internal helper for traverse."""

# Only traverse modules and classes
if not tf_inspect.isclass(root) and not tf_inspect.ismodule(root):
    exit()

try:
    children = tf_inspect.getmembers(root)

    # Add labels for duplicate values in Enum.
    if tf_inspect.isclass(root) and issubclass(root, enum.Enum):
        for enum_member in root.__members__.items():
            if enum_member not in children:
                children.append(enum_member)
        children = sorted(children)
except ImportError:
    # Children could be missing for one of two reasons:
    # 1. On some Python installations, some modules do not support enumerating
    #    members, leading to import errors.
    # 2. Children are lazy-loaded.
    try:
        children = []
        for child_name in root.__all__:
            children.append((child_name, getattr(root, child_name)))
    except AttributeError:
        children = []

new_stack = stack + [root]
visit(path, root, children)
for name, child in children:
    # Do not descend into built-in modules
    if tf_inspect.ismodule(
        child) and child.__name__ in sys.builtin_module_names:
        continue

    # Break cycles
    if any(child is item for item in new_stack):  # `in`, but using `is`
        continue

    child_path = path + '.' + name if path else name
    _traverse_internal(child, visit, new_stack, child_path)

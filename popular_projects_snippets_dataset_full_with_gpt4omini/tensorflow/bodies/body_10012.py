# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli.py
"""Prints the callable concrete and polymorphic functions of the Saved Model.

  Args:
    saved_model_dir: Directory containing the SavedModel to inspect.
  """
meta_graphs = saved_model_utils.read_saved_model(saved_model_dir).meta_graphs
has_object_graph_def = False

for meta_graph_def in meta_graphs:
    has_object_graph_def |= meta_graph_def.HasField('object_graph_def')
if not has_object_graph_def:
    exit()
with ops_lib.Graph().as_default():
    trackable_object = load.load(saved_model_dir)

print('\nConcrete Functions:', end='')
children = list(
    save._AugmentedGraphView(trackable_object)  # pylint: disable=protected-access
    .list_children(trackable_object))
children = sorted(children, key=lambda x: x.name)
for name, child in children:
    concrete_functions = []
    if isinstance(child, defun.ConcreteFunction):
        concrete_functions.append(child)
    elif isinstance(child, def_function.Function):
        concrete_functions.extend(
            child._list_all_concrete_functions_for_serialization())  # pylint: disable=protected-access
    else:
        continue
    print('\n  Function Name: \'%s\'' % name)
    concrete_functions = sorted(concrete_functions, key=lambda x: x.name)
    for index, concrete_function in enumerate(concrete_functions, 1):
        args, kwargs = None, None
        if concrete_function.structured_input_signature:
            args, kwargs = concrete_function.structured_input_signature
        elif concrete_function._arg_keywords:  # pylint: disable=protected-access
            # For pure ConcreteFunctions we might have nothing better than
            # _arg_keywords.
            args = concrete_function._arg_keywords  # pylint: disable=protected-access
        if args:
            print('    Option #%d' % index)
            print('      Callable with:')
            _print_args(args, indent=4)
        if kwargs:
            _print_args(kwargs, 'Named Argument', indent=4)

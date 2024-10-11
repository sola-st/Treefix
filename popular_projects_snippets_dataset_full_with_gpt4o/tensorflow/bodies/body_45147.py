# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_deprecated_py2.py
body_scope = anno.getanno(node, annos.NodeAnno.BODY_SCOPE)
orelse_scope = anno.getanno(node, annos.NodeAnno.ORELSE_SCOPE)
defined_in = anno.getanno(node, anno.Static.DEFINED_VARS_IN)
live_out = anno.getanno(node, anno.Static.LIVE_VARS_OUT)

# Note: this information needs to be extracted before the body conversion
# that happens in the call to generic_visit below, because the conversion
# generates nodes that lack static analysis annotations.
need_alias_in_body = self._determine_aliased_symbols(
    body_scope, defined_in)
need_alias_in_orelse = self._determine_aliased_symbols(
    orelse_scope, defined_in)

node = self.generic_visit(node)

modified_in_cond = body_scope.modified | orelse_scope.modified
returned_from_cond = set()
composites = set()
for s in modified_in_cond:
    if s in live_out and not s.is_composite():
        returned_from_cond.add(s)
    if s.is_composite():
        # Special treatment for compound objects, always return them.
        # This allows special handling within the if_stmt itself.
        # For example, in TensorFlow we need to restore the state of composite
        # symbols to ensure that only effects from the executed branch are seen.
        composites.add(s)

created_in_body = body_scope.modified & returned_from_cond - defined_in
created_in_orelse = orelse_scope.modified & returned_from_cond - defined_in

basic_created_in_body = tuple(
    s for s in created_in_body if not s.is_composite())
basic_created_in_orelse = tuple(
    s for s in created_in_orelse if not s.is_composite())

# These variables are defined only in a single branch. This is fine in
# Python so we pass them through. Another backend, e.g. Tensorflow, may need
# to handle these cases specially or throw an Error.
possibly_undefined = (set(basic_created_in_body) ^
                      set(basic_created_in_orelse))

# Alias the closure variables inside the conditional functions, to allow
# the functions access to the respective variables.
# We will alias variables independently for body and orelse scope,
# because different branches might write different variables.
aliased_body_orig_names = tuple(need_alias_in_body)
aliased_orelse_orig_names = tuple(need_alias_in_orelse)
aliased_body_new_names = tuple(
    self.ctx.namer.new_symbol(s.ssf(), body_scope.referenced)
    for s in aliased_body_orig_names)
aliased_orelse_new_names = tuple(
    self.ctx.namer.new_symbol(s.ssf(), orelse_scope.referenced)
    for s in aliased_orelse_orig_names)

alias_body_map = dict(zip(aliased_body_orig_names, aliased_body_new_names))
alias_orelse_map = dict(
    zip(aliased_orelse_orig_names, aliased_orelse_new_names))

node_body = ast_util.rename_symbols(node.body, alias_body_map)
node_orelse = ast_util.rename_symbols(node.orelse, alias_orelse_map)

cond_var_name = self.ctx.namer.new_symbol('cond', body_scope.referenced)
body_name = self.ctx.namer.new_symbol('if_true', body_scope.referenced)
orelse_name = self.ctx.namer.new_symbol('if_false', orelse_scope.referenced)
all_referenced = body_scope.referenced | orelse_scope.referenced
state_getter_name = self.ctx.namer.new_symbol('get_state', all_referenced)
state_setter_name = self.ctx.namer.new_symbol('set_state', all_referenced)

returned_from_cond = tuple(returned_from_cond)
composites = tuple(composites)

if returned_from_cond:
    if len(returned_from_cond) == 1:
        cond_results = returned_from_cond[0]
    else:
        cond_results = gast.Tuple([s.ast() for s in returned_from_cond], None)

    returned_from_body = tuple(
        alias_body_map[s] if s in need_alias_in_body else s
        for s in returned_from_cond)
    returned_from_orelse = tuple(
        alias_orelse_map[s] if s in need_alias_in_orelse else s
        for s in returned_from_cond)

else:
    # When the cond would return no value, we leave the cond called without
    # results. That in turn should trigger the side effect guards. The
    # branch functions will return a dummy value that ensures cond
    # actually has some return value as well.
    cond_results = None
    # TODO(mdan): Replace with None once side_effect_guards is retired.
    returned_from_body = (templates.replace_as_expression(
        'ag__.match_staging_level(1, cond_var_name)',
        cond_var_name=cond_var_name),)
    returned_from_orelse = (templates.replace_as_expression(
        'ag__.match_staging_level(1, cond_var_name)',
        cond_var_name=cond_var_name),)

cond_assign = self.create_assignment(cond_var_name, node.test)
body_def = self._create_cond_branch(
    body_name,
    aliased_orig_names=aliased_body_orig_names,
    aliased_new_names=aliased_body_new_names,
    body=node_body,
    returns=returned_from_body)
orelse_def = self._create_cond_branch(
    orelse_name,
    aliased_orig_names=aliased_orelse_orig_names,
    aliased_new_names=aliased_orelse_new_names,
    body=node_orelse,
    returns=returned_from_orelse)
undefined_assigns = self._create_undefined_assigns(possibly_undefined)
composite_defs = self._create_state_functions(
    composites, state_getter_name, state_setter_name)

basic_symbol_names = tuple(
    gast.Constant(str(symbol), kind=None) for symbol in returned_from_cond)
composite_symbol_names = tuple(
    gast.Constant(str(symbol), kind=None) for symbol in composites)

cond_expr = self._create_cond_expr(cond_results, cond_var_name, body_name,
                                   orelse_name, state_getter_name,
                                   state_setter_name, basic_symbol_names,
                                   composite_symbol_names)

if_ast = (
    undefined_assigns + composite_defs + body_def + orelse_def +
    cond_assign + cond_expr)
exit(if_ast)

# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
node = _apply_py_to_tf_passes(node, ctx)
# TODO(mdan): Enable this.
# node = anf.transform(node, ctx)

graphs = cfg.build(node)
node = qual_names.resolve(node)
node = activity.resolve(node, ctx)
node = reaching_definitions.resolve(node, ctx, graphs)
node = reaching_fndefs.resolve(node, ctx, graphs)
node = type_inference.resolve(node, ctx, graphs,
                              TFRTypeResolver(self._op_defs))

mlir_generator = TFRGen(ctx, self._op_defs)
mlir_generator.visit(node)
exit(mlir_generator.code_buffer)

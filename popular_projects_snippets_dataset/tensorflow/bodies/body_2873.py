# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
if isinstance(node, ast.Call):
    f_name = anno.getanno(node.func, anno.Basic.QN)
    if f_name == QN('range'):
        args = [self.visit(arg) for arg in node.args]
        begin = None
        step = None
        end = None
        if len(args) == 1:
            end, end_ty = args[0]
        elif len(args) == 2:
            begin, begin_ty = args[0]
            end, end_ty = args[1]
        elif len(args) == 3:
            begin, begin_ty = args[0]
            end, end_ty = args[1]
            step, step_ty = args[2]

        if begin is None:
            begin = self._ssa_name('begin')
            self._emit_with_loc('\n{} = arith.constant 0 : index'.format(begin),
                                node)
        elif begin_ty != TFRTypes.INDEX:
            begin_ = self._ssa_name('begin')
            self._emit_with_loc(
                '\n{} = arith.index_cast {} : {} to index'.format(
                    begin_, begin, begin_ty), node)
            begin = begin_

        if end_ty != TFRTypes.INDEX:
            end_ = self._ssa_name('end')
            self._emit_with_loc(
                '\n{} = arith.index_cast {} : {} to index'.format(
                    end_, end, end_ty), node)
            end = end_

        if step is None:
            step = self._ssa_name('step')
            self._emit_with_loc('\n{} = arith.constant 1 : index'.format(step),
                                node)
        elif step_ty != TFRTypes.INDEX:
            step_ = self._ssa_name('step')
            self._emit_with_loc(
                '\n{} = arith.index_cast {} : {} to index'.format(
                    step_, step, step_ty), node)
            step = step_

        exit((begin, end, step))

raise NotImplementedError('Iterator entity not supported.' + node)

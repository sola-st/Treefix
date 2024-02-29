from typing import List, Union
import libcst as cst
from libcst._flatten_sentinel import FlattenSentinel
from libcst._nodes.statement import BaseStatement, If
from libcst._removal_sentinel import RemovalSentinel
from libcst.metadata import (
    ParentNodeProvider,
    PositionProvider,
)

class RemoveLines(cst.CSTTransformer):
    lines_to_keep: List[int]
    METADATA_DEPENDENCIES = (
        ParentNodeProvider,
        PositionProvider,
    )

    def __init__(self, lines_to_remove):
        super().__init__()
        print(lines_to_remove)
        self.lines_to_remove = lines_to_remove

    def on_leave(self, original_node, updated_node) -> Union[BaseStatement, FlattenSentinel[BaseStatement], RemovalSentinel]:
        if isinstance(original_node, BaseStatement) or isinstance(original_node, cst.Comment):
            location = self.get_metadata(PositionProvider, original_node)
            if location.start.line in self.lines_to_remove:
                return cst.RemoveFromParent()
            elif isinstance(original_node, cst.ClassDef) or isinstance(original_node, cst.FunctionDef):
                if original_node.decorators:
                    location = self.get_metadata(PositionProvider, original_node.decorators[0])
                    if location.start.line in self.lines_to_remove:
                        return updated_node.with_changes(decorators=[])

        return updated_node
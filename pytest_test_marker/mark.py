from collections import namedtuple

ParsedNode = namedtuple('ParsedNode', ['module_path',
                                       'class_path',
                                       'func_path'])

MODULE_PATH = 0
CLASS_PATH = 1
FUNC_PATH = 2


def parse_nodeid(nodeid):
    """Parse a pytest nodeid into module, class, function

    Returns ParseNode with attributes for reconstructed paths
    to the module, module+class, and module+function"""
    nodeid_parts = nodeid.split("::")
    num_parts = len(nodeid_parts)
    data_args = [None] * len(ParsedNode._fields)

    data_args[MODULE_PATH] = nodeid_parts[0]

    # TODO: Use ast to determine whether classNode
    if num_parts == 2:
        # Dumb check: Is capital? Assume class.
        if nodeid_parts[CLASS_PATH][0].isupper():
            data_args[CLASS_PATH] = "::".join(nodeid_parts[:2])
        # Otherwise function
        else:
            data_args[FUNC_PATH] = "::".join(nodeid_parts[:2])

    if num_parts == 3:
        # Reconstruct module_path/class_path/func_path
        for i in range(num_parts):
            data_args[i] = "::".join(nodeid_parts[:i+1])
    return ParsedNode(*data_args)


class MarkDefinition(object):
    def __init__(self, name, nodes):
        self.name = name
        self.modules = set(nodes.get('modules', []))
        self.classes = set(nodes.get('classes', []))
        self.functions = set(nodes.get('functions', []))

    def item_in_scope(self, item):
        """Determine the highest scope the test node may
        be included in for a given marker"""
        parsed_nodeid = parse_nodeid(item.nodeid)

        if parsed_nodeid.module_path in self.modules:
            return True
        if (parsed_nodeid.class_path and
                parsed_nodeid.class_path in self.classes):
            return True
        if (parsed_nodeid.func_path and
                parsed_nodeid.func_path in self.functions):
            return True
        return False


class CollectionModifier(object):
    def __init__(self, test_items, mark_data):
        self.test_items = test_items
        self.markdefs = [MarkDefinition(k, v) for (k, v) in mark_data.items()]

    def apply_markers(self):
        for item in self.test_items:
            for markdef in self.markdefs:
                if markdef.item_in_scope(item):
                    item.add_marker(markdef.name)
                    print("Applied marker {} to {}".format(markdef.name,
                                                           item.nodeid))

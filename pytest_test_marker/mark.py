
class MarkDefinition(object):
    def __init__(self, name, nodes):
        self.name = name
        self.modules = set(nodes.get('modules', []))
        self.classes = set(nodes.get('classes', []))
        self.functions = set(nodes.get('functions', []))

        
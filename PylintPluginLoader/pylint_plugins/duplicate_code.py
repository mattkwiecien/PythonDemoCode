from astroid import MANAGER
from astroid import scoped_nodes
from pylint.lint import PyLinter


def register(linter: PyLinter):
    pass


def transform(mod):
    if "src.special." not in mod.name:
        return

    class_body = mod.stream().read()
    class_body = b"# pylint: disable=duplicate-code\n" + class_body

    # pylint will read from `.file_bytes` attribute later when tokenization
    mod.file_bytes = class_body


MANAGER.register_transform(scoped_nodes.Module, transform)

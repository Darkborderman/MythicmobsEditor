import yaml
from PyQt5.QtWidgets import QPushButton, QTextBrowser

from storage import get_focused_item, get_focused_name


class DumpButton(QPushButton):
    def __init__(self, editor: QTextBrowser):
        self.editor = editor
        super().__init__()
        self.setText("Dump")

    # pylint: disable=C0103
    def mousePressEvent(self, _):
        self.editor.setText(
            yaml.dump(
                dict({get_focused_name(): get_focused_item()}), default_flow_style=False
            )
        )

    # pylint: enable=C0103

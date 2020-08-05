"""Main application"""
import sys

from PyQt5.QtWidgets import (
    QApplication,
    QGridLayout,
    QMainWindow,
    QTextBrowser,
    QWidget,
)

from components.dump_button import DumpButton
from components.toolbar import NavigationBar
from components.viewer import ViewTree
from storage import init_storage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MMEditor")
        self.resize(1200, 800)

        self.toolbar = NavigationBar()
        self.addToolBar(self.toolbar)

        layout = QGridLayout()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.informant = QTextBrowser()
        self.informant.setText("""<p>Attribute information will display here</p>""")
        layout.addWidget(self.informant, 0, 1, 1, 1)

        self.viewer = ViewTree(self.informant, None)
        layout.addWidget(self.viewer, 0, 0, 3, 1)

        self.brower = QTextBrowser()
        self.brower.setText(
            """<p>YAML will dump here after clicking 'Dump' button</p>"""
        )
        layout.addWidget(self.brower, 1, 1, 1, 1)

        convert = DumpButton(self.brower)
        layout.addWidget(convert, 2, 1, 1, 1)


if __name__ == "__main__":
    init_storage()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

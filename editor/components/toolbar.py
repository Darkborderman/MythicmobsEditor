from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLabel, QMenu, QPushButton, QToolBar

from components.viewer import ViewTree
from storage import STORAGE, set_focused_item, get_focused_item


class NavigationBar(QToolBar):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Currently:")
        for category in [
            "DropTables",
            "Enchantments",
            "Items",
            "Mobs",
            "RandomSpawns",
            "Skills",
        ]:
            button = SelectButton(category)
            self.addWidget(button)
        self.addWidget(self.label)


class SelectButton(QPushButton):

    category: str
    update_signal = pyqtSignal()

    def __init__(self, category: str):
        super().__init__()
        self.category = category
        self.setText(category)

        menu = QMenu()
        menu.text = category
        for item in STORAGE[category]:
            menu.addAction(item.unique_id)
        menu.triggered.connect(self.update_focused_item)

        self.setMenu(menu)

    def update_focused_item(self, action):
        self.update_signal.emit()
        set_focused_item(self.category, action.text())
        self.parentWidget().label.setText(
            f"Currently: {self.category}>{action.text()} "
        )
        viewer: ViewTree = self.parentWidget().parentWidget().viewer
        viewer.clear()
        viewer.fill_item(
            viewer.invisibleRootItem(), get_focused_item()
        )

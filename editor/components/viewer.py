from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTextBrowser, QTreeWidget, QTreeWidgetItem
from classes.skill import MythicSkill

class ViewItem(QTreeWidgetItem):

    description = ""

    def __init__(self, text: str, description=""):
        super().__init__([text])
        self.description = description


class ViewTree(QTreeWidget):
    def render_browser(self, *args):
        print(args)
        print(args[0].text(0))
        print(args[0].description)
        self.browser.setText(args[0].description)

    def __init__(self, browser: QTextBrowser, data):
        self.browser = browser
        super().__init__()
        self.setHeaderHidden(True)
        self.setMouseTracking(True)
        self.fill_item(self.invisibleRootItem(), data)

        self.itemClicked.connect(self.render_browser)
        # this should used to update storage
        # self.itemChanged.connect(self.render_browser)

    def add_view_item(self, parent, name, desc):
        child = ViewItem(name, desc)
        parent.addChild(child)
        return child

    def new_item(self, parent, text, val=None):
        child = ViewItem(text)
        child.setFlags(child.flags() | Qt.ItemIsEditable)
        self.fill_item(child, val)
        parent.addChild(child)

    def fill_item(self, item, value):
        if value is None:
            return
        if isinstance(value, MythicSkill):
            for attribute in value.get_attributes():
                child = self.add_view_item(
                    item,
                    value.get_name(attribute),
                    value.get_desc(attribute)
                )
                data = getattr(value, attribute)
                if isinstance(data, (list, tuple)):
                    for val in data:
                        self.new_item(child, val)
                if isinstance(data, dict):
                    for key, val in value.items():
                        self.new_item(item, str(key), val)
                else:
                    self.new_item(child, str(data))
            # print(item)
        # print(value.__dict__)
        # if isinstance(value, dict):
        #     for key, val in value.items():
        #         self.new_item(item, str(key), val)
        # elif isinstance(value, (list, tuple)):
        #     for val in value:
        #         if not isinstance(val, (dict, list, tuple)):
        #             text = str(val)
        #         else:
        #             text = "[%s]" % type(val).__name__
        #         self.new_item(item, text)
        # else:
        #     self.new_item(item, str(value))

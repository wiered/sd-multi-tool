from PySide6.QtWidgets import QListWidget, QListWidgetItem
from PySide6.QtCore import QRect
from PySide6.QtGui import QFont

from core import StylesList, Style, Category
from core import write_csv, read_csv

styelsheet = """QAbstractScrollArea {
	padding: 5px 5px 5px 0;
	border-radius: 7px;
}

QScrollBar::vertical {
    border: 0px solid rgba(50, 50, 70, 1);
    background: rgba(50, 50, 70, 1);
    width: 10px;
	border-radius: 20px;
}

QScrollBar::handle:vertical {
    background: #6464A0;
	border-radius: 4px;
    min-height: 0px;
}

QScrollBar::add-line:vertical {
    border: 0px solid grey;
    background: rgba(50, 50, 70, 1);
    height: 0px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:vertical {
    border: 0px solid grey;
    background: rgba(50, 50, 70, 1);
    height: 0px;
    subcontrol-position: top;
    subcontrol-origin: margin;
}
QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
    border: 0px solid grey;
    width: 0px;
    height: 0px;
    background: rgba(50, 50, 70, 1);
}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    background: none;
}"""

class StylesListWidget(QListWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.current_stylename = ""
        self.current_filename = ""
        self.search_query = ""
        self.styles_list: StylesList = StylesList()
        font = QFont()
        font.setFamilies([u"JetBrains Mono NL"])
        self.setFont(font)


    def get_current_style(self) -> Style:
        """Get current style

        Returns:
            Style: current style
        """
        return self.styles_list.find_by_name(self.current_stylename)
    

    def add_style(self, name: str, prompt: str, negative_prompt: str):
        """Add a style to the list

        Args:
            name (str): style name
            prompt (str): style prompt
            negative_prompt (str): style negative prompt
        """
        self.styles_list.append(Style([name, prompt, negative_prompt]))
    

    def pop(self):
        """Pop style from styles list
        """
        self.styles_list.remove(self.current_stylename)

    
    def clear_data(self):
        """Clear self, styles_list and current style
        """
        self.current_stylename = ""
        self.clear()
        self.styles_list.clear()
    

    def add_styles_from_styles_list(self):
        """Adding styles from StyleList to QListWidget(self)
        """
        for category in self.styles_list.categories:
            total = 0
            for style in category._styles:
                if self.search_query.lower() in style.name.lower():
                    total += 1
                    break
            
            if total > 0:
                self.addItem(category._name)
                for style in category._styles:
                    if self.search_query.lower() in style.name.lower():
                        self.addItem(style.name)

    
    def reload(self):
        """reload ui, styles_list and current style
        """
        self.clear_data()
        self.styles_list.read_from_csv(self.current_filename)
        self.add_styles_from_styles_list()


    def select_style(self, style: QListWidgetItem, properties: list):
        """Select style from QListWidget(self)

        Args:
            style (QListWidgetItem): Style Item in QListWidget(self)
            properties (list): Properties of previous Style
            properties[0]: name
            properties[1]: prompt
            properties[2]: negative prompt

        Returns:
            _type_: _description_
        """
        try:
            style_name = style.text()
        except:
            return "", "", ""

        if not self.styles_list:
            return "", "", ""

        if not self.styles_list.is_style_exists(style_name):
            return "", "", ""
        
        self.styles_list.save_style(*properties)

        self.current_stylename = style_name
        style: Style = self.styles_list.find_by_name(self.current_stylename)

        return style.name, style.prompt, style.negative_prompt
        

    def set_parent_window(self, parent):
        """set parent window

        Args:
            parent: parent window
        """
        self.parent_window = parent
        self.setStyleSheet(styelsheet)
        self.setGeometry(QRect(0, 0, 291, 631))


    def dragEnterEvent(self, event):
        """Accpeting drag and drop events"""
        event.accept()


    def dropEvent(self, event):
        """Drop event. Loads .csv file to widget

        Args:
            event (QEvent)
            event.mimeData (QMimeData): https://doc.qt.io/qtforpython-6/PySide6/QtCore/QMimeData.html#qmimedata
        """
        mimedata = event.mimeData()
        if not mimedata.hasText():
            return
        
        filename = mimedata.text()[8:]
        
        if ".csv" in filename:
            self.current_filename = filename
            self.clear_data()
            self.styles_list.read_from_csv(self.current_filename)
            self.add_styles_from_styles_list()


    def dragMoveEvent(self, event):
        pass
        
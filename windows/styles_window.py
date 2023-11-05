from PySide6.QtWidgets import (
    QAbstractItemView, QDialog,
    )

from windows import (
    Ui_StylesEditor, Ui_NewStyleDialog, 
    )
from widgets import (
    StylesListWidget
)
from core import write_csv

class StylesEditorDialog(QDialog):
    def __init__(self):
        super(StylesEditorDialog, self).__init__()
        self.ui = Ui_StylesEditor()
        self.ui.setupUi(self)

        self.styles_list_widget: StylesListWidget = StylesListWidget(self.ui.styles_widget)

        self.styles_list_widget.currentItemChanged.connect(self.select_style)
        self.styles_list_widget.addItem("Drag and drop styles.csv here")
        self.styles_list_widget.set_parent_window(self)
        self.styles_list_widget.setDragDropMode(QAbstractItemView.DragDrop)

        self.ui.search_bar.textChanged.connect(self.search_bar_changed)

        self.ui.add_button.clicked.connect(self.open_style_editor)
        self.ui.copy_button.clicked.connect(self.copy_button_clicked)
        self.ui.delete_button.clicked.connect(self.delete_button_clicked)
        self.ui.refresh_button.clicked.connect(self.refresh_button_clicked)
        
        self.ui.save_button.clicked.connect(self.save_button_clicked)
    

    def clear_ui(self):
        # clears ui
        self.ui.style_name.setPlainText("")
        self.ui.prompt.setPlainText("")
        self.ui.negative_prompt.setPlainText("")


    def parse_properties(self) -> list:
        name = self.ui.style_name.toPlainText()
        prompt = self.ui.prompt.toPlainText()
        negative_prompt = self.ui.negative_prompt.toPlainText()
        return [name, prompt, negative_prompt]


    def set_properties(self, name, prompt, negative_prompt):
        self.ui.style_name.setPlainText(name)
        self.ui.prompt.setPlainText(prompt)
        self.ui.negative_prompt.setPlainText(negative_prompt)


    def select_style(self, style, properties):
        style = self.styles_list_widget.select_style(style, self.parse_properties())
        self.set_properties(*style)


    def open_style_editor(self):
        self.style_editor_window = QDialog()
        self.style_editor = Ui_NewStyleDialog()

        self.style_editor.setupUi(self.style_editor_window)
        self.style_editor.save_button.clicked.connect(self.add_style_button_clicked)
        self.style_editor_window.show()


    def add_style_button_clicked(self):
        name = self.style_editor.style_name.toPlainText()
        prompt = self.style_editor.prompt.toPlainText()
        negative_prompt = self.style_editor.negative_prompt.toPlainText()

        self.styles_list_widget.add_style(name, prompt, negative_prompt)
        self.styles_list_widget.clear()
        self.styles_list_widget.add_styles_from_styles_list()
        self.style_editor_window.close()


    def copy_button_clicked(self):
        if not self.styles_list_widget.current_stylename:
            return
        
        self.open_style_editor()
        style = self.styles_list_widget.get_current_style()
        self.style_editor.style_name.setPlainText(style.name)
        self.style_editor.prompt.setPlainText(style.prompt)
        self.style_editor.negative_prompt.setPlainText(style.negative_prompt)

    
    def delete_button_clicked(self):
        self.styles_list_widget.pop()
        self.clear_ui()
        self.styles_list_widget.clear()
        self.styles_list_widget.add_styles_from_styles_list()

    
    def refresh_button_clicked(self):
        self.clear_ui()
        self.styles_list_widget.reload()
    

    def save_button_clicked(self):
        self.styles_list_widget.styles_list.save_style(*self.parse_properties())
        write_csv(
            self.styles_list_widget.current_filename, 
            self.styles_list_widget.styles_list
            )

    
    def search_bar_changed(self):
        self.styles_list_widget.search_query = self.ui.search_bar.toPlainText()
        self.clear_ui()
        self.styles_list_widget.clear()
        self.styles_list_widget.add_styles_from_styles_list()

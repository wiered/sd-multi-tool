from PySide6.QtCore import Qt, QResource, QMimeData
from PySide6.QtGui import QPixmap, QImage, QDrag, QPixmap, QPainter, QCursor
from PySide6.QtWidgets import QGraphicsScene, QLabel, QApplication

from core import ImageDataReader

class ImageScene(QGraphicsScene):
    def set_parent_window(self, parent):
        self.parent_window = parent


    def set_image(self, image_filename: str):
        """set image

        Args:
            image_filename (str): path to the image file
        """
        self.image_filename = image_filename
        self.image_pixmap = QPixmap(self.image_filename)
        self.addPixmap(self.image_pixmap.scaled(512, 512, Qt.KeepAspectRatio))


    def dragEnterEvent(self, e):
        e.accept()


    def dropEvent(self, e):
        """Drop event. Loads .csv file to widget

        Args:
            event (QEvent)
            event.mimeData (QMimeData): https://doc.qt.io/qtforpython-6/PySide6/QtCore/QMimeData.html#qmimedata
        """
        mimedata = e.mimeData()
        if not mimedata.hasText():
            return
        
        if ".png" in mimedata.text():
            self.image_filename = mimedata.text()[8:]
            resource = QResource(self.image_filename)
            image = QImage(self.image_filename)
            self.clear()
            image_pixmap = QPixmap(image)
            self.addPixmap(image_pixmap.scaled(512, 512, Qt.KeepAspectRatio))
            

            image_reader = ImageDataReader(self.image_filename)
            self.parent_window.prompt.setPlainText(image_reader.positive)
            self.parent_window.negative_prompt.setPlainText(image_reader.negative)
            self.parent_window.settings.setPlainText(image_reader.setting.replace(", ", "\n"))
    

    def dragMoveEvent(self, e):
        ...
        
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from UI.loadSyllabusWindow import Ui_loadSyllabusWindow
import sys
import logging
from datetime import datetime
from excel_reader import ExcelReader
from word import FillTemplate
import os


def exception_hook(exc_type, exc_value, exc_traceback):
    logging.error(
        "Uncaught exception",
        exc_info=(exc_type, exc_value, exc_traceback)
    )
    sys.exit()


def set_up_logger():
    try:
        os.mkdir('Log')
    except Exception as e:
        print(e)
    date_time_obj = datetime.now()
    timestamp_str = date_time_obj.strftime("%d-%b-%Y_%H_%M_%S")
    filename = './Log/crash-{}.log'.format(timestamp_str)
    logging.basicConfig(filename=filename)
    sys.excepthook = exception_hook


class Window1(QWidget, Ui_loadSyllabusWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.choose_file)
        self.db_path = self.path_label.text()
        self.nextButton.clicked.connect(self.read_file)
        self.nextButton.clicked.connect(self.hide)

    def choose_file(self):
        file_name = QFileDialog.getOpenFileName(self, 'Выберите файл...', '', 'Excel file (*.xlsx)')
        self.path_label.setText(file_name[0])
        self.db_path = file_name[0]

    def read_file(self):
        file = ExcelReader(self.db_path)
        filler = FillTemplate(file.read())
        filler.fill_words()


def main():
    set_up_logger()

    app = QApplication(sys.argv)

    window1 = Window1()
    window1.show()
    window1.nextButton.clicked.connect(app.exit)
    app.exec()


if __name__ == "__main__":
    main()

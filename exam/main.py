from PySide6 import QtWidgets
import datetime

from Notes import Ui_MainWindow


class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_signals()
        self.unsaved = False
        self.notes_dict = {}
        self.last = None
        self.lastIndex = 0
        self.file = {
            "notes_dict": self.notes_dict,
            "last": self.last
        }

    def init_signals(self):
        self.ui.plainTextEdit.textChanged.connect(lambda: self.note_changed())
        self.ui.plainTextEdit_2.textChanged.connect(lambda: self.note_changed())
        self.ui.pushButton.clicked.connect(lambda: self.save_changes())
        self.ui.pushButton_2.clicked.connect(lambda: self.new_note())
        self.ui.progressBar.setMaximum(100)

    def new_note(self):

        self.ui.plainTextEdit.setPlainText("")
        self.ui.plainTextEdit_2.setPlainText("")
        self.ui.dateTimeEdit.setDateTime(datetime.datetime.now())

    def save_changes(self):

        if self.get_note_title() not in list(self.notes_dict.keys()):
            time_now = datetime.datetime.now()
            current_date_seconds_from_start = time_now.timestamp()
            current_date = str(time_now.strftime("%H:%M %d.%m.%Y"))

            if self.get_note_title().strip() == "":
                self.notes_dict["untitled"] = {
                    "title": self.get_note_title(),
                    "date": current_date,
                    "text": self.get_note_text(),
                    "date_to_seconds": current_date_seconds_from_start,
                    "due_date": self.get_due_date()
                }
            else:
                self.notes_dict[self.get_note_title()] = {
                    "title": self.get_note_title(),
                    "date": current_date,
                    "text": self.get_note_text(),
                    "date_to_seconds": current_date_seconds_from_start,
                    "due_date": self.get_due_date()
                }
        else:
            time_now = datetime.datetime.now()
            current_date_seconds_from_start = time_now.timestamp()
            current_date = str(time_now.strftime("%H:%M %d.%m.%Y"))
            self.notes_dict[self.get_note_title()] = {
                "title": self.get_note_title(),
                "date": current_date,
                "text": self.get_note_text(),
                "date_to_seconds": current_date_seconds_from_start,
                "due_date": self.get_due_date()
            }

        self.ui.pushButton.setDisabled(True)

    def note_changed(self):

        if self.get_note_title().strip() == "":
            self.ui.pushButton.setDisabled(True)
        else:
            self.ui.pushButton.setEnabled(True)

    def get_note_title(self):
        return str(self.ui.plainTextEdit.toPlainText())

    def get_note_text(self):
        return self.ui.plainTextEdit_2.toPlainText()

    def get_due_date(self):
        return self.ui.dateTimeEdit.text()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()

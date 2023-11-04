import sys
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QStatusBar,
    QToolBar,
    QMainWindow,
    QGridLayout,
    QLineEdit,
    QWidgetItem,
    QLayoutItem,
    QSizePolicy,
    QCalendarWidget
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from functools import partial
import os

WINDOW_SIZE = 250
DISPLAY_HEIGHT = 35
BUTTON_SIZE = 200



class Window(QMainWindow):
    def __init__(self):
        super().__init__(parent=None,)
        self.setWindowTitle("Osheas Poker Points System")
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)
        self.generalLayout = QVBoxLayout()
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        self._addMainMenuPicture()
        self._createDisplay()
        self._mainMenuButtons()
        self._dynamicResizeWindows()

    def _createDisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(DISPLAY_HEIGHT)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)

    def _mainMenuButtons(self):
        self.buttonMap = {}
        buttonsLayout = QVBoxLayout()
        options = ["Create a New Game",
                   "Modify an Existing Game",
                   "Add a New Player",
                   "View/Modify Existing Players",
                   "Create a New Season"
                   ]

        for keys in options:
            self.buttonMap[keys] = QPushButton(keys)
            buttonsLayout.addWidget(self.buttonMap[keys])

        self.generalLayout.addLayout(buttonsLayout)

    def _addMainMenuPicture(self, picture: str = "picture.jpeg") -> None:
        picture_label = QLabel(self)
        Path = os.path.join(".", "pictures", "Logo_small.jpg")
        pixmap = QPixmap(Path)
        picture_label.setPixmap(pixmap)
        self.generalLayout.addWidget(picture_label)

    def clearWindows(self):
        """ Empties the windows and clears all objects in reverse order.
        Reverse order is required for inhereted objects.
        """
        for i in reversed(range(self.generalLayout.count())):
            item = self.generalLayout.itemAt(i)
            if isinstance(item, QWidgetItem):
                item.widget().deleteLater()
            elif isinstance(item, QLayoutItem):
                sublayout = item.layout()
                for j in reversed(range(sublayout.count())):
                    subitem = sublayout.itemAt(j)
                    subitem.widget().deleteLater()
                sublayout.deleteLater()

    def _dynamicResizeWindows(self) -> None:
        self.adjustSize()   # Automatically resize the window

        # Adjust window size policy
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setMinimumSize(self.sizeHint())
        self.setMaximumSize(self.sizeHint())

    def _addCalendar(self):
        calendar = QCalendarWidget(self)
        calendar.clicked.connect(self._onDateSelected)
        self.generalLayout.addWidget(calendar)

    def _onDateSelected(self, date):
        selected_date = date.toString("yyyy-MM-dd")
        print(f"Selected date: {selected_date}")
        # Do something with the selected date

    def _createButtons(self):
        self.buttonMap["Select Date"] = QPushButton("Select Date")
        self.buttonMap["Select Date"].clicked.connect(self._addCalendar)
        buttonsLayout.addWidget(self.buttonMap["Select Date"])

    def _createNewGameWindow(self):
        self._addCalendar()
        self._createButtons()


class Operations():

    def __init__(self, view):
        self._view = view
        self._connectSignalsAndSlots()

    def redirectToNewWindow(self, buttonName):
        match buttonName:
            case "Create a New Game":
                self._view.clearWindows()
                self._view._addMainMenuPicture()
                self._view._createNewGameWindow()
            case "Modify an Existing Game":
                self._view.clearWindows()
            case "Add a New Player":
                pass
            case "View/Modify Existing Players":
                pass
            case "Create a New Season":
                pass
            case _:
                pass

    def _connectSignalsAndSlots(self):
        for keySymbol, button in self._view.buttonMap.items():
            button.clicked.connect(partial(self.redirectToNewWindow, keySymbol))


def main():
    """PokerApp's main function."""
    pokerApp = QApplication([])
    pokerWindow = Window()
    pokerWindow.show()
    Operations(view=pokerWindow)
    sys.exit(pokerApp.exec())


if __name__ == "__main__":
    main()

import sys
import os
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QMainWindow,
    QLineEdit,
    QSizePolicy,
    QCalendarWidget,
    QComboBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from functools import partial

WINDOW_SIZE = 250
DISPLAY_HEIGHT = 35
BUTTON_SIZE = 200


class Window(QMainWindow):
    seasonDropdown = None  # Class variable to store the season dropdown widget

    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("Osheas Poker Points System")
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)
        self.generalLayout = QVBoxLayout()
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        self._addMainMenuPicture()
        self._addSeasonDropdown()
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
        options = [
            "Create a New Game",
            "Modify an Existing Game",
            "Add a New Player",
            "View/Modify Existing Players",
            "Create a New Season"
        ]

        for keys in options:
            button = QPushButton(keys)
            button.clicked.connect(partial(self._redirect, keys))
            self.buttonMap[keys] = button
            self.generalLayout.addWidget(button)

    def _addMainMenuPicture(self, picture: str = "picture.jpeg") -> None:
        picture_label = QLabel(self)
        path = os.path.join(".", "pictures", "Logo_small.jpg")
        pixmap = QPixmap(path)
        picture_label.setPixmap(pixmap)
        self.generalLayout.addWidget(picture_label)

    def clearWindows(self):
        while self.generalLayout.count() > 0:
            item = self.generalLayout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

    def _dynamicResizeWindows(self) -> None:
        self.adjustSize()  # Automatically resize the window
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setMinimumSize(self.sizeHint())
        self.setMaximumSize(self.sizeHint())

    def _redirect(self, buttonName):
        match buttonName:
            case "Create a New Game":
                self.clearWindows()
                self._addMainMenuPicture()
                self._addCalendar()
                # self._createButtons()
            case "Modify an Existing Game":
                self.clearWindows()
                # Add code for modifying existing game
            case "Add a New Player":
                self.clearWindows()
                # Add code for adding a new player
            case "View/Modify Existing Players":
                self.clearWindows()
                # Add code for viewing/modifying existing players
            case "Create a New Season":
                self.clearWindows()
                # Add code for creating a new season
            case _:
                pass

    def _addCalendar(self):
        calendar = QCalendarWidget(self)
        calendar.clicked.connect(self._onDateSelected)
        self.generalLayout.addWidget(calendar)

    def _onDateSelected(self, date):
        selected_date = date.toString("yyyy-MM-dd")
        print(f"Selected date: {selected_date}")
        # Do something with the selected date

    def _addSeasonDropdown(self):
        "Add a season drop down, prefering the most recent season to be the default"
        season_files = self.list_season_files()
        sorted_season_files = sorted(season_files, key=lambda x: int(x.replace('season', '')), reverse=True)

        if sorted_season_files:
            self.seasonDropdown = QComboBox()
            self.seasonDropdown.addItems(sorted_season_files)
            self.generalLayout.addWidget(self.seasonDropdown)

    def list_season_files(self):
        data_folder = "./data"
        season_files = []

        for file_name in os.listdir(data_folder):
            if "season" in file_name.lower():
                season_files.append(file_name.strip(".db"))

        return season_files


def main():
    """PokerApp's main function."""
    pokerApp = QApplication([])
    pokerWindow = Window()
    pokerWindow.show()
    # Operations(view=pokerWindow)
    sys.exit(pokerApp.exec())


if __name__ == "__main__":
    main()

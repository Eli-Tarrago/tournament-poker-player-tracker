import sqlite3
from datetime import date
import os


class createDBFirstTime():
    def createPlayersDB(self, databaseName: str = "players"):
        Path = os.path.join(".", "data", f"{databaseName}.db")
        con = sqlite3.connect(Path)
        cur = con.cursor()
        cur.execute("CREATE TABLE athlete(fName, lName, emailAddress)")

    def createNewGame(self, seasonName: str = "tournament", seasonDate: str = "20691201"):
        Path = os.path.join(".", "data", f"{seasonName}.db")
        con = sqlite3.connect(Path)
        cur = con.cursor()

        # Convert date to Month first because I cannot create a table name with a number
        # 12012069 is bad, Dec012069 works fine :/

        d = date.fromisoformat(seasonDate).strftime("%b%d%Y")

        cur.execute(f"CREATE TABLE {d}(fName, lName, pointValue, main, cons, bounty, gameNumber)")


if __name__ == "__main__":
    db = createDBFirstTime()
    db.createPlayersDB()
    db.createNewGame()

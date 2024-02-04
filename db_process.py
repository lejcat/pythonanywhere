import pandas as pd
import sqlite3

# Read csv file.
df = pd.read_csv("AparchesMMDList.csv")

# Connect to (create) database.
database = "db.sqlite3"
conn = sqlite3.connect(database)
dtype={
    "Index": "IntegerField",
    "Title": "CharField",
    "TitleEng": "CharField", 
    "Artist": "CharField",
    "Cover": "CharField",
    "Type": "CharField",
    "Player": "IntegerField",
    "Motion": "CharField",
    "MotionEdited": "BooleanField",
    "Facial": "CharField",
    "Lipsync": "CharField",
    "Camera": "CharField",
    "CameraEdited": "BooleanField"
}
df.to_sql(name='mmdlist_mmdinfo', con=conn, if_exists='replace', dtype=dtype, index=True, index_label="id")

query1 = "UPDATE mmdlist_mmdinfo SET MotionEdited=False WHERE MotionEdited IS NULL"
query2 = "UPDATE mmdlist_mmdinfo SET CameraEdited=False WHERE CameraEdited IS NULL"

conn.execute(query1)
conn.execute(query2)
conn.commit()

conn.close()
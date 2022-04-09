import sqlite3
import os

class DB():

    def __init__(self):
        self.connect_database()
        self.cur.execute('''DROP TABLE IF EXISTS DICTS;''')
        self.cur.execute('''CREATE TABLE IF NOT EXISTS "DICTS" (
                "Name"	TEXT NOT NULL,
                "Is_Preset"	BOOLEAN NOT NULL,
                PRIMARY KEY("Name")
                );''')
        
        for dictname in list(PRESETDICTS):
            self.cur.execute("INSERT INTO DICTS ('Name', 'Is_Preset') VALUES\n('{}', 'TRUE')".format(dictname))
        
            self.cur.execute('DROP TABLE IF EXISTS "{}";'.format(dictname))
        
            command = '''CREATE TABLE "{}" (
                    "Word"	TEXT NOT NULL,
                    "Definition"	TEXT NOT NULL,
                    PRIMARY KEY("Word")
                    );'''.format(dictname)
            self.cur.execute(command)

            for word in list(PRESETDICTS[dictname]):
                self.cur.execute('''INSERT OR REPLACE INTO \'''' + dictname + '''' ('Word', 'Definition') VALUES''' + '''
                        ('{}', '{}')'''.format(word, PRESETDICTS[dictname][word]))

        self.close_database()

    def connect_database(self):
        # connection
        self.conn = sqlite3.connect(os.path.abspath('./CCT211-SpellWell/db/spellwell_db'))
        # cursor
        self.cur = self.conn.cursor()

    def close_database(self):
        self.conn.commit()
        self.conn.close()

    def getDict(self, name):
        self.connect_database()
        self.cur.execute("SELECT * FROM 'DICTS'")
        rows = self.cur.fetchall()
        self.cur.execute("SELECT * FROM 'animals'")
        rows = self.cur.fetchall()
        self.cur.execute("SELECT * FROM \'{}\'".format(name))
        rows = self.cur.fetchall()
        dictionary = {}
        for row in rows:
            word = row[0]
            definition = row[1]
            dictionary[word] = definition
        self.close_database()
        return dictionary 

PRESETDICTS = {"animals":{"cat": "best animal that meows", 
                    "dog": "best animal that barks",
                    "giraffe": "very tall animal", 
                    "unicorn": "magical animal(?)"},

            "body": {"nose": "the body part you use to smell", 
                "mouth": "the body part you use to speak",
                "teeth": "the body parts you use to chew your food", 
                "legs": "the body parts you use to walk or run", 
                "hands": "the body parts you use to write or type"},

        "polygons": {"triangle": "the polygon that has three sides", 
                    "quadrilateral": "the polygon that has four sides",
                    "pentagon": "the polygon that has five sides", 
                    "hexagon": "the polygon that has six sides", 
                    "heptagon": "the polygon that has seven sides"},
    
        "medical": {"doctor": "a qualified practitioner of medicine", 
                    "stethoscope": "a medical instrument for listening to the heartbeat",
                    "surgical mask": "a mask work in surgery", 
                    "surgical gown": "something a surgeon wears during surgery", 
                    "gloves": "worn on hands by surgeons"},
    
        "numbers": {"one": "the number 1", 
                    "one hundred": "the number 100",
                    "five hundred": "the number 500", 
                    "one thousand": "the number 1000", 
                    "two thousand": "the number 2000"}}
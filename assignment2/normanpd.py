import sqlite3

conn = sqlite3.connect('normanpd.db')

conn.execute('''CREATE TABLE IF NOT EXISTS incidents (
    incident_time TEXT,
    incident_number TEXT,
    incident_location TEXT,
    nature TEXT,
    incident_ori TEXT
);''')

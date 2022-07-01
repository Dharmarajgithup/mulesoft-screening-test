import sqlite3
connection = sqlite3.connect('shows.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Movies
              (MovieName TEXT,Actor TEXT,Actress TEXT, Year INT,Director TEXT)''')
cursor.execute('''INSERT INTO Movies  VALUES ('bigil', 'Vijay', 'Rashmika Mandanna', 2023,'Vamshi Paidipally' )''')
cursor.execute('''INSERT INTO Movies VALUES ('Asuran', 'Dhanush', 'Manju Warrier', 2019,'Vetrimaran' )''')
cursor.execute('''INSERT INTO Movies VALUES ('Ayan', 'Surya', 'Tamana Bhatia','2009,'K V Anand' )''')
cursor.execute('''INSERT INTO Movies VALUES ('Beast', 'Vijay', 'Pooja Hegde', 2022,'Nelson' )''')
cursor.execute('''SELECT * from Movies''')
cursor.execute("SELECT * from Movies where Actor='Surya'")
result = cursor.fetchall();
print(result)
connection.commit()
connection.close()

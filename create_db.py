import sqlite3

connection = sqlite3.connect('db/database.db')

cur = connection.cursor()

cur.execute('''
        CREATE TABLE IF NOT EXISTS client (
                client_id INTEGER PRIMARY KEY AUTOINCREMENT,
                telegram_id VARCHAR(50) NOT NULL,
                user_name_id INT,
                first_name VARCHAR (50),
                last_name VARCHAR (50),
                more_info TEXT,
                mobile_number VARCHAR (17),
                client_enabled BOOLEAN DEFAULT 1
        )
''')


cur.execute('''
        CREATE TABLE IF NOT EXISTS admin (
                admin_id INTEGER PRIMARY KEY AUTOINCREMENT,
                telegram_id VARCHAR(50) NOT NULL,
                user_name_id INT,
                first_name VARCHAR (50),
                last_name VARCHAR (50),
                more_info TEXT,
                mobile_number VARCHAR (17),
                admin_enabled BOOLEAN DEFAULT 1,
                level_add_client BOOLEAN DEFAULT 0,
                level_add_region BOOLEAN DEFAULT 0,
                level_add_data BOOLEAN DEFAULT 0,
                level_add_admin BOOLEAN DEFAULT 0,
                level_send BOOLEAN DEFAULT 0,
                date_registered TEXT NOT NULL
        );
            ''')

cur.execute('''
        CREATE TABLE IF NOT EXISTS region (
                region_id INTEGER PRIMARY KEY AUTOINCREMENT,
                blame_admin INTEGER NOT NULL,
                region_name VARCHAR (50) NOT NULL,
                more_info TEXT,
                date_added TEXT NOT NULL,
                region_enabled BOOLEAN DEFAULT 1,

                FOREIGN KEY (blame_admin) REFERENCES admin (admin_id)
        );
''')

cur.execute('''
        CREATE TABLE IF NOT EXISTS data_file (
                data_id INTEGER PRIMARY KEY AUTOINCREMENT,
                data_name VARCHAR(50),
                type VAHCHAR(80),
                data_file_path TEXT,
                more_info TEXT,
                data_enabled BOOLEAN DEFAULT 1
        );
''')


# LINK TABLE
cur.execute('''
        CREATE TABLE IF NOT EXISTS enrollment_lt (
                client_id INT NOT NULL,
                region_id INT NOT NULL,
                blame_admin INT NOT NULL,
                date_enrollment TEXT NOT NULL,
                client_region_enabled BOOLEAN DEFAULT 1,
            
                PRIMARY KEY (client_id, region_id),
                FOREIGN KEY (client_id) REFERENCES client (client_id),
                FOREIGN KEY (region_id) REFERENCES region (region_id),
                FOREIGN KEY (blame_admin) REFERENCES admin (admin_id)
        );
''')

cur.execute('''        
        CREATE TABLE IF NOT EXISTS reg_data_lt (
                region_id INT NOT NULL, 
                data_id INT NOT NULL,
                blame_admin INT NOT NULL,
                date_added TEXT NOT NULL,
                region_data_enabled BOOLEAN DEFAULT 1,
            
                PRIMARY KEY (region_id, data_id),
                FOREIGN KEY (region_id) REFERENCES region (region_id),
                FOREIGN KEY (data_id) REFERENCES data_file (data_id),
                FOREIGN KEY (blame_admin) REFERENCES admin (admin_id)
        );
''')


print('database created')
cur.close()
connection.close()

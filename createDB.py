import sqlite3
import pandas as pd

# Connects to an existing database file in the current directory
# If the file does not exist, it creates it in the current directory
db_connect = sqlite3.connect('PawsomePets.db')

# Instantiate cursor object for executing queries
cursor = db_connect.cursor()

# Create Clinic table without FK because SQLite doesn't allow adding a FK using ALTER TABLE - this will be discarded later
query = """
   CREATE TABLE IF NOT EXISTS Clinic ( 
        clinicNo    varchar(10) NOT NULL, 
        name    varchar(200) NOT NULL, 
        address varchar(200) NOT NULL, 
        telephoneNo varchar(10) NOT NULL,
        PRIMARY KEY (clinicNo)
    );
    """
cursor.execute(query)

# Create Staff table
query = """
    CREATE TABLE IF NOT EXISTS Staff (   
        staffNo varchar(10) NOT NULL,   
        name    varchar(200) NOT NULL,   
        address varchar(200) NOT NULL,   
        telephoneNo varchar(10) NOT NULL,   
        DOB DATE NOT NULL,  
        position varchar(200) CHECK (position in ('Vet', 'Technician', 'Manager', 'Assistant', 'Receptionist', 'Janitor')),  
        salary int NOT NULL,
        clinicNo 	varchar(10) NOT NULL, 
        FOREIGN KEY (clinicNo) REFERENCES Clinic (clinicNo), 
        PRIMARY KEY (staffNo)
    );
    """
cursor.execute(query)

# Delete OldClinic table if it already exists in order to add foreign key to Clinic table
query = """
    DROP TABLE OldClinic;
    """
cursor.execute(query)

query = """
    ALTER TABLE Clinic RENAME TO OldClinic;
    """
cursor.execute(query)

# Create new Clinic table with staffNo FK now that Staff table exists
query = """
    CREATE TABLE IF NOT EXISTS Clinic ( 
        clinicNo    varchar(10) NOT NULL, 
        name    varchar(200) NOT NULL, 
        address varchar(200) NOT NULL, 
        telephoneNo varchar(10) NOT NULL,
        staffNo varchar(10) NOT NULL,
        FOREIGN KEY (staffNo) REFERENCES Staff (staffNo),
        PRIMARY KEY (clinicNo)
    );
    """
cursor.execute(query)

# Create PetOwner table
query = """
    CREATE TABLE IF NOT EXISTS PetOwner (   
        ownerNo varchar(10) NOT NULL,   
        name    varchar(200) NOT NULL,   
        address varchar(200) NOT NULL,   
        telephoneNo varchar(10) NOT NULL,   
        clinicNo    varchar(10) NOT NULL, 
        FOREIGN KEY (clinicNo) REFERENCES Clinic (clinicNo), 
        PRIMARY KEY (ownerNo)
    );
    """
cursor.execute(query)

# Create Pet table
query = """
    CREATE TABLE IF NOT EXISTS Pet (   
        petNo   varchar(10) NOT NULL,   
        name    varchar(200) NOT NULL,   
        DOB DATE NOT NULL,    
        species varchar(200) NOT NULL,
        breed   varchar(200) NOT NULL,
        color   varchar(200) NOT NULL,  
        ownerNo varchar(10) NOT NULL,
        clinicNo varchar(10) NOT NULL, 
        FOREIGN KEY (ownerNo) REFERENCES PetOwner (ownerNo), 
        FOREIGN KEY (clinicNo) REFERENCES Clinic (clinicNo), 
        PRIMARY KEY (petNo)
    );
    """
cursor.execute(query)

# Create Examination table
query = """
    CREATE TABLE IF NOT EXISTS Examination (   
        examNo   varchar(10) NOT NULL,   
        chiefComplaint    varchar(1000) NOT NULL,   
        description varchar(1000) NOT NULL,    
        dateSeen    DATE NOT NULL 
            CONSTRAINT time_check CHECK (dateSeen <= date()),
        actionsTaken    varchar(1000) NOT NULL, 
        staffNo varchar(10) NOT NULL,
        petNo varchar(10) NOT NULL, 
        FOREIGN KEY (staffNo) REFERENCES Staff (staffNo), 
        FOREIGN KEY (petNo) REFERENCES Pet (petNo), 
        PRIMARY KEY (examNo)
    );
    """
cursor.execute(query)

# Insert Clinic data
query = """
    INSERT INTO Clinic VALUES ('C001', 'Coral Gables', '1234 Ponce De Leon Blvd', '3054358934', 'S001');
    """
cursor.execute(query)
query = """
    INSERT INTO Clinic VALUES ('C002', 'Fort Lauderdale', '523 Las Olas Blvd', '7542369482', 'S002');
    """
cursor.execute(query)
query = """
    INSERT INTO Clinic VALUES ('C003', 'Hollywood', '500 Jefferson Street', '7542375632', 'S003');
    """
cursor.execute(query)
query = """
    INSERT INTO Clinic VALUES ('C004', 'Jacksonville', '945 Main Street', '9043782365', 'S004');
    """
cursor.execute(query)
query = """
    INSERT INTO Clinic VALUES ('C005', 'West Palm Beach', '256 Clematis Street', '5613678993', 'S005');
    """
cursor.execute(query)

# Insert Staff data
query = """
    INSERT INTO Staff VALUES ('S001', 'Michael Wright', '435 Old Town Road', '3053877743', '1990-12-21', 'Manager', 100000, 'C001');
    """
cursor.execute(query)
query = """
    INSERT INTO Staff VALUES ('S002', 'Larry Herd', '770 Sage Drive', '7543781125', '1992-03-09', 'Manager', 100000, 'C002');
    """
cursor.execute(query)
query = """
    INSERT INTO Staff VALUES ('S003', 'Rachel Gant', '509 Summerhouse Drive', '7543784323', '1995-10-27', 'Manager', 100000, 'C003');
    """
cursor.execute(query)
query = """
    INSERT INTO Staff VALUES ('S004', 'Andrew Bell', '3 Sugar Road', '9047877723', '1993-07-15', 'Manager', 100000, 'C004');
    """
cursor.execute(query)
query = """
    INSERT INTO Staff VALUES ('S005', 'Jackson Clark', '557 North Holly Street', '5611288983', '1997-02-18', 'Manager', 80000, 'C005');
    """
cursor.execute(query)
query = """
    INSERT INTO Staff VALUES ('S006', 'Jane Doe', '1000 Wood Cliff Lane', '7542843211', '1987-1-14', 'Vet', 125000, 'C003');
    """
cursor.execute(query)
query = """
    INSERT INTO Staff VALUES ('S007', 'Robert Small', '921 South West Road', '5614467822', '1999-11-02', 'Technician', 70000, 'C005');
    """
cursor.execute(query)
query = """
    INSERT INTO Staff VALUES ('S008', 'Bella Anker', 'Shady Meadow Street', '7541244568', '2001-03-31', 'Receptionist', 45000, 'C002');
    """
cursor.execute(query)
query = """
    INSERT INTO Staff VALUES ('S009', 'Frank Simon', '289 Shore Ave', '3054782745', '1986-04-10', 'Janitor', 35000, 'C001');
    """
cursor.execute(query)
query = """
    INSERT INTO Staff VALUES ('S010', 'Jennifer Dixon', '8932 Norfolk Drive', '9049023364', '1995-12-26', 'Assistant', 60000, 'C004');
    """
cursor.execute(query)
query = """
    INSERT INTO Staff VALUES ('S011', 'Noah Stevens', '357 Oklahoma Street', '3056298037', '1997-02-18', 'Technician', 70000, 'C001');
    """
cursor.execute(query)
query = """
    INSERT INTO Staff VALUES ('S012', 'Carole Harrington', '11 South Devon Ave', '7547889657', '1998-06-22', 'Technician', 70000, 'C003');
    """
cursor.execute(query)
query = """
    INSERT INTO Staff VALUES ('S013', 'Traci Reyes', '758 Boston Rd', '7545441537', '2000-03-10', 'Technician', 70000, 'C002');
    """
cursor.execute(query)
query = """
    INSERT INTO Staff VALUES ('S014', 'Angelo Maldonado', '68 Coffee Drive', '9047200688', '2000-05-20', 'Technician', 70000, 'C004');
    """
cursor.execute(query)

# Insert PetOwner data
query = """
    INSERT INTO PetOwner VALUES ('O001', 'Angelica Brown', '900 Canvas Street', '5617865361', 'C005');
    """
cursor.execute(query)
query = """
    INSERT INTO PetOwner VALUES ('O002', 'Barry White', '2002 West Apple Road', '9047433522', 'C004');
    """
cursor.execute(query)
query = """
    INSERT INTO PetOwner VALUES ('O003', 'John Smith', '3000 Sunrise Lane', '7549184564', 'C003');
    """
cursor.execute(query)
query = """
    INSERT INTO PetOwner VALUES ('O004', 'Johnny Williams', '545 East Tangerine Road', '7542936851', 'C002');
    """
cursor.execute(query)
query = """
    INSERT INTO PetOwner VALUES ('O005', 'Adam Toyota', '7155 South Overlook Ave', '3057448916', 'C001');
    """
cursor.execute(query)

# Insert Pet data
query = """
    INSERT INTO Pet VALUES ('P001', 'Dunkin', '2013-04-29', 'Dog', 'Bulldog', 'Gray', 'O004', 'C002');
    """
cursor.execute(query)
query = """
    INSERT INTO Pet VALUES ('P002', 'Maggie', '2016-12-03', 'Dog', 'Husky', 'White', 'O001', 'C005');
    """
cursor.execute(query)
query = """
    INSERT INTO Pet VALUES ('P003', 'Leo', '2010-09-16', 'Cat', 'Siamese', 'White', 'O003', 'C003');
    """
cursor.execute(query)
query = """
    INSERT INTO Pet VALUES ('P004', 'Snuffles', '2018-06-07', 'Dog', 'Golden Retriever', 'Golden', 'O005', 'C001');
    """
cursor.execute(query)
query = """
    INSERT INTO Pet VALUES ('P005', 'Ginger', '2014-08-12', 'Cat', 'Sphynx', 'Tan', 'O002', 'C004');
    """
cursor.execute(query)
query = """
    INSERT INTO Pet VALUES ('P006', 'Baxter', '2018-02-21', 'Dog', 'Lab', 'Black', 'O003', 'C003');
    """
cursor.execute(query)
query = """
    INSERT INTO Pet VALUES ('P007', 'Ollie', '2017-01-05', 'Dog', 'Husky', 'Gray', 'O004', 'C002');
    """
cursor.execute(query)

# Insert Examination data
query = """
    INSERT INTO Examination VALUES ('E001', 'Stomach issues', 'Gave the dog a piece of steak and he has been having stomach issues.', 
        '2022-07-20', 'Gave anti-nausea medication and recommended a plain diet.', 'S013', 'P001');
    """
cursor.execute(query)
query = """
    INSERT INTO Examination VALUES ('E002', 'Ear infection', 'Skin around ear has turned red and signs of swelling and scratching.', 
        '2022-08-01', 'Thoroughly cleaned ears and recommended a topical medication for use at home.', 'S007', 'P002');
    """
cursor.execute(query)
query = """
    INSERT INTO Examination VALUES ('E003', 'Cancer', 'Large mass in mouth indicating oral cancer. Trouble eating and bloody discharge from mouth.', 
        '2022-09-29', 'Scheduled surgery to remove the oral tumor for 2022-11-15.', 'S012', 'P003');
    """
cursor.execute(query)
query = """
    INSERT INTO Examination VALUES ('E004', 'Allergies', 'Has been itching his belly and sneezing often.',
        '2022-10-13', 'Gave injection and oral medications to take at home.', 'S011', 'P004');
    """
cursor.execute(query)
query = """
    INSERT INTO Examination VALUES ('E005', 'Pain', 'Pain in rear left leg, noticable limp when walking.',
        '2022-11-15', 'Minor sprain in rear left leg, gave anti-inflammatory medications.', 'S014', 'P005');
    """
cursor.execute(query)
query = """
    INSERT INTO Examination VALUES ('E006', 'Cancer', 'Surgery for oral tumor.',
        '2022-11-15', 'Successfully removed tumor, gave medication and told owner to monitor any signs of infection.', 'S012', 'P003');
    """
cursor.execute(query)
query = """
    INSERT INTO Examination VALUES ('E007', 'Eye condition', 'Has been bumping into objects and is scared to go up or down stairs.',
        '2022-11-27', 'Gave eye drops and oral medications for owner to give at home.', 'S012', 'P006');
    """
cursor.execute(query)
query = """
    INSERT INTO Examination VALUES ('E008', 'Ligament tear', 'Struggles to bear weight on back left leg and is painful to touch.',
        '2022-12-04', 'Told owner to monitor his behavior and if conditions worsen we will schedule surgery.', 'S013', 'P007');
    """
cursor.execute(query)

# Select data
query = """
    SELECT *
    FROM Clinic
    """
cursor.execute(query)

# Extract column names from cursor
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df)
print(df.columns)

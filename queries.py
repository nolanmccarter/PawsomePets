# Queries from part 2

# 1. 
# List all staff numbers and names of those with the position ‘Manager’ as with their corresponding clinic numbers and names.
query = """
    SELECT Staff.staffNo, Staff.name, Staff.position, Clinic.clinicNo, Clinic.name
    FROM Staff, Clinic
    WHERE Staff.position='Manager' AND Staff.staffNo=Clinic.staffNo
    ;
    """
cursor.execute(query)

# 2.
# List the names and phone numbers of owners of pets with the breed ‘Husky’.
query = """
    SELECT Pet.breed, PetOwner.name, PetOwner.telephoneNo
    FROM Pet, PetOwner
    WHERE Pet.breed='Husky' AND Pet.ownerNo=PetOwner.ownerNo
    ;
    """
cursor.execute(query)

# 3.
# List all staff that work in the Coral Gables clinic and have a salary greater than $50,000.
query = """
    SELECT Clinic.name, Staff.staffNo, Staff.name, Staff.salary
    FROM Clinic, Staff
    WHERE Clinic.name='Coral Gables' AND Staff.salary > 50000 AND Clinic.clinicNo=Staff.clinicNo
    ORDER BY Staff.salary ASC
    ;
    """
cursor.execute(query)

# 4.
# List all pets belonging to John Smith including their species, breed and color.
query = """
    SELECT PetOwner.name, Pet.species, Pet.breed, Pet.color
    FROM PetOwner, Pet
    WHERE PetOwner.name='John Smith' AND PetOwner.ownerNo=Pet.ownerNo
    ;
    """
cursor.execute(query)

# 5.
# List all the cats that underwent an examination on November 15, 2022.
query = """
    SELECT Examination.dateSeen, Pet.petNo, Pet.name
    FROM Pet, Examination 
    WHERE Examination.dateSeen='2022-11-15' AND Examination.petNo=Pet.petNo AND Pet.species='Cat'
    ORDER BY Pet.petNo ASC
    ;
    """
cursor.execute(query)

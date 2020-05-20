from datetime import date
import csv
#class to make objects from all records from GFS (FR01, 03, 08, 09)
class CsvRecord:
    def __init__(self, div_code, uni_lib, uni_date_debut, uni_date_fin, uni_code):
        self.div_code = div_code
        self.uni_lib = uni_lib
        self.uni_date_debut = uni_date_debut
        self.uni_date_fin = uni_date_fin
        self.uni_code = uni_code
        self.created_by_user = "python user"
        self.last_update_day = str(date.today())
    def to_string(self):
        print ("div_code = " + self.div_code + "\nuni_lib = " + self.uni_lib +
               "\nuni_date_debut = " + self.uni_date_debut + "\nuni_date_fin = " + self.uni_date_fin +
               "\nuni_code = " + self.uni_code + "\ncreated_by_user = " + self.created_by_user + "\nlast_update_day = " + self.last_update_day)

#class to make objects from Database data

class DataFromDatabaseRecord:
    def __init__(self, uni_code, uni_parent, uni_type):
        self.uni_code = uni_code
        self.uni_parent = uni_parent
        self.uni_type = uni_type
    def to_string(self):
        print("uni_code = " + self.uni_code + "\nuni_parent = " + self.uni_parent + "\nuni_type = " + self.uni_type)

#function used to filter Uni_Codes which has no uni_parent

def checkIfUniCodeHasNoParent(uni_code, database_codes_objects_list : [DataFromDatabaseRecord] ):
    for record in database_codes_objects_list:
        if uni_code == record.uni_code:
            if record.uni_parent == "":
                return True
#making list of DataFromDatabaseRecords objects, to create this file export results of query: "SELECT UNI_CODE, UNI_PARENT, UNI_TYPE FROM S_UNITE WHERE div_code in ('FR03', 'FR01', 'FR08', 'FR09');"

database_codes_objects_list = []
with open('database_codes.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    for row in csv_reader:
        record = DataFromDatabaseRecord(row[0], row[1], row[2])
        database_codes_objects_list.append(record)


#making list of all uni_codes which are in database

database_codes = []
for record in database_codes_objects_list:
    new_line = record.uni_code
    database_codes.append(new_line)

#making list of all CsvRecords

records_list = []
with open('FRAll_input.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ";")
    for row in csv_reader:
        record = CsvRecord(row[0], row[1], row[2], row[3], row[4])
        records_list.append(record)

#Creating SQL statements
insert_statements = []
update_statements = []
update_statements_with_uni_parent = []

for record in records_list:
    if record.uni_code not in database_codes:
        statement = "Insert into WTR.S_UNITE (DIV_CODE,UNI_CODE,UNI_LIB,UNI_PARENT,UNI_TYPE,UNI_DATE_DEBUT," \
                    "UNI_DATE_FIN,UNI_MATRICULE_MGR,UNI_DIVISION_MGR,UNI_UNITE_MGR,CREATION_DATE,CREATED_BY_USER," \
                    "LAST_UPDATE_DATE,MODIFIED_BY_USER,INTERFACE_DATE,SL_CODE,UNI_MATRICULE_MGR2,UNI_DIVISION_MGR2," \
                    "UNI_UNITE_MGR2,UNI_MATRICULE_SEC1,UNI_DIVISION_SEC1,UNI_UNITE_SEC1,UNI_MATRICULE_SEC2," \
                    "UNI_DIVISION_SEC2,UNI_UNITE_SEC2,UNI_MATRICULE_CTG1,UNI_DIVISION_CTG1,UNI_UNITE_CTG1," \
                    "UNI_MATRICULE_CTG2,UNI_DIVISION_CTG2,UNI_UNITE_CTG2,BU) " \
                    "values ('" + record.div_code + "','" + record.uni_code + "','" + record.uni_lib + "','N','N',to_date('" + record.uni_date_debut + "','DD.MM.YYYY')," \
                    "to_date('" + record.uni_date_fin + "','DD.MM.YYYY'),null,null,null,to_date('" + record.last_update_day + "','YYYY-MM-DD')," \
                    "'" + record.created_by_user + "',null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null);"
        insert_statements.append(statement)
    elif record.uni_code in database_codes and checkIfUniCodeHasNoParent(record.uni_code, database_codes_objects_list):
        statement = "UPDATE WTR.S_UNITE SET UNI_LIB = '" + record.uni_lib + "', UNI_DATE_DEBUT = TO_DATE('" + record.uni_date_debut + "', 'DD.MM.YYYY'), " \
                    "UNI_DATE_FIN = TO_DATE('" + record.uni_date_fin + "', 'DD.MM.YYYY'), LAST_UPDATE_DATE = TO_DATE('" + record.last_update_day + "', 'YYYY-MM-DD')," \
                    " CREATED_BY_USER = '" + record.created_by_user + "', UNI_PARENT = 'N', UNI_TYPE = 'N'" + " WHERE UNI_CODE = '" + record.uni_code + "';"
        update_statements_with_uni_parent.append(statement)
    else:
        statement = "UPDATE WTR.S_UNITE SET UNI_LIB = '" + record.uni_lib + "', UNI_DATE_DEBUT = TO_DATE('" + record.uni_date_debut + "', 'DD.MM.YYYY'), " \
                    "UNI_DATE_FIN = TO_DATE('" + record.uni_date_fin + "', 'DD.MM.YYYY'), LAST_UPDATE_DATE = TO_DATE('" + record.last_update_day + "', 'YYYY-MM-DD')," \
                    " CREATED_BY_USER = '" + record.created_by_user + "' WHERE UNI_CODE = '" + record.uni_code + "';"
        update_statements.append(statement)

#Saving output file
with open ("SQL_statements.sql", 'w') as output:
    output.write("UNI_CODES which are not" +
                 " present in the database (" + str(len(insert_statements)) + " records in total):\n--------------------------------------------------------------\n")
    for line in insert_statements:
        output.write(line + "\n")
    output.write("\n--------------------------------------------------------------------\nUNI_CODES which are" +
                 " present in the database (" + str(len(update_statements)) +
                 " records in total):\n----------------------------------------------------------\n")
    for line in update_statements:
        output.write(line + "\n")
    output.write("\n--------------------------------------------------------------------\nUNI_CODES which are" +
                 " present in the database but has null as parent (" + str(len(update_statements_with_uni_parent)) +
                 " records in total):\n----------------------------------------------------------\n")
    for line in update_statements_with_uni_parent:
        output.write(line + "\n")
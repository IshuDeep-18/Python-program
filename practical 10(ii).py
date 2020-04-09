import cx_Oracle
con = cx_Oracle.connect("system/admin@localhost:1521/xe")
cur = con.cursor()
stmt = 'select * from stdb'
cur.execute(stmt)
result = cur.fetchall()
print("Name\tMother's Name\tFather's Name\tDOB\t\tAddress\t\t\tPin code\tDepartment\tBranch\tContact\t\t\tEmail")
for data in result:
    print(data[0],'\t',data[1],'\t\t',data[2],'\t\t',data[3],'\t',data[4],'\t',data[5],'\t',data[6],'\t\t',data[7],'\t',data[8],'\t',data[9])
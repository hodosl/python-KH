# try:
#     f = open("MOCK_DATA.csv")
#      for line in f:
#         print(line.strip())
# finally: # mindig lefut, ha hiba van, ha nincs
#     f.close()

from ipaddress import ip_address


count = 0
employees = []
with open("MOCK_DATA.csv") as f: # ez a helyes mód!
    for line in f:
        employee = line.strip().split(",")
        id, first_name, last_name, email, gender, ip_address = employee
        employees.append(employee)
        if "Female" in line:
            #print(line.strip())
            count += 1

print(f"{count} db no talalhato")
print(employees)



# Напишите программу для печати всех уникальных значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, 
# {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]

d= [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]

res = set()
for i in d:
    for item in i:
        res.add(i[item])
print(res)
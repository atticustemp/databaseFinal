import pymysql
lineToAdd = []
resources = 0
db = pymysql.connect(host = 'database-final.cazc7ungu94n.us-west-2.rds.amazonaws.com', user = 'admin', password= 'Sheba123!', database= 'final' )
crsr = db.cursor()

#input = open("legalRes.txt")
#input = open("patentRes.txt")
#input = open("taxRes.txt")
#input = open("industry.txt")
#input = open("BType.txt")
#input = open("certifications.txt")
input = open("bankingRes.txt")

lineToAdd.append([])
for i in input:
    data = i.strip().split(',')
    data = i.split('\n')
    for i in data:
        if i == '':
            resources += 1
            lineToAdd.append([])
        else:
            lineToAdd[resources].append(i)

for i in range(2 , len(lineToAdd)):
    query = 'INSERT INTO final.'
    query = query + lineToAdd[0][0] + ' ('
    for k in lineToAdd[1]:
        query = query + k + ','
    query = query[:-1]
    query = query + ') Values('
    tempData = lineToAdd[i][0].split(',')
    for j in range(0,len(tempData)):
        query = query + '\'' + tempData[j] + '\','
    query = query[:-1]
    query = query + ');'
    res = crsr.execute(query)
    db.commit()


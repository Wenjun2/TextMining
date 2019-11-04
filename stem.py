from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
ps = PorterStemmer()
import csv
with open('export.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    #rows = [row for row in reader]
    column = [row[0] for row in reader]
csvfile.close
with open('export.csv','r') as csv1:
    reader = csv.reader(csv1)
    column1 = [row[1] for row in reader]
    #print(column1)
csv1.close
with open('export.csv', 'r') as cf:
    reader = csv.reader(cf)
    column2 = [row[2] for row in reader]
cf.close
a = []
b= []
c = []
for w in column:
    a.append(ps.stem(w))
for term in column1:
    b.append(ps.stem(term))
#print(b)
for termid in column2:
    c.append(ps.stem(termid))
rows = zip(a,b,c)
with open('JD.csv','w') as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)
f.close

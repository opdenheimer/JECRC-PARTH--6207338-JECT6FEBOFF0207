import csv
from datetime import date
file=open('expense.csv','a+',newline='')
# w=csv.writer(file)
r=csv.reader(file)
file.seek(0)
print(list(r))
# w.writerow(['Date','Category','Amount'])
# w.writerows([
#     [
#      date.today(),'Travel',2000
#     ],
#     [
#      date.today(),'food',1100
#     ]
# ])
file.close()
from datetime import datetime
d=list(map(int,input().split()))
date_1=datetime(d[0],d[1],d[2])
print(date_1.strftime("%B"))

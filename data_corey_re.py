import os
import re
with open(r'C:\Users\user\Desktop\GeekTech\2month\src\data_corey_re.txt') as f:
    text=f.read()
lookfor=r'\d'
withseven=r'\b7'
gmails=r'\S+@\S+'
result=re.findall(lookfor,text)
result_two=re.findall(withseven,text)
gmailsfind=re.findall(gmails,text)
print(f'Total amount of phone numbers:',len(lookfor))
print(f"Total amount of phone numbers with ending 7:",len(withseven))
print(f'Total gmails without symbols,numbers,-, besides letters and which end in com or net:',len(gmailsfind))

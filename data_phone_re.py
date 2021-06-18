import re
with open(r'C:\Users\user\Desktop\GeekTech\2month\src\data_phone.json') as f:
    text=f.read()


digits = r"[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]"
search=re.findall(digits,text)
print(f'Total amount of phone numbers with 13 digits:',len(search))

code = r"(\d{3})(\d{3})(\d{4})"
search_2 = re.findall(code,text)
print(search_2)
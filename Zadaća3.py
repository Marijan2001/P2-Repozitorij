import re
txt="marijan zivkovic"
regex= "m.....z$"

result= re.findall(regex, txt)

if result:
    print("Podudaranje:", result)
else:
    print("Nema podudaranja")

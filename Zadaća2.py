from csv import reader

with open("rezultati.csv", "r") as read_obj:
    csv_reader = reader(read_obj)

    prezime = list(map(tuple, csv_reader))

    prezime.sort()

    print(prezime)

for ime, prezime, bodovi in rezultati:
    if int(bodovi) >= 0% or <= 49%:
        print(Nedovoljan)

    if int(bodovi) >= 50% or <= 64%:
        print(Dovoljan)

    if int(bodovi) >= 65% or <= 79%:
        print(Dobar)

    if int(bodovi) >= 80% or <= 89%:
        print(Vrlo dobar)

    if int(bodovi) >= 90 % or <= 100%:
        print(Odličan)

novi_rezultati=[]
for ime, prezime, bodovi in rezultati:
    novi_rezultati.append((bodovi, ime, prezime))

novi_rezultati.osrt(reverse=True)
print(novi_rezultati)

for bodovi, ime, prezime in novi_rezultati:
    print(bodovi, ime, prezime)

     
        

     

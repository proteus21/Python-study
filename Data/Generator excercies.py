'''W tym zadaniu należy przerobić listy z poprzedniego LAB do postaci generatora.  Nieco problematyczne
będzie ustalenie ile wartości jest generowanych przez generator, bo w tym celu... trzeba go przejść!

Jeżeli taki opis Ci wystarcza to GO! GO! GO!

A tu dokładniejsza instrukcja:

Na przekręcie z wpłatomatem z poprzedniego zadania postanawiasz wraz ze swoim szefem otworzyć linie
lotnicze "Flying Python". Linie będą krajowe. Oto wykaz portów lotniczych:

ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']
1. Zbuduj generator tupletów symbolizujących port początkowy i końcowy. Wykonaj połączenie każdy-z-każdym

2. Wyeliminuj z powyższego generatora połączenie z portu do tego samego portu

3. Ponieważ połączenie z A do B dubluje się z połączeniem z B do A - wygeneruj możliwe połączenia krajowe
pomijając takie zdublowane trasy.

4. Policz ilość generowanych połączeń w krokach 1,2,3. W tym celu napisz pętlę for, która: wyświetli
wygenerowane wartości i policzy je

)'''

ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']
routes= ( (start, stop) for start in ports for stop in ports)
print(routes)
# if appears <generator object <genexpr> at 0x000001B7D9BE91C8>
counter = 0
for (start, stop) in routes:
    print("{} - {}".format(start, stop))
    counter += 1
print(counter)

#2
routes= ( (start, stop) for start in ports for stop in ports if start !=stop)
print(routes)
for (start, stop) in routes:
    print("{} - {}".format(start, stop))
    counter += 1
print(counter)

#3
routes= ( (start, stop) for start in ports for stop in ports if start <stop)
print(routes)
for (start, stop) in routes:
    print("{} - {}".format(start, stop))
    counter += 1
print(counter)




#


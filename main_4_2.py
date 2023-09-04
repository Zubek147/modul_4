#stworzę funkcję określającą czy dane słowo to palindrom
#jeśli testowane słowo będzie palindromem funkcja zwróci wartość TRUE
#jeśli testowane słowo nie będzie palindromem funkcja zwróci wartośc FALSE
#przetestuję słowo, które jest palindromem, żeby sprawdzić czy funkcja działa poprawnie
#dla pewności sprawdzę kolejne słowo, które jest palindromem
#przetestuję słowo, które nie jest palindromem, żeby sprawdzić drugi warunek funkcji i poprawność działania

def palindrome_check(tekst):
    tekst = tekst.lower().replace(" ","").replace(",","").replace("'","")
    return tekst == tekst[::-1] , f"{tekst} {'to' if tekst == tekst[::-1] else 'to nie'} palindrom."

print(palindrome_check('Kajak'))
print(palindrome_check('Anna'))
print(palindrome_check('Madam, in Eden, I\'m Adam'))
print(palindrome_check('Kobyła ma mały bok'))
print(palindrome_check('Rowerek'))


#stworzę funkcję określającą czy dane słowo to palindrom
#jeśli testowane słowo będzie palindromem funkcja zwróci wartość TRUE
#jeśli testowane słowo nie będzie palindromem funkcja zwróci wartośc FALSE
#przetestuję słowo, które jest palindromem, żeby sprawdzić czy funkcja działa poprawnie
#dla pewności sprawdzę kolejne słowo, które jest palindromem
#przetestuję słowo, które nie jest palindromem, żeby sprawdzić drugi warunek funkcji i poprawność działania

def palindrome_check(tekst):
    if tekst == tekst[::-1]:
        return True
    else:
        return False
print(palindrome_check('kajak'))
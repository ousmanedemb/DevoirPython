# Ecris autrement
lst1 = list(range(1200, 2000, 135))
lst2 = [i * 2 for i in lst1 if i % 2 == 0]
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
o = [x for x in numbers if x % 2 == 0]
e = [x for x in numbers if x % 2 != 0]

# Affichage des résultats
print(lst1)
print(lst2)
print(o)
print(e)

# la fonction sum() permet d'additionner 2 nombres entier :
# Exemple
print(sum([5,10]))
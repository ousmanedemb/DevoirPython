import sqlite3


def manquant_1(tableau):
    x = min(tableau)
    y = max(tableau)
    somme_attendue = sum(range(x, y + 1))

    # Calculer la somme réelle des nombres dans le tableau
    somme_reelle = sum(tableau)

    # Trouver le nombre manquant
    nombre_manquant = somme_attendue - somme_reelle

    # Stocker le nombre manquant dans la table SQLite
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS nombres_manquants (nombre INTEGER)")
    cursor.execute("INSERT INTO nombres_manquants VALUES (?)", (nombre_manquant,))
    connection.commit()
    connection.close()

    return nombre_manquant


def manquant_2(tableau):
    # Trouver la somme attendue des nombres consécutifs
    x = min(tableau)
    y = max(tableau)
    somme_attendue = 0
    for i in range(x, y + 1):
        somme_attendue ^= i

    # Calculer la somme réelle des nombres dans le tableau
    somme_reelle = 0
    for nombre in tableau:
        somme_reelle ^= nombre

    # Trouver le nombre manquant
    nombre_manquant = somme_attendue ^ somme_reelle

    # Stocker le nombre manquant dans la table SQLite
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS nombres_manquants_xor (nombre INTEGER)")
    cursor.execute("INSERT INTO nombres_manquants_xor VALUES (?)", (nombre_manquant,))
    connection.commit()
    connection.close()

    return nombre_manquant


# Exemple
tableau_exemple = [1, 2, 3, 4, 5, 6, 7, 9, 10]
resultat1 = manquant_1(tableau_exemple)
resultat2 = manquant_2(tableau_exemple)
print("Nombre manquant :", resultat1)
print("Nombre manquant :", resultat2)
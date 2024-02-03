def transform(chain):
    # votre programme ici
    chaine1 = chain[0]
    chaine2 = chain[1]
    chiffres1 = set(filter(bool, chaine1.split(', ')))
    chiffres2 = set(filter(bool, chaine2.split(', ')))
    resultat = sorted(chiffres1 & chiffres2, key=int, reverse=True)
    if not resultat:
        return None
    else:
        return f"{resultat} : DEMBELE_Ousmane_Master1IA"


# vous ne modifierez rien après cette ligne
if __name__ == "__main__":
    arr1 = ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
    out = transform(arr1)
    print(out)  # doit afficher ---> 31,4,1:nom_prenom_classe

    arr3 = ["9, 3, 5, 7, 14", "10, 2, 6, 16, 15"]
    out = transform(arr3)
    print(out)  # doit afficher ---> None

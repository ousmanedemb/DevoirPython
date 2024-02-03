# La fonction transform écris autrement
def transform(chain):
    chiffres1 = set(filter(bool, chain[0].split(', ')))
    chiffres2 = set(filter(bool, chain[1].split(', ')))

    resultat = sorted(chiffres1 & chiffres2, key=int, reverse=True)

    return f"{', '.join(resultat)} : DEMBELE_Ousmane_Master1IA" if resultat else None


# vous ne modifierez rien après cette ligne
if __name__ == "__main__":
    arr1 = ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
    out = transform(arr1)
    print(out)  # doit afficher ---> 31,4,1:nom_prenom_classe

    arr3 = ["9, 3, 5, 7, 14", "10, 2, 6, 16, 15"]
    out = transform(arr3)
    print(out)  # doit afficher ---> None

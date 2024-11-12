def fibonacci(n):
    # Cas de base
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Calcul de Fibonacci pour n ≥ 2
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Programme principal
try:
    # Demande à l'utilisateur d'entrer un nombre
    n = int(input("Entrez un nombre entier positif : "))
    
    # Vérification que le nombre est positif
    if n < 0:
        print("Veuillez entrer un nombre positif.")
    else:
        # Calcul et affichage du résultat
        resultat = fibonacci(n)
        print(f"F({n}) = {resultat}")
        
except ValueError:
    print("Erreur : Veuillez entrer un nombre entier valide.")
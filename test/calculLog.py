import numpy

# Calculer y
def f(x) -> float:
# {
    # Calcul de chaque terme avec une gestion d'erreur intégrée pour éviter les valeurs invalides
    term1: float = (2 * x**3 + 4 * x**2 - 5 * x + 7) / numpy.sqrt(x**2 + 1);
    term2: float = numpy.log(x + 5);
    term3: float = numpy.exp(x / 2);
    term4: float = -numpy.abs((3 * x - 4) / (x**2 + 1));

    return term1 + term2 + term3 + term4;
# }

# int main(int argc, char **argv)
# {
# Entree du nombre
x: float = float(input("Veuillez entrer un nombre : "));

# Vérifier si x est valide
if x <= -5:
# {
    print("Erreur : x doit être supérieur à -5.");
# }
elif x == 0:
# {
    print("Erreur : x doit être différent de 0.");
# }
else:
# {
    y = f(x);
    if y is not None:
    # {
        print("La valeur de y pour x = ", x, " est : ", y);
    # }
# }
# }

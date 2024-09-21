#  1. Démarrer avec PythonPython est un langage de programmation simple à prendre en main.
# Voici comment afficher un message à l'écran avec la fonction print() :

print("Bienvenue dans le monde de Python !")

# 2. input(). La fonction input() permet de lire une saisie utilisateur :

nom = input("Quel est ton nom ? ")
print(f"Bonjour, {nom} !")

# 3. Variables en Python. En Python, on peut stocker des données dans des variables sans définir leur type (Python est typé dynamiquement) :

age = 17  # Un entier
pi = 3.14159  # Un nombre à virgule flottante
nom_complet = "Jean Dupont"  # Une chaîne de caractères

# 4. Calculs mathématiques en Python. On peut effectuer des opérations arithmétiques de base :

a = 5
b = 3
somme = a + b
produit = a * b
difference = a - b
division = a / b
print(f"Somme: {somme}, Produit: {produit}, Différence: {difference}, Division: {division}")

# 5. Condition - if elif else. Les conditions permettent de diriger le flux de votre programme :

if age < 18:
    print("Vous êtes mineur.")
elif age == 18:
    print("Vous avez tout juste 18 ans.")
else:
    print("Vous êtes majeur.")
  
# 6. Boucle for. La boucle `for` permet de répéter un bloc de code un certain nombre de fois :

for i in range(5):  # de 0 à 4
    print(f"Iteration {i}")

# 7. Boucle while. La boucle `while` s'exécute tant qu'une condition est vraie :

compteur = 0
while compteur < 5:
    print(f"Compteur: {compteur}")
    compteur += 1  # Incrémente compteur

# 8. Module random et math. Le module random permet de générer des nombres aléatoires, et math contient des fonctions mathématiques utiles.

import random
import math

# Nombre aléatoire entre 1 et 10
nombre_aleatoire = random.randint(1, 10)
print(f"Nombre aléatoire : {nombre_aleatoire}")

# Calcul de racine carrée et de puissance avec le module math
racine_carre = math.sqrt(16)  # racine carrée de 16
puissance = math.pow(2, 3)  # 2^3
print(f"Racine carrée : {racine_carre}, Puissance : {puissance}")

# 9. Exercices For, While, If. Exercice : Afficher les nombres pairs entre 1 et 10

for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} est pair.")

# 10. Python et les suites. Exemple de suite arithmétique (suite de nombres avec une différence constante)

premier_terme = 1
raison = 3
n = 10  # Nombre de termes
for i in range(n):
    terme = premier_terme + i * raison
    print(f"Terme {i + 1}: {terme}")

#11. Opérateurs : Modulo %, quotient //, puissance **. Le modulo renvoie le reste de la division, // donne le quotient entier, et ** est l'opérateur de puissance.

a = 10
b = 3

c = x % y
d = x // y 
e = a**b

print(f"10 % 3 = {c} (reste)")
print(f"10 // 3 = {d} (quotient entier)")
print(f"10 ** 3 = {e} (puissance)")

# 12. Liste. Les listes permettent de stocker plusieurs valeurs dans une seule variable.

ma_liste = [1, 2, 3, 4, 5]
print(f"Liste : {ma_liste}")

a = ma_liste[0} # accéder à un élément de la liste à l'index 0
ma_liste[2] = 35 # modifier la valeur de l'élement de la liste à l'index 2
ma_liste.append(6)  # Ajoute un élément à la liste
ma_liste.remove(3)  # Supprime la première occurrence de 3
ma_liste.sort() # trier la liste
ma_liste.reverse() # renverser la liste
b = len(ma_liste) # récuperer le nombre d'éléments dans la liste

#13. Courbes Tracé et graphique. On peut tracer des courbes avec la bibliothèque matplotlib (à installer si besoin avec pip install matplotlib)

import matplotlib.pyplot as plt

x_vals = [1, 2, 3, 4, 5]
y_vals = [1, 4, 9, 16, 25]
plt.plot(x_vals, y_vals)
plt.title("Courbe de y = x^2")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

#14. Chaine de caractères. Une chaîne de caractères est une suite de caractères entourée de guillemets.

ma_chaine = "Bonjour, tout le monde!"

print(f"Premier caractère : {ma_chaine[0]}") # Accéder à un caractère spécifique
print(f"Sous-chaîne de 0 à 6 : {ma_chaine[0:7]}")  # Extraire une sous-chaîne (slicing) de l'indice 0 à 6
print(f"Longueur de la chaîne : {len(ma_chaine)}") # 3. Longueur de la chaîne
print(f"En majuscules : {ma_chaine.upper()}") # Convertir en majuscules 
print(f"En minuscules : {ma_chaine.lower()}") # Convertir en minuscules
nouvelle_chaine = ma_chaine.replace("tout le monde", "les amis") # Remplacer des mots ou caractères
mots = ma_chaine.split()# Diviser une chaîne en une liste de mots (split)
chaine_concatenée = ma_chaine + " Comment ça va ?" # Concaténer (joindre) des chaînes

prenom = "Alice"
age = 25
message = f"Je m'appelle {prenom} et j'ai {age} ans." # Formater une chaîne avec des variables
print(f"Message formaté : {message}")

# 15. Fonction. Les fonctions permettent de regrouper du code réutilisable sous un même nom. il faut utiliser le mot "def" et indenter son code:
#fonction carré
def carre(x):
    return x * x

print(f"Le carré de 4 est {carre(4)}")

#fonction de calcul d'un terme d'une suite arithmétique
def suite_arithmetique(u0, r, n):
    """Renvoie le n-ème terme de la suite arithmétique."""
    return u0 + n * r

# Exemple d'utilisation
u0 = 5  # premier terme
r = 2   # raison
n = 10  # n-ième terme
print(f"Le terme u_{n} de la suite arithmétique est : {suite_arithmetique(u0, r, n)}")

#fonction de calcul d'un terme d'une suite géométrique
def suite_geometrique(u0, q, n):
    """Renvoie le n-ème terme de la suite géométrique."""
    return u0 * (q ** n)

# Exemple d'utilisation
u0 = 3  # premier terme
q = 2   # raison
n = 5   # n-ième terme
print(f"Le terme u_{n} de la suite géométrique est : {suite_geometrique(u0, q, n)}")


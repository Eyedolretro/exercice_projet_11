[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
# Mini-Projet Calculatrice

Ce projet a été implémenté dans le but de s'entrainer au test unitaire à l'aide Pytest et UnitTest. Le code source
contient un mini-projet calculatrice qui permet d'effectuer 4 opérations différentes (addition, soustraction, 
multiplication et division). Vous pourrez ainsi développer l'ensemble des scénarios nécessaires afin de tester 
l'ensemble du code source. À noter que des propositions de corrections sont mises à disposition dans différentes branches 
du répertoire.

## Pré-requis

* Installer Python 3 : [Téléchargement Python 3](https://www.python.org/downloads/)
* Installer git : [Téléchargement Git](https://git-scm.com/book/fr/v2/D%C3%A9marrage-rapide-Installation-de-Git)

## Installation

### 1. Télécharger le projet sur votre répertoire local : 
```
git clone https://github.com/OpenClassrooms-Student-Center/4425126-testing-python.git 
cd 4425126-testing-python
```
### 2. Mettre en place un environnement virtuel :
* Créer l'environnement virtuel: `python -m venv venv`
* Activer l'environnement virtuel :
    * Windows : `venv\Scripts\activate.bat`
    * Unix/MacOS : `source venv/bin/activate`

    
### 3. Installer les dépendances du projet
```
pip install -r requirements.txt
```

## Démarrage
* Lancer le script à l'aide de la commande suivante : `python main.py`

## Corrections
1. Proposition de correction pour les tests unitaires avec UnitTest :
```
git checkout unittest-test
python -m unittest discover tests/
```

2. Proposition de correction pour les tests unitaires avec Pytest :
```
git checkout pytest-test
pytest
```

3. Proposition de correction pour les mocks avec Pytest:
```
git checkout mock-test
pytest
```

4. Proposition de correction pour les tests paramétriques Pytest :
```
git checkout parametrize-test
pytest
```





Plan de Test Unitaire – Super-Calculatrice
Fichier	Fonction	Cas de test	Entrée	Résultat attendu
calculate.py	add	Addition de deux entiers positifs	2, 3	5
calculate.py	add	Addition avec un nombre négatif	-2, 3	1
calculate.py	add	Addition avec zéro	0, 5	5
calculate.py	add	Addition de flottants	2.5, 3.1	5.6
calculate.py	subtract	Soustraction de deux entiers positifs	5, 3	2
calculate.py	subtract	Soustraction avec résultat négatif	3, 5	-2
calculate.py	subtract	Soustraction avec zéro	0, 5	-5
calculate.py	subtract	Soustraction de flottants	5.5, 2.2	3.3
calculate.py	multiply	Multiplication de deux entiers positifs	2, 3	6
calculate.py	multiply	Multiplication par zéro	5, 0	0
calculate.py	multiply	Multiplication avec négatif	-2, 3	-6
calculate.py	multiply	Multiplication de flottants	2.5, 4.0	10.0
calculate.py	divide	Division de deux entiers positifs	6, 3	2
calculate.py	divide	Division avec négatif	-6, 3	-2
calculate.py	divide	Division par zéro	5, 0	lève ZeroDivisionError
calculate.py	divide	Division de flottants	5.0, 2.0	2.5
main.py	main	Entrée utilisateur : addition	"2 + 3"	Affiche 5
main.py	main	Entrée utilisateur : soustraction	"5 - 2"	Affiche 3
main.py	main	Entrée utilisateur : multiplication	"2 * 3"	Affiche 6
main.py	main	Entrée utilisateur : division	"6 / 2"	Affiche 3
main.py	main	Entrée invalide	"a + b"	Affiche message d’erreur
main.py	main	Division par zéro	"5 / 0"	Affiche message d’erreur / exception gérée
tests/test_calculate.py	test_addition	Vérifie toutes les combinaisons pour add	2,3 ; -2,3 ; 0,5 ; 2.5,3.1	5 ; 1 ; 5 ; 5.6
tests/test_calculate.py	test_soustraction	Vérifie toutes les combinaisons pour subtract	5,3 ; 3,5 ; 0,5 ; 5.5,2.2	2 ; -2 ; -5 ; 3.3
tests/test_calculate.py	test_multiplication	Vérifie toutes les combinaisons pour multiply	2,3 ; -2,3 ; 5,0 ; 2.5,4.0	6 ; -6 ; 0 ; 10.0
tests/test_calculate.py	test_division	Vérifie toutes les combinaisons pour divide	6,3 ; -6,3 ; 5,0 ; 5.0,2.0	2 ; -2 ; lève ZeroDivisionError ; 2.5
Recommandations supplémentaires
Cas limites :
Tester des nombres très grands ou très petits.
Tester des flottants avec plusieurs décimales.
Type de retour :
add, subtract, multiply → int ou float.
divide → float.
Paramétrisation Pytest :
Utiliser @pytest.mark.parametrize pour tester plusieurs combinaisons rapidement.
Gestion des exceptions :
Toujours tester la division par zéro (ZeroDivisionError).

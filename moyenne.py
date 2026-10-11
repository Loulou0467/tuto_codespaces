"""Ce module fournit une fonction pour calculer une moyenne de valeurs"""

# NB: Ce fichier contient du code à compléter

from rich.markdown import Markdown
from rich.console import Console


def moyenne(valeurs):
    # docstrings en markdown
    if not valeurs:
        raise ValueError("La liste ne doit pas être vide")
    
    return sum(valeurs) / len(valeurs)



if __name__ == "__main__":
    Console().print(Markdown(moyenne.__doc__))
    print("moyenne([10, 20, 15]) :", end=" ")
    print(moyenne([10, 20, 15]))

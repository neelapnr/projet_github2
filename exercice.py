print('Bienvenue dans le gestionnaire de todo')

# Liste des todos (chaque todo est un dictionnaire avec un nom et un statut)
todos = []

def lister_todos():
    """Affiche tous les todos avec leur statut"""
    if not todos:
        print("Aucun todo à afficher.")
    else:
        print("\nListe des todos :")
        for i, todo in enumerate(todos):
            print(f"{i + 1}: {todo['name']} - Statut: {todo['status']}")

def creer_todo():
    """Crée un nouveau todo avec le statut 'à faire'"""
    nom_todo = input("Entrez le nom du todo : ")
    todo = {"name": nom_todo, "status": "à faire"}
    todos.append(todo)
    print(f"Le todo '{nom_todo}' a été créé avec le statut 'à faire'.")

def modifier_statut_todo():
    """Permet de modifier le statut d'un todo"""
    lister_todos()
    if not todos:
        return

    try:
        index = int(input("\nEntrez le numéro du todo dont vous voulez modifier le statut : ")) - 1
        if index < 0 or index >= len(todos):
            print("Numéro de todo invalide.")
            return

        todo = todos[index]
        if todo['status'] == "à faire":
            todo['status'] = "Fait"
            print(f"Le statut du todo '{todo['name']}' a été changé en 'Fait'.")
        elif todo['status'] == "Fait":
            # Erreur volontaire : changer le statut en "à fair" au lieu de "à faire"
            todo['status'] = "à fair"
            print(f"Le statut du todo '{todo['name']}' a été changé en 'à fair'.")
        else:
            print(f"Le statut du todo '{todo['name']}' est déjà dans un état inconnu.")
    except ValueError:
        print("Entrée invalide. Veuillez entrer un numéro de todo valide.")

def supprimer_todo():
    """Supprime un todo"""
    lister_todos()
    if not todos:
        return

    try:
        index = int(input("\nEntrez le numéro du todo à supprimer : ")) - 1
        if index < 0 or index >= len(todos):
            print("Numéro de todo invalide.")
            return

        todo = todos.pop(index)
        print(f"Le todo '{todo['name']}' a été supprimé.")
    except ValueError:
        print("Entrée invalide. Veuillez entrer un numéro de todo valide.")

# Boucle principale
choix = ''
while choix != 'q':
    print('\n ====Menu principal====')
    print('1: Lister les todos')
    print('2: Créer un todo')
    print('3: Modifier le statut d\'un todo')
    print('4: Supprimer un todo')
    print('q: quitter')

    choix = input('=> Choix :')

    match choix:
        case '1':
            lister_todos()
        case '2':
            creer_todo()
        case '3':
            modifier_statut_todo()
        case '4':
            supprimer_todo()
        case 'q':
            print('Au revoir')
        case _:
            print('Choix invalide')

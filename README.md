Vous travaillez au service informatique du grand hôtel le Ritz Otto à Paris qui souhaite moderniser et améliorer 
son système d'information car beaucoup de données sont encore conservées en version papier. 
Une grande partie des revenus de l'hôtel provient des événements d'entreprise et notamment des conférences organisées 
dans ses locaux.
La direction vous a demandé de travailler sur une application qui permettra la gestion du calendrier des conférences 
et des conférenciers intervenant dans les locaux. Cela permettra au personnel d'économiser du temps et d'éviter les 
erreurs d'organisation.Spécifications fonctionnelles :- La page d'accueil demande à l'utilisateur s'il souhaite gérer les 
conférenciers ou les conférences- Depuis l'accueil l'utilisateur peut quitter l'application- 
Sur la page de gestion des conférenciers l'utilisateur peut : créer un conférencier, supprimer un conférencier ou voir tous les conférenciers- Un conférencier est composé d'un prénom, d'un nom, d'une description, d'une profession et d'un statut 
(actif ou non-actif). 
Par défaut tout nouveau conférencier est considéré comme actif- 
La liste des conférenciers n'affiche que les conférenciers actifs
- Sur la page de gestion des conférences l'utilisateur peut : 
créer une conférence, supprimer une conférence ou voir toutes les conférences- 
Une conférence est composée d'un titre, d'un résumé, d'une date, d'une heure, d'une date de création 
et est obligatoirement associée à un conférencier par son ID- Quand on affiche toutes les conférences, 
on affiche également le prénom et le nom du conférencierassocié.- 
La suppression d'une entité (conférence ou conférencier) se fait par son ID uniquement- 
Depuis une page de gestion l'utilisateur peut revenir à la page d'accueil- 
Faire en sorte que si l'on supprime un conférencier alors toutes les conférences qui lui sont associées sont 
également suppriméesSpécifications techniques :- Langage Python 3- Organisation du code selon le principe MVC- 
Usage de la programmation orientée objet- Respect du principe DRY- Essayer de respecter certains des principes SOLID- 
Programme exécutable par le lancement d'un fichier main.py- 
Intégration d'une base de données PostgreSQL via la librairie Psycopg2

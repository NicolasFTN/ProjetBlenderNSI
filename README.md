# ProjetBlenderNSI

## Description

creation d'arbre aleatoire via le logiciel blender avec python

## Solution



## Cahier journal

Attention les codes donnés ci-dessous son executable uniquement dans le logiciel Blender version 1.9 et versions ultérieures. Les fichiers blender sont directement donner avec le code intégrer . Mais le code python est lui aussi données à part même si celui-ci utilise les modules Blender. Le résultat ne peut pas être afficher en dehors de Blender

## 25/03

Apprentissage du fonctionnement de python dans Blender via les tuto sur Youtube de Motion Live Tech.

## 09/03

Mise en page du contenu Git Hub

## 13/03

Début de la programmation . J'ai reussi à générer un nombre aléatoire de meltball pour faire un tronc de plus ou moins grande longueur,
mais le résulat n'était pas satisfaisant .
J'ai donc plutot générer des courbes de beziers avec des paramêtre aleatoire se qui a permis d'avoir un base pour un tronc plus oragnique avec des coubures aleatoire.
J'ai ainsi realiser aussi les première branche de l'arbre . Un probleme persiste il faut que je fasse concorder le bout du tronc et le départ des branches.

Code: [ProjetArbre.py](ProjetArbre.py) / Code + Visuel 3D: [ProjetArbre.blend](ProjetArbre.blend)

## 15/03
J'ai passé beaucoup d'heures sur le projet aujourd'hui le programme a enormement avancer . J'ai regler le probleme de la dernière session. J'ai fait apparaitre les feuilles sur les branches de mon arbre , donner de l'épaisseur au tronc, et ajouter des couleurs a l'arbre mais j'ai un probleme dans mon code que je n'arrive pas a regler et c'est essentiel pour pouvoir donner de la couleur au tronc.

Code: [ProjetArbre1.py](ProjetArbre1.py) / Code + Visuel 3D: [ProjetArbre1.blend](ProjetArbre1.blend)


## 20/03
Changement de methode je n'utilise plus les particules hair dans blender mais je vais importer un objet feuille que je vais dupliquer le long de chaque branches
via des listes et leurs index

Code: [ProjetArbre2.py](ProjetArbre2.py) / Code + Visuel 3D: [ProjetArbre2.blend](ProjetArbre2.blend)

## 27/03
codage importation feuille et aplication des contraines et des modifiers

Code: [ProjetArbre3.py](ProjetArbre3.py) / Code + Visuel 3D: [ProjetArbre3.blend](ProjetArbre3.blend)

## 29/03
le programme fonctionne quelques ajouts et reglages reste encore à faire.
J'ai utiliser une variable x dans ma boucle for qui lui ajoute 1 a chaque répétiton se meme x va être convertie en str a la fin de chaque nom d'objet créer se qui me permet de les nommés precisemment et faire des actions independament sur chaque objet

Code: [ProjetArbre4.py](ProjetArbre4.py) / Code + Visuel 3D: [ProjetArbre4.blend](ProjetArbre4.blend)

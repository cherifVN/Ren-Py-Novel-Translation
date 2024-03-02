# Ren-Py-Novel-Translation
Cet outil en Python est un traducteur de Visual Novel qui ont été fait avec Ren'Py.

Il filtre le fichier afin de traduire uniquement les dialogues en prenant soin de gérer tous les cas comme de ne pas traduire les variables ou autre

## Table des Matières

- [Utilisation](#utilisation)
  
- [Avertissement](#avertissement)
  
- [Limitations et Erreurs Connues](#limitations-et-erreurs-connues)
  - [Traductions](#traductions)
  - [Echappements](#echappements)
  - [Encodage de fichiers](#encodage-de-fichiers)
- [A venir](#a-venir)
    
- [License](#license)

## Utilisation

1. [Installez Python](https://www.python.org/)
2. Téléchargez Ren'Py Novel Translation en clonant avec [git](https://git-scm.com/) ou en téléchargant le zip dans Code
3. Installez [googletrans 4.0.0rc1](https://pypi.org/project/googletrans/4.0.0rc1/) en utilisant la commande: `pip install googletrans==4.0.0rc1`
4. Vérifiez que vous avez bien la même version de Ren'Py que votre jeu et éxécutez Ren'Py
5. Générez des fichiers de traduction de votre jeu
6. Copiez [translator.py](https://github.com/cherifVN/Ren-Py-Novel-Translation/blob/main/translator.py) dans le dossier tl/yourlanguage (yourlanguage est le nom de la langue de la traduction)
7. Executez le. Renseignez le nom du fichier à traduire, la langue source/d'origine et la langue cible (dans laquelle vous voulez traduire)
8. Votre fichier sera traduit dans en tant que nomfichier_traduit.rpy (nomfichier est le nom de départ de votre fichier)

## Avertissement


Cet outil est actuellement en version bêta.Il se peut que des bugs mineurs se produisent mais rien de grave. Il est mis à jour régulièrement et je travaille constamment à son amélioration et à l'ajout de nouvelles fonctionnalités

Si vous rencontrez des problèmes ou avez des suggestions d'amélioration, n'hésitez pas à m'en en informer en créant une nouvelle [issue](https://github.com/cherifVN/Ren-Py-Novel-Translation/issues)

Si vous souhaitez apporter des modifications ou des corrections, n'hésitez pas à créer un [fork](https://github.com/cherifVN/Ren-Py-Novel-Translation/fork) du projet, à effectuer vos modifications et à soumettre une [pull request](https://github.com/cherifVN/Ren-Py-Novel-Translation/pulls) avec vos propositions

De plus, si vous appréciez cet outil et que vous souhaitez soutenir son développement, n'hésitez pas à lui donner une étoile ⭐️ sur GitHub

Merci de votre intérêt et de votre soutien !

## Limitations et Erreurs Connues

 Comme Ren'Py Novel Translation est en version beta, il a quelques limitations et erreurs connues à prendre en compte :

### Traductions
Les traductions sont effectuées par un traducteur automatique, comme google traduction, ce qui peut causer des traductions approximatives. Il est conseillé de relire le code pour corriger si besoin.

Le code n'étant pas optimisé, il se peut que la traduction soit longue pour les gros fichiers

Le traducteur traduit uniquement les fichiers en .rpy. Il ne traduira en aucun cas d'autres fichiers comme les images, les sons etc.

### Encodage de fichiers 

certains encodages de fichiers autre que UTF-8 et UTF-8 with BOM peuvent causer des problèmes mais vous n'avez pas à vous en soucier car par défaut avec Ren'Py ils sont en UTF-8

### Echappements
Certains echappements ont des problèmes. 

1. L'échappement du \n n'est pas pris en charge
2. les echappemets de guillemets sont pris en charge mais contient des erreurs mineures. exemple: 'je \\'mange\\'' traduit en anglais devient 'I\\'m eating\\'' traduction exacte : 'I\\'m \\'eating\\''
3. des espaces en trop peuvent se rajouter. "ce \\"texte\\" par exemple" devient "This \\ "text \\" for example" au lieu de "This \\"text\\" for example"

## A venir 
Le système de fichier json n'a pas été mis pour l'instant. Il sera intégré lorsque le code fonctionnera parfaitement et sera expliqué

Un système de traduction de tous les fichiers rpy d'un répertoire sera ajouté également

Les erreurs cités précédemment seront bien sûr corrigées


## License

Ren'Py Novel Translation est sous licence `CC-BY-SA 4.0`. Veullez voir la [section license](https://github.com/cherifVN/Ren-Py-Novel-Translation?tab=CC-BY-SA-4.0-1-ov-file) ou directement depuis [LICENSE-CC-BY-SA.txt](LICENSE-CC-BY-SA.txt)

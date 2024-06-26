# modules
import os
import re
from googletrans import Translator
import json


# verif json
if os.path.exists("translated_cache.json"):
    with open("translated_cache.json", "r", encoding='utf-8') as f:
        translation_dictionary = json.load(f)


# variables +
translator = Translator()
translation_dictionary = {}
translated_dialogue = ''
slash_quote_start = 0
slash_quote_end = 0
spaces_at_start = 0
spaces_at_end = 0
fichier = input("Nom du fichier sans l'extension: ")
fichiercible = fichier + "_traduit.rpy"
fichier += ".rpy"
langue_source = input("Langue d'origine: ")
langue_cible = input("Langue cible: ")

if not os.path.exists(fichier):
    print("Le fichier n'existe pas")
    exit(1)


### fonctions ###
# simple quotes
def escape_simple_quotes():
    global translated_dialogue
    global dialogue_filtered
    global slash_quote_end
    global slash_quote_start
    global spaces_at_start
    global spaces_at_end

    while dialogue_filtered.startswith(" "):
        spaces_at_start += 1
        dialogue_filtered = dialogue_filtered[1:]

    while dialogue_filtered.startswith("\\'"):
        slash_quote_start += 1
        dialogue_filtered = dialogue_filtered[2:]

    while dialogue_filtered.endswith(" "):
        spaces_at_end += 1
        dialogue_filtered = dialogue_filtered[:-1]

    while dialogue_filtered.endswith("\\'"):
        slash_quote_end += 1
        dialogue_filtered = dialogue_filtered[:-2]
    
    #dialogue_filtered = dialogue_filtered.replace("\\'", "'")
    try:
        translated_dialogue = translator.translate(dialogue_filtered, src=langue_source, dest=langue_cible).text
    except Exception as e:
        print(e)
        global error
        error = True 
    
    translated_dialogue = translated_dialogue.replace("'", "\\'")
    for s in range(spaces_at_start):
        translated_dialogue = " " + translated_dialogue

    for i in range(slash_quote_start):
        translated_dialogue = "\\'" + translated_dialogue 

    for e in range(spaces_at_end):
        translated_dialogue = translated_dialogue + " "
    
    for i in range(slash_quote_end):
        translated_dialogue = translated_dialogue + "\\'"

    translated_dialogue = f"'{translated_dialogue}'"

# double quotes    
def escape_double_quotes():
    global dialogue_filtered
    global translated_dialogue
    global slash_quote_start
    global slash_quote_end
    global spaces_at_start
    global spaces_at_end

    
    while dialogue_filtered.startswith(" "):
        spaces_at_start += 1
        dialogue_filtered = dialogue_filtered[1:]

    while dialogue_filtered.startswith('\\"'):
        dialogue_filtered = dialogue_filtered[2:]
        slash_quote_start += 1
    
    while dialogue_filtered.endswith(" "):
        spaces_at_end += 1
        dialogue_filtered = dialogue_filtered[:-1]


    if dialogue_filtered.endswith('\\"'):
        dialogue_filtered = dialogue_filtered[:-2]
        slash_quote_end += 1
        escape_double_quotes()
        return
    
    try:
        translated_dialogue = translator.translate(dialogue_filtered, src=langue_source, dest=langue_cible).text
    except Exception as e:
        print(e)
        global error
        error = True

        
    for s in range(spaces_at_start):
        translated_dialogue = " " + translated_dialogue

    for e in range(spaces_at_end):
        translated_dialogue = translated_dialogue + " "

    
    for i in range(slash_quote_start):
        translated_dialogue = '\\"' + translated_dialogue

    for i in range(slash_quote_end):
        translated_dialogue = translated_dialogue + '\\"'

    translated_dialogue = f'"{translated_dialogue}"'


##### main #####
# ouvrir les fichier source et cible 
with open(fichiercible, 'w+', encoding='utf-8') as f_cible:
    with open(fichier, 'r', encoding='utf-8') as f_source:
        # define line
        for line in f_source:
            slash_quote_start = 0
            slash_quote_end = 0
            simple_quote_dialogue = False
            double_quote_dialogue = False
            error = False
            spaces_at_end = 0
            spaces_at_start = 0

            # si la ligne n'est pas un commentaire ou old (elle peut contenir des dialogues)
            if not line.strip().startswith("#") and not line.strip().startswith("old"):
                # filtrer les dialogues entre guillemets
                dialogue = re.search(r'"((?:\\"|[^"])*?)"|\'((?:\\\'|[^\'])*?)\'', line)
                if dialogue:
                    dialogue = dialogue.group()
                    if dialogue not in translation_dictionary:
                        # variables
                        vars = re.findall(r'\[(.*?)\]', dialogue)
                        dialogue_filtered = re.sub(r'\[(.*?)\]', '[...]', dialogue)
                        # Filtrer les balises
                        tags = re.finditer(r'({(.*?)})+', dialogue_filtered)
                        tags = [tag.group(0) for tag in tags]
                        for tag in tags:
                            dialogue_filtered = dialogue_filtered.replace(tag, "{...}", 1)

                        # échappement de guillemets 
                        if dialogue_filtered.startswith("'"):
                                dialogue_filtered = dialogue_filtered[1:]
                                simple_quote_dialogue = True
                        
                        if dialogue_filtered.endswith("'"):
                                dialogue_filtered = dialogue_filtered[:-1]
                                simple_quote_dialogue = True

                        if simple_quote_dialogue == True:
                                escape_simple_quotes()
                        
                        if dialogue_filtered.startswith('"'):
                            dialogue_filtered = dialogue_filtered[1:]
                            double_quote_dialogue = True
                        
                        if dialogue_filtered.endswith('"'):
                            dialogue_filtered = dialogue_filtered[:-1]
                            double_quote_dialogue = True

                        if double_quote_dialogue == True:
                            escape_double_quotes()

                            
                        
                        for tag in tags:
                            tag = f"{tag}"
                            translated_dialogue = translated_dialogue.replace("{...}", tag, 1)

                        # restaurer les variables
                        for var in vars:
                            var = f"[{var}]"
                            translated_dialogue = translated_dialogue.replace("[...]", var, 1)
                            
                        if error == False:
                            print(translated_dialogue)
                            translation_dictionary[dialogue] = translated_dialogue

                   
                    else:  # if dialogue is in translation dictionary
                        translated_dialogue = translation_dictionary[dialogue]
                    

                    if error == False:
                        f_cible.write(f"{line.replace(dialogue, translated_dialogue)}")
                    else:
                        f_cible.write(line)
                
                # si il y a pas de dialogue 
                else:
                    f_cible.write(f"{line}")
            else:
                f_cible.write(f"{line}")
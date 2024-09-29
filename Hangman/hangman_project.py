# 16.1 Projekt 1: Hangmann

# 16.1.1 Ziel:

# Entwickeln Sie ein einfaches Hangman-Spiel in Python. Bei diesem Spiel soll der Spieler
# ein Wort erraten, indem er Buchstaben vorschlägt. Bei jedem falschen Versuch kommt der “Hangman” (Galgenmännchen) ein Stück näher zu seiner Vollendung.

# 16.1.2 Spezifikationen:
# • Wortauswahl:
#       – Das Spiel beginnt mit einem zufällig ausgewählten Wort aus einer vordefinierten Liste von Wörtern.

# • Spiellogik:
#       – Der Spieler kann Buchstaben vorschlagen, um das Wort zu erraten.
#       – Jeder falsche Buchstabe führt dazu, dass der Hangman weiter aufgebaut wird.
#       – Der Spieler gewinnt, wenn er das Wort errät, bevor der Hangman vollständig ist.

# • Anzeige des Fortschritts:
#       – Zeigen Sie nach jedem Versuch den aktuellen Stand des Wortes (welche Buchstaben erraten wurden) und den Zustand des Hangman an.

# • Maximale Versuche:
#       – Legen Sie eine maximale Anzahl von Fehlversuchen fest, bevor das Spiel verloren ist.

# • Fehlerbehandlung:
#       – Stellen Sie sicher, dass nur gültige Buchstaben eingegeben werden können.
import random

def wort_wahl():
    # Wörterliste wird hier vergeben
    word_list = ["affe", "hund", "apfel", "klettergerüst", "waldbrand", "grundierung"]
    # random.choice nimmt ein zufälliges wort aus der liste
    random_word = random.choice(word_list)
    # random_word = str(random_word)
    
    return random_word 


def hangman(): 
    random_word = wort_wahl()
    # print(random_word)

    print("Wilkommen bei Hangman :) ")
    print("----------------------")
    print("Gib Buchstaben ein um das Spiel zu spielen!")
    print("----------------------")
    print("Für jeden falschen Buchstaben, baut sich der Hangman auf, bei sieben falschen Eingaben, hast du das Spiel verloren!")

    hangman_list = list("hangman")
    hangman_hidden = ["_"] * len(hangman_list)
    hangman_counter = 0
    random_word_win = list(random_word)
    hidden_word = ["_"] * len(random_word)
    loose_counter = len("hangman")
    print("----------------------")
    print("Dies ist das zu erratende Wort:", hidden_word)
    print("----------------------")
    random_word_list = list(random_word)
    
    
    while True:
        user_input = input("Gib einen Buchstaben ein: ").lower()
        print("----------------------")
        if user_input in random_word_list:
            
            # for loop checkt wie oft ein user_input in random_wort_list vorkommt
            for x in random_word_list:
                if x == user_input:
                    # prüfe welchen index der user input hat
                    index_input = random_word_list.index(user_input)
                    random_word_list.pop(index_input)
                    random_word_list.insert(index_input, "_")

                # entfernt "_" im rätselwort und fügt user_input hinzu
                    hidden_word.pop(index_input)
                    hidden_word.insert(index_input, user_input)
                    print("Buchstabe richtig")
                    print("----------------------")
                    print(hidden_word)
                    print("----------------------")

          
        else:
           hangman_hidden[hangman_counter] = hangman_list[hangman_counter]
           hangman_counter += 1
           loose_counter -= 1
           print("Falscher Buchstabe!")
           print("----------------------")
           print(hangman_hidden)
           print("----------------------")
           print(f" Du hast noch {loose_counter} Versuche!")
           print("----------------------")

        if random_word_win == hidden_word:
            print("Du hast das Spiel gewonnen!")
            print("----------------------")

            break

        elif hangman_list == hangman_hidden:
            print("Du hast das Spiel verloren!")
            print("----------------------")
            
            break

    if input("Möchtest du nochmal Spielen? j für ja alles andere für nein:") == "j":
        print("----------------------")
        print("Spiel wird ausgeführt.")
        print("----------------------")
        
        hangman()
    else:
        print("----------------------")
        print("Spiel wird beendet.")
        print("----------------------")

        exit(0)


hangman()




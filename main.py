from view.speakerview import SpeakerView

from view.conferenceview import ConferenceView

import time

import os

if __name__ == "__main__":
    # Main file acting like a routing system
    speaker = SpeakerView()
    conference = ConferenceView()
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Bienvenue sur votre systeme de gestion des conferenciers et conferences ")
    time.sleep(1)  # display remains for 1 sec
    print(
        "Que souhaitez vous gerer les conferences ou les conferenciers ? tapez sur c pour les conferences , s pour les conferenciers q pour quitter")
    answer = input("entrez votre choix :")  # Call the right action function according to user input
    while answer != "q":
        if answer == "c":
            print("que souhaitez vous faire ? a : ajouter , m : modifier , r : supprimer , e : quitter")
            while answer != "e":
                answer = input("entrez votre choix :")
                if answer == "a":
                    conference.new_conference()  # add conference
                    print("vous avez ajouter une conférence !")
                elif answer == "m":
                    conference.to_update_conference()  # modify conference
                    print("vous avez modifier une conference")
                elif answer == "v":
                    conference.show_conferences()  # display every conferences
                elif answer == "r":
                    conference.remove_conference()  # delete conference
                    print("vous avez supprimer un conference")
                else:
                    exit()

        elif "s" == answer:
            while answer != "e":
                speaker.show_speakers()
                print("que souhaitez vous faire ? a : ajouter , m : modifier , r : supprimer,  q : quitter")
                answer = input("entrez votre choix :")
                if answer == "a":
                    speaker.new_speaker()
                    print("vous avez ajouter un conferencier")
                elif answer == "m":
                    speaker.to_update_speaker()
                    print("vous avez modifier un conferencier")
                elif answer == "r":
                    speaker.remove_speaker()
                    print("vous avez supprimer un conferencier")

                else:
                    exit()

        else:
            exit()

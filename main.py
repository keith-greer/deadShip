import time
from medic_path import get_medic_path 
from typing_print import typingPrint
#defines the typingPrint function


# Define a list of character styles
character_styles = ["Medic", "Engineer", "Technician"]  # Add more character styles as needed

# Define a dictionary to map character styles to their descriptions
character_descriptions = {
    "Medic": "As you awaken on the ship in the aftermath of an explosion, your focus remains on the critical tasks ahead. The ship's systems are in disarray, and your nurturing instincts come to the fore. In the role of a Medic, you embark on a mission to mend both the ship's failing components and the physical well-being of its crew. Armed with a trusty medical kit, you navigate the dimly lit corridors`, quietly working to heal and restore, all while keeping an eye on the ticking clock of urgency.",
   "Medic": "As you awaken on the ship in the aftermath of an explosion, your focus remains on the critical tasks ahead. The ship's systems are in disarray, and your nurturing instincts come to the fore. In the role of a Medic, you embark on a mission to mend both the ship's failing components and the physical well-being of its crew. Armed with a trusty medical kit, you navigate the dimly lit corridors`, quietly working to heal and restore, all while keeping an eye on the ticking clock of urgency.",
    "Engineer": "Emerging from the aftermath of a sudden explosion, you find yourself on a damaged starship. The ship's power core is faltering, and your technical expertise becomes invaluable. As a Mechanical Engineer, you wield your toolkit with precision, striving to revive the ship's mechanical systems one step at a time. As you traverse the ship's passageways, you methodically piece together both the ship's functions and your own identity, all beneath the steady hum of urgency.",
    "Techician": "Waking up amidst the chaos of a ship damaged by an explosion, you discover yourself aboard a crippled starship. The ship's digital infrastructure is in turmoil, and your affinity for coding and hacking takes center stage. In the role of a Computer Technician, you embark on a quest to reboot the ship's digital core. Amidst the lines of code and data fragments, you also aim to uncover the secrets of your own past. Your journey unfolds quietly, with each keystroke holding the power to save the ship and unlock the enigma of your own existence, all while racing against the relentless countdown of time.",
    # Add more character styles and descriptions as needed
}




messages = [
    "Welcome to my simple game, enjoy!!!",
    "      .....",
    "      .....",
    "      .....",
    "      .....",
    "      .....",
    "  ..KEEFUSOFT..",
    "      .....",
    "      .....",
    "  ..presents..",
    "      .....",
    "      .....",
    " ..DeadStation..",
    "      .....",
    "      .....",
    "      ....."
]

for message in messages:
    print(message)
    time.sleep(0.5)





print("\nChoose a character class from the following options:")
for i, location in enumerate(character_styles, start=1):
    print(f"{i}. {location}")

while True:
    character_choice = input("Enter the number corresponding to your character's class: ")
    if character_choice.isdigit():
        character_choice = int(character_choice)
        if 1 <= character_choice <= len(character_styles):
            selected_character_style = character_styles[character_choice - 1]
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            typingPrint("Character class: ")
            typingPrint( selected_character_style)
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            
            # Retrieve and print the description for the selected character class
            character_description = character_descriptions.get(selected_character_style, "Description not available")
            
            typingPrint(character_description)
            break
        
        else:
            print("Invalid input. Please choose a valid number.")
    else:
        print("Invalid input. Please enter a number.")
        print(".")
        print(".")

        get_medic_path()

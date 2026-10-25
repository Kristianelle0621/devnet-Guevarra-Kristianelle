import requests
import random

def randomizer(): 
    random_id = random.randint(1, 1351)
    pokemon = f"https://pokeapi.co/api/v2/pokemon/{random_id}"
    api = requests.get(pokemon)
         
    info = api.json()
    print("\nGuess the pokemon!!")
    print(f"\nThis Pokemon's ID is: {info['id']}")
    print(f"The Height is: {info['height']}")
    print(f"The Weight is: {info['weight']}")
    
    
    abilities = info["abilities"]
    print("The Abilities are: ")         
    for ability_item in abilities:
        print(ability_item["ability"]["name"])
        
    return info

def play():
    info = randomizer()
    for attempt in range(1, 5):
        answer = input("\nWho's That Pokemon: ").lower()
        if answer == info["name"]:
            print("\nYou Guessed Right!")
            break
        else:
            if attempt == 4:
                print("\nSkill issue!")
                print(f"The answer is {info['name']}")
                break
            else:
                print(f"\n Wrong answer!, {attempt} / 3 Chance")
        
def main():
    while True:
        choice = input("\nPlay the game? [1/2]: ")
        if choice == "1":
            play()    
        elif choice == "2":
            print("Goodbye")
            break
        else:
            print("Error")

main()

import speech_recognition as sr
print("Greetings, ufood bot welcomes you. Please select from the below menu.")
print('\n')
print("Menu:")
print("1. Appetizer")
print("2. veg")




def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio=recognizer.listen(source)
            try:
    #            speechtx("Recognizing...")
                print(("Recognizing..."))
                data=recognizer.recognize_google(audio,language='en-in')
                return data
            except sr.UnknownValueError:
                print("Sorry, i can't understand, Please use the keywords from main menu")
if __name__=='__main__':
        query=sptext().lower()
        if "appetizer" in query:
            starters={"Fries":"CCB","Pizza Puff":"CCB","Veg Kulcha":"CCB","White Pasta":"Chaat Bhandaar","Red Pasta":"Chaat Bhandaar",
        "Bun Tikki":"Chaat Bhandaar","chana tikki chat":"Chaat Bhandaar","Spicy Chicken Roll":"Chai Nagri",
        "Mutton Keema Roll":"Chai Nagri","Veg Tortilla":"Burger kingdom","Egg Tortilla":"Burger kingdom",
        "Chicken malai tortilla":"Burger kingdom"}
            print(starters)
        elif "veg" in query:
            vegstarters={"Fries":"CCB","Pizza Puff":"CCB","Veg Kulcha":"CCB","White Pasta":"Chaat Bhandaar","Red Pasta":"Chaat Bhandaar",
        "Bun Tikki":"Chaat Bhandaar","chana tikki chat":"Chaat Bhandaar","Veg Tortilla":"Burger kingdom"}
            print(vegstarters)
        else:
            exit(0)

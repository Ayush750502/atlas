
#feature setup of the speaker(eg. male/female speaker,speed of narration etc.)
import pyttsx3
engine = pyttsx3.init('sapi5')
engine.setProperty('rate',150)
engine.setProperty('volume',1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# speak function for system output in voice : 
def speak(text):
    engine.say(text)
    engine.runAndWait()

#continentsAndContries = ['Africa' , 'Antarctica' , 'Australia' , 'Asia','Afghanistan','Albania','Algeria','Andorra','Angola','Antigua and Barbuda','Argentina','Armenia','Australia','Austria','Azerbaijan','Bahamas','Bahrain','Bangladesh','Barbados','Belarus','Belgium','Belize','Benin','Bhutan','Bolivia','Bosnia and Herzegovina','Botswana','Brazil','Brunei','Bulgaria','Burkina Faso','Burundi','Europe','North America','South America',"Cambodia","Cameroon","Canada","Cabo Verde","Central African Republic","Chad","Chile","China","Colombia","Comoros","Congo, Democratic Republic of the","Congo, Republic of the","Costa Rica","Cote d'Ivoire","Croatia","Cuba","Curacao","Cyprus","Czechia","Denmark","Djibouti","Dominica","Dominican Republic","East Timor","Ecuador","Egypt","El Salvador","Equatorial Guinea","Eritrea","Estonia","Ethiopia","Fiji","Finland","France","Gabon","Gambia","Georgia","Germany","Ghana","Greece","Grenada","Guatemala","Guinea","Guinea-Bissau","Guyana","Haiti","Holy See","Honduras","Hong Kong","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Israel","Italy","Jamaica","Japan","Jordan","Kazakhstan","Kenya","Kiribati","Korea, North","Korea, South","Kosovo","Kuwait","Kyrgyzstan","Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg","Macau","Macedonia","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Marshall Islands","Mauritania","Mauritius","Mexico","Micronesia","Moldova","Monaco","Mongolia","Montenegro","Morocco","Mozambique","Namibia","Nauru","Nepal","Netherlands","New Zealand","Nicaragua","Niger","Nigeria","North Korea","Norway","Oman","Pakistan","Palau","Palestinian Territories","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal","Qatar","Romania","Russia","Rwanda","Saint Kitts and Nevis","Saint Lucia","Saint Vincent and the Grenadines","Samoa","San Marino","Sao Tome and Principe","Saudi Arabia","Senegal","Serbia","Seychelles","Sierra Leone","Singapore","Sint Maarten","Slovakia","Slovenia","Solomon Islands","Somalia","South Africa","South Korea","South Sudan","Spain","Sri Lanka","Sudan","Suriname","Swaziland","Sweden","Switzerland","Syria","Taiwan","Tajikistan","Tanzania","Thailand","Timor-Leste","Togo","Tonga","Trinidad and Tobago","Tunisia","Turkey","Turkmenistan","Tuvalu","Uganda","Ukraine","United Arab Emirates","United Kingdom","Uruguay","Uzbekistan","Vanuatu","Venezuela","Vietnam","Yemen","Zambia","Zimbabwe"]

#function that greets the user
from datetime import datetime
def greet_user():
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak("Good Morning Everyone")
    elif (hour >= 12) and (hour < 16):
        speak("Good afternoon Everyone")
    elif (hour >= 16) and (hour < 23):
        speak("Good Evening Everyone")
    speak("Welcome! Lets play Atlas .")
greet_user()


#function that takes user's spoken command as input
import speech_recognition as sr
def user_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        if not 'execut' in query or 'terminate' in query or 'stop' in query:
            return query
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            exit()
    except Exception:
        speak('Sorry, I could not understand. Could you please speeak it again!')
        return user_input()
        
# gameplay type countries and continent type atlas
def international():
    continentsAndContries = ['America','Africa','Antarctica','Australia','Asia','Afghanistan','Albania','Algeria','Andorra','Angola','Antigua and Barbuda','Argentina','Armenia','Australia','Austria','Azerbaijan','Bahamas','Bahrain','Bangladesh','Barbados','Belarus','Belgium','Belize','Benin','Bhutan','Bolivia','Bosnia and Herzegovina','Botswana','Brazil','Brunei','Bulgaria','Burkina Faso','Burundi','Europe','North America','South America',"Cambodia","Cameroon","Canada","Cabo Verde","Central African Republic","Chad","Chile","China","Colombia","Comoros","Congo, Democratic Republic of the","Congo, Republic of the","Costa Rica","Cote d'Ivoire","Croatia","Cuba","Curacao","Cyprus","Czechia","Denmark","Djibouti","Dominica","Dominican Republic","East Timor","Ecuador","Egypt","El Salvador","Equatorial Guinea","Eritrea","Estonia","Ethiopia","Fiji","Finland","France","Gabon","Gambia","Georgia","Germany","Ghana","Greece","Grenada","Guatemala","Guinea","Guinea-Bissau","Guyana","Haiti","Holy See","Honduras","Hong Kong","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Israel","Italy","Jamaica","Japan","Jordan","Kazakhstan","Kenya","Kiribati","Korea, North","Korea, South","Kosovo","Kuwait","Kyrgyzstan","Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg","Macau","Macedonia","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Marshall Islands","Mauritania","Mauritius","Mexico","Micronesia","Moldova","Monaco","Mongolia","Montenegro","Morocco","Mozambique","Namibia","Nauru","Nepal","Netherlands","New Zealand","Nicaragua","Niger","Nigeria","North Korea","Norway","Oman","Pakistan","Palau","Palestinian Territories","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal","Qatar","Romania","Russia","Rwanda","Saint Kitts and Nevis","Saint Lucia","Saint Vincent and the Grenadines","Samoa","San Marino","Sao Tome and Principe","Saudi Arabia","Senegal","Serbia","Seychelles","Sierra Leone","Singapore","Sint Maarten","Slovakia","Slovenia","Solomon Islands","Somalia","South Africa","South Korea","South Sudan","Spain","Sri Lanka","Sudan","Suriname","Swaziland","Sweden","Switzerland","Syria","Taiwan","Tajikistan","Tanzania","Thailand","Timor-Leste","Togo","Tonga","Trinidad and Tobago","Tunisia","Turkey","Turkmenistan","Tuvalu","Uganda","Ukraine","United Arab Emirates","United Kingdom","Uruguay","Uzbekistan","Vanuatu","Venezuela","Vietnam","Yemen","Zambia","Zimbabwe"]
    print("International type !")
    speak("International type !")
    endGame = ['exit','quit','end']
    played = []
    scr = 0
    print("To quite game , just speak one of these words :",endGame,':-')
    player = user_input().lower()
    print('>>>Player ',player)
    ch = player[0].lower()
    while not player in endGame :
        idx = 0
        check = 0
        if player in endGame :
            speak("Quitting game !")
            break
        if player[0].lower() == ch.lower():
            for i in continentsAndContries :
                i = i.lower()
                if i in player :
                    played.append(continentsAndContries.pop(idx))
                    check += 1
                    break
                idx+=1
        
        if check == 0 :
            if player in played :
                speak(player+" is already been played.")
            elif player[0].lower() != ch.lower():
                speak("Hey don't cheat initial letter of last used word does not matches with first letter of term you used")
            else :
                speak("Hey there is no such country or contient !")
            player = user_input().lower()
            print(">>>Player",player)
            continue
        ch = player[-1]
        idx = 0
        for i in continentsAndContries :
            i = i.lower()
            if ch.lower() == i[0]:
                print("Computer :",i)
                speak(i)
                ch = i[-1].lower()
                played.append(continentsAndContries.pop(idx))
                break
            idx+=1
        scr +=1
        player = user_input().lower()
        print(">>>Player",player)
    print('We just played :',played)
    print('Your score :',scr)
    speak('Your score : '+str(scr))

# initiating game function
def initiating():
    international()
    print("Waana have a rematch(yes/no)")
    speak("Waana have a rematch! yes or no")
    re = user_input().lower()
    if 'yes' in re :
        initiating()
    elif 'no' in re :
        speak("It was a good match! Thank you!")
    speak("Have a good time!")

initiating()







import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os
import openai
import random
import google

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)  

def ai(prompt):
    openai.api_key = "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"
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        response_text = response["choices"][0]["message"]["content"]
        print(response_text)
        text += response_text

        if not os.path.exists("Openai"):
            os.mkdir("Openai")

        with open(f"Openai/prompt-{random.randint(1, 2343434356)}.txt", "w") as f:
            f.write(text)

    except Exception as e:
        print(f"An error occurred: {e}")
        text += "\nAn error occurred while generating the response."

    return text

    openai.api_key = "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"
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)

chatStr = ""
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = "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"
    chatStr += f"User: {query}\nflora: "
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": chatStr}
            ]
        )
        response_text = response["choices"][0]["message"]["content"]
        say(response_text)
        chatStr += f"{response_text}\n"
        return response_text

    except openai.error.OpenAIError as e:
        print(f"An error occurred: {e}")
        return "An error occurred while generating the response."



def speak(audio):
    engine.say(audio)
    engine.runAndWait() 

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("hello sir, good morning")
    elif hour >= 12 and hour < 18:
        speak("hello sir, good after noon ")
    else:
        speak("HELLO , SIR")
    speak("I AM FLORA. HOW MAY I HELP YOU")

def takecommand():
    # it takes microphone input from the user and gives string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....") 
        r.pause_threshold = 0.6
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print(e)    
        print("say that again please...")
        return "none"
    return query    

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        # LOGIC FOR EXECUTING TASK BASED ON QUERY
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=10)
            speak("according to wikipedia")

        if 'google' in query:
            speak('searching google...')
            query = query.replace("google", "")
            result = wikipedia.summary(query, sentences=10)
            speak("according to google")

            print(result)
            speak(result)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'twitter' in query:
            webbrowser.open("twitter.com")
        elif 'instagram' in query:
            webbrowser.open("instagram.com")
        elif 'linkedin' in query:
            webbrowser.open("linkedin.com")    
        elif 'gmail' in query:
            webbrowser.open("gmail.com")  
        elif 'facebook' in query:
            webbrowser.open("facebook.com")
        elif 'Google Map' in query:
            webbrowser.open("google maps.com") 
        elif 'play music' in query:
            # music_dir = 'D:\\non critical\\songs\\favorite songs2'm
            music_dir = 'C:\\Users\\Manmit  Kumar\\Music'
            songs = os.listdir(music_dir)
            if songs:  # Check if the list is not empty
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))
            else:
                speak("No songs found in the directory.")
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strtime}")
        elif 'open code'in query:
            codepath = "C:\\Users\\Manmit  Kumar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"     
            os.startfile(codepath)
        elif 'open pictures' in query:
            pictures = "C:\\Users\\Manmit  Kumar\\Pictures"  

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)

        
        # say(query)


       


        # thank you and best regards
        # VIPUL KUMAR YADAV 
        #   FILHAAL BEROJAGAR 




            







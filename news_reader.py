def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == "__main__":
    
    speak("News for today")
    import requests
    import json
    url = "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=89d55daff40d418eace3f13fa1b2ca1a"
    req = requests.get(url).text
    parsed = json.loads(req)
    art = parsed['articles']
    print(art)
    
    for article in art:
        speak(article['title'])
        speak("Moving to the next news ,listen carefully")
    speak("Thanks for listening bitch")
import speech_recognition as sr
import requests
import pyttsx3
import webbrowser
import wolframalpha
from firebase import firebase
#from spotify_local import SpotifyLocal
import datetime
import os
import sys
import wikipedia
import smtplib
from PyDictionary import PyDictionary

#musixmatch API key: d4c6d2b06d5c0efd07a558fdfd9a237d

app_id = "4GYHPG-3K88PA567X"
client = wolframalpha.Client('4GYHPG-3K88PA567X')
# APP NAME: Voice assistant
# APPID: 4GYHPG-3K88PA567X
# USAGE TYPE: Personal/Non-commercial Only
fbcom=firebase.FirebaseApplication('https://voice-assistant-50b0c.firebaseio.com/')

def speak(s):
    engine=pyttsx3.init()
    engine.say(s)
    data={"response":s}
    res=fbcom.post('/mySE_test',data)
    engine.runAndWait()

def weather():
    res=requests.get("https://ipinfo.io")
    data=res.json()
    city=data['city']   
    a='https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=25fbb8bfdf839edb698b98f45a4d6451'
    q=requests.get(a)
    w=q.json()
    f=w['weather'][0]['description']
    g="There will be "+f
    print(g)
    speak(g)

def jokes():
	api="http://api.icndb.com/jokes/random"
	req=requests.get(api)
	j=req.json()
	g=j['value']['joke']
	print(g)
	speak(g)

def wra(text):
    res = client.query(text)
    answer = next(res.results).text 
    print(answer)
    speak(answer)

def wiki(text):
	results=wikipedia.summary(text, sentences=2)
	print("According to wikipedia")
	speak("According to wikipedia")
	print(results)
	speak(results)

def mycommand():
	r = sr.Recognizer()
	with sr.Microphone() as source:
	    r.pause_threshold=1
	    r.adjust_for_ambient_noise(source,duration=1)
	    print("Listening...")
	    audio = r.listen(source)
	try:
		text = r.recognize_google(audio)
		print(text)
		data={"command":text}
		res=fbcom.post('/mySE_test',data)
	except:
		print("Sorry I didn\'t quite get that, try typing the command")
		speak("Sorry I didn\'t quite get that, try typing the command")
	return text

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
    	print('Good Morning!')
    	speak('Good Morning!')
        
    if currentH >= 12 and currentH < 18:
    	print('Good Afternoon!')
    	speak('Good Afternoon!')
        
    if currentH >= 18 and currentH !=0:
    	print('Good Evening!')
    	speak('Good Evening!')
        
    print('Hello Sir')
    speak('Hello Sir')
    print('How may I help you?')
    speak('How may I help you?')

#greetMe()
while True:
	
		text=mycommand();
		try:
			if 'weather' in text:
				weather()
			elif 'exit' in text or 'abort' in text or 'stop' in text or 'close' in text:
				break
			elif 'open browser' in text:
				webbrowser.open('https://www.google.com', new=2)
			elif 'joke' in text or 'entertain' in text or 'laugh' in text or 'smile' in text:
				jokes()
			elif 'email' in text:
				print("Who is the recipient?")
				speak('Who is the recipient? ')
				recipient = mycommand()
				if 'myself' in recipient:
					try:
						print("What should I say?")
						speak('What should I say?')
						content = mycommand()
						server = smtplib.SMTP('smtp.gmail.com', 587)
						server.ehlo()
						server.starttls()
						server.login("joshi.gaurav@sitpune.edu.in", 'Gauravjoshi1')
						server.sendmail('joshi.gaurav@sitpune.edu.in', "harshil.shrivastava@sitpune.edu.in", content)
						server.close()
						print("Email sent")
						speak('Email sent!')

					except:
						print("Sorry Sir! I am unable to send your message at this moment!")
						speak('Sorry Sir! I am unable to send your message at this moment!')
			else:
				try:
					try:
						wra(text)
					except:
						wiki(text)	
				except:
						webbrowser.open(www.google.com)	
		except:
			print("Sorry I didn\'t quite get that, try typing the command")
			speak("Sorry I didn\'t quite get that, try typing the command")
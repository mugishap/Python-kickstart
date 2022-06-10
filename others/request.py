from tkinter import *
import requests
import webbrowser
window =  Tk()


window.title("My first Python GUI")
window.geometry('350x200')


query = input("Search here: ")

url = "https://youtube-search9.p.rapidapi.com/snc/{}".format(query)

headers = {
	"X-RapidAPI-Key": "a6a50747c6msh3b9df5163dc6c28p1bb422jsn7f9f8d1462fc",
	"X-RapidAPI-Host": "youtube-search9.p.rapidapi.com"
}

data = requests.get(url, headers=headers).json()


response = data['result']


for i in response:

	t = Text(window,height=5,width=52)
	l = Label(window,text="{}".format(i['title']))
	l.config(font =("Courier", 14))
	l.pack()
	t.pack()

window.mainloop()

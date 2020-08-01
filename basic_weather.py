from tkinter import *
import requests
import json

root = Tk()
root.title("Weather App")
root.geometry("700x400")
root.configure(background = "black")



# http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=5&API_KEY=6EFD0188-43D5-491F-88B3-C156371654C9


try:
    api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=5&API_KEY=6EFD0188-43D5-491F-88B3-C156371654C9")
    api = json.loads(api_request.content)
    
    city = api[0]['ReportingArea']
    quality = api[0]['AQI']
    category = api[0]['Category']['Name']
                               
except Exception as e:
    api = "Error..."                           



myLabel = Label(root, text=city + " Air Quality " + str(quality) + "  " + category, font=("Helvetica", 20), background="yellow")
myLabel.pack()


root.mainloop()

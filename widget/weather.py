#!/usr/bin/python3

from tkinter import *
import requests


# API = Insert your own API key 
# API current time = api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}


def get_weather(city):
    # Function that get the information
    try:
        api_key = "" # The code will only work if you use your API key for openweathermap

        url = "https://api.openweathermap.org/data/2.5/weather"

        api_parameters = {"APPID": api_key, "q": city,
                          "units": "metric"}  # Parameters for the API

        weather_request = requests.get(
            url, params=api_parameters)  # Request to the API

        weather_response = weather_request.json()  # Get a response from the API

        city_label["text"] = weather_response["name"]

        description_label["text"] = weather_response["weather"][0]["description"]

        weather_label["text"] = str(weather_response["main"]["temp"]) + " °C"
    except:
        city_label["text"] = ""

        description_label["text"] = ""

        weather_label["text"] = "Wrong city,\n or API key"
    # Used to avoid an  Error


# Main Window
window = Tk()
window.title("Weather App")
window.geometry("400x550")

Welcome_label = Label(window, text="Hi!, where are you?",
                      font=("Courier", 15, "italic"))
Welcome_label.pack()

# weather entry
place_entry = Entry(window, font=("Courier", 20), justify="center")
place_entry.pack(padx=30, pady=30)

check_button = Button(window, text='Get weather', font=(
    "Courier", 20), command=lambda: get_weather(place_entry.get()))
check_button.pack()

city_label = Label(window, font=("Courier", 20))
city_label.pack(padx=30, pady=30)

weather_label = Label(window, font=("Courier", 35))
weather_label.pack(padx=30, pady=30)

description_label = Label(window, font=("Courier", 20))
description_label.pack(padx=30, pady=30)

window.mainloop()

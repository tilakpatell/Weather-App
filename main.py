import customtkinter as ctk
import requests 
import tkintermapview as tkmap
from PIL import Image, ImageTk


API_KEY = '39ddea89727e5c431638cb569eca853e'
#API_URL = 

app = ctk.CTk()
app.title("Weather App")
#app.iconbitmap("icon.ico")
app.geometry("700x400")
app.resizable(False, False)
app.config(bg="#fff")

icon = app.iconbitmap("weather.ico")

frame = ctk.CTkFrame(app, width=700, height=400)
frame.place(x=200, y=0)

frame_2 = ctk.CTkFrame(app, width=200, height=400, fg_color= "#fff")
frame_2.place(x=0, y=0)

stringvariable = ctk.StringVar()
def get_city():
    tkmap_view.set_address(city_entrybox.get())

IMAGE_PATH = Image.open('searchbar-removebg-preview.png')
Search_bar = IMAGE_PATH.resize((300, 370))
ctk_img = ImageTk.PhotoImage(Search_bar)

IMAGE_2_PATH = Image.open('weather.png')
weather_img = IMAGE_2_PATH.resize((200,200))
ctk_img_2 = ImageTk.PhotoImage(weather_img)

label_1 = ctk.CTkLabel(frame_2, image= ctk_img)
label_1.place(x=0, y=-95)


tkmap_view = tkmap.TkinterMapView(frame, width=900, height=900)
tkmap_view.place(x=0, y=0)

def get_city():
    tkmap_view.set_address(city_entrybox.get())
    selected_location = city_entrybox.get()
    get_weather(selected_location)
    
    

    
city_entrybox = ctk.CTkEntry(frame_2, width=175,height = 35, font=("Arial", 20), textvariable=stringvariable,)
city_entrybox.place(x=12.5, y=13)

city_button = ctk.CTkButton(frame_2, text="Search", width=175, height=1, font=("Arial", 20), command=get_city, fg_color="LIGHTGRAY")
city_button.place(x=12.5, y=60)

city = city_entrybox.get()

    
label_2 = ctk.CTkLabel(frame_2, image= ctk_img_2, text = "")
label_2.place(x=35, y=100)

temperature_label = ctk.CTkLabel(frame_2, bg_color="WHITE", font = ("Arial", 20), fg_color="gray", text = "")
temperature_label.place(x=10, y=250)

temperature = "N/A"
description = "N/A"

def get_weather(city):
    global temperature, description
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:  
        weather_data = response.json()

        if 'main' in weather_data:
            temperature = weather_data['main']['temp']  
            description = weather_data['weather'][0]['description']  
        else:
            temperature_label.configure(text="Error: Weather data not found for this location.")
    else:
        temperature_label.configure(text="Error: Failed to fetch weather data. Check your city name and API key.")

    temperature_label.configure(text=f"Temperature: {temperature}°C\nDescription: {description}")
    
    
app.mainloop()

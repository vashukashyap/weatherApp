import tkinter as tk
from tkinter import *
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk
import module.roundbg as roundbg
from tkinter.ttk import Progressbar
import threading
import urllib.request
import io
from io import BytesIO


API_KEY = 'bbdbda87321346bb65931a17d8c1d968'


def webimage(url,width=None,height=None):
        with urllib.request.urlopen(url) as u:
            raw_data = u.read()
            image = Image.open(io.BytesIO(raw_data))
            if(width!=None) and (height!=None):
                 image = image.resize((width,height))
            image = ImageTk.PhotoImage(image)
            return image

def daysmaxmintemp(json_data,day_list):
    #Current Day
    daymax_temp = json_data['list'][day_list[0]]['main']['temp_max']
    daymin_temp = json_data['list'][day_list[0]]['main']['temp_min']
    currenttemp_label.config(text=f'DAY: {daymax_temp}°C\n NIGHT: {daymin_temp}°C')
    #Day Two
    daymax_temp = json_data['list'][day_list[1]]['main']['temp_max']
    daymin_temp = json_data['list'][day_list[1]]['main']['temp_min']
    daytwotemp_label.config(text=f'DAY: {daymax_temp}°C\n NIGHT: {daymin_temp}°C')
    #Day Three
    daymax_temp = json_data['list'][day_list[2]]['main']['temp_max']
    daymin_temp = json_data['list'][day_list[2]]['main']['temp_min']
    daythreetemp_label.config(text=f'DAY: {daymax_temp}°C\n NIGHT: {daymin_temp}°C')
    #Day four
    daymax_temp = json_data['list'][day_list[3]]['main']['temp_max']
    daymin_temp = json_data['list'][day_list[3]]['main']['temp_min']
    dayfourtemp_label.config(text=f'DAY: {daymax_temp}°C\n NIGHT: {daymin_temp}°C')  
    #Day Five
    daymax_temp = json_data['list'][day_list[4]]['main']['temp_max']
    daymin_temp = json_data['list'][day_list[4]]['main']['temp_min']
    dayfivetemp_label.config(text=f'DAY: {daymax_temp}°C\n NIGHT: {daymin_temp}°C')
    #Day Six
    daymax_temp = json_data['list'][day_list[5]]['main']['temp_max']
    daymin_temp = json_data['list'][day_list[5]]['main']['temp_min']
    daysixtemp_label.config(text=f'DAY: {daymax_temp}°C\n NIGHT: {daymin_temp}°C')
    #Day Seven
    daymax_temp = json_data['list'][day_list[6]]['main']['temp_max']
    daymin_temp = json_data['list'][day_list[6]]['main']['temp_min']
    dayseventemp_label.config(text=f'DAY: {daymax_temp}°C\n NIGHT: {daymin_temp}°C')

def daysicon(json_data,day_list):       
    #Current Cell
    image=json_data['list'][day_list[0]]['weather'][0]['icon']
    day=datetime.now()
    currentday_label.config(text=day.strftime('%A'))
    image = webimage(f'https://openweathermap.org/img/wn/{image}@2x.png')
    current_image.config(image=image)
    current_image.image=image
    
    #Day Two cell
    image=json_data['list'][day_list[1]]['weather'][0]['icon']
    day=day+timedelta(days=1)
    daytwo_label.config(text=day.strftime('%A'))
    curnt_image = webimage(f'https://openweathermap.org/img/wn/{image}@2x.png',80,80)
    daytwo_image.config(image=curnt_image)
    daytwo_image.image=curnt_image
    
    #Day Three Cell
    image=json_data['list'][day_list[2]]['weather'][0]['icon']
    day=day+timedelta(days=1)
    daythree_label.config(text=day.strftime('%A'))
    curnt_image = webimage(f'https://openweathermap.org/img/wn/{image}@2x.png',80,80)
    daythree_image.config(image=curnt_image)
    daythree_image.image=curnt_image
    
    
    #Day Four Cell
    image=json_data['list'][day_list[3]]['weather'][0]['icon']
    day=day+timedelta(days=1)
    dayfour_label.config(text=day.strftime('%A'))
    curnt_image = webimage(f'https://openweathermap.org/img/wn/{image}@2x.png',80,80)
    dayfour_image.config(image=curnt_image)
    dayfour_image.image=curnt_image
    
    
    #Day Five Cell
    image=json_data['list'][day_list[4]]['weather'][0]['icon']
    day=day+timedelta(days=1)
    dayfive_label.config(text=day.strftime('%A'))
    curnt_image = webimage(f'https://openweathermap.org/img/wn/{image}@2x.png',80,80)
    dayfive_image.config(image=curnt_image)
    dayfive_image.image=curnt_image
    
    
    #Day Six Cell
    image=json_data['list'][day_list[5]]['weather'][0]['icon']
    day=day+timedelta(days=1)
    daysix_label.config(text=day.strftime('%A'))
    curnt_image = webimage(f'https://openweathermap.org/img/wn/{image}@2x.png',80,80)
    daysix_image.config(image=curnt_image)
    daysix_image.image=curnt_image
    
    #Day Seven Cell
    image=json_data['list'][day_list[6]]['weather'][0]['icon']
    day=day+timedelta(days=1)
    dayseven_label.config(text=day.strftime('%A'))
    curnt_image = webimage(f'https://openweathermap.org/img/wn/{image}@2x.png',80,80)
    dayseven_image.config(image=curnt_image)
    dayseven_image.image=curnt_image
     

def apicall(location):
    part = 'hourly,daily'
    try:
        #Fetching data
        api=f'https://api.openweathermap.org/data/2.5/forecast?lat={location.latitude}&lon={location.longitude}&units=metric&appid={API_KEY}'
        #api=f'https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}'
        #api=f'https://api.openweathermap.org/data/2.5/forecast?q={city}&exclude=hourly,daily&appid={API_KEY}'
        json_data = requests.get(api).json()
        #Extracting data
        temprature = json_data['list'][0]['main']['temp']
        humidity = json_data['list'][0]['main']['humidity']
        pressure = json_data['list'][0]['main']['pressure']
        wind = json_data['list'][0]['wind']['speed']
        description = json_data['list'][0]['weather'][0]['description']
        #Displaying value
        temp_val.config(text=(str(temprature)+' °C'))
        hum_val.config(text=(str(humidity)+' %'))
        press_val.config(text=(str(pressure)+' hPa'))
        wind_val.config(text=(str(wind)+' m/s'))
        des_val.config(text=(description))
        date=json_data['list'][0]['dt_txt'][8:10]
        day_list = [0]
        j=0
        for i in json_data['list']:
            if(i['dt_txt'][8:10]!=date):
                date=json_data['list'][0]['dt_txt'][8:10]
                day_list.append(j)
            j+=1

        daysicon(json_data,day_list)
        daysmaxmintemp(json_data,day_list)

        


    except KeyError:
         print("unbale to fetch")


def loading():
    #Showing progressbar
    progress.place(x=600,y=1)
    #Starting progressbar
    progress.start()
    #Progress bar will load until date time and weather is featching
    #Getting City name
    try:
        city=textfield.get() 
        #Gettig Timezone
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        #Setting time location
        timezone.config(text=result)
        #Setting Latitude and Longitude
        long_lat.config(text=f'{round(location.latitude,4)}°N,{round(location.longitude,4)}°E')
        #Getting location current time
        home=pytz.timezone(result)
        #Setting time
        local_time=datetime.now(home)
        current_time=local_time.strftime('%I:%M %p')
        time.config(text=current_time)

        #api calling for weather data
        apicall(location)



        #Hiding progress bar
        progress.stop()
        progress.place_forget()
    except AttributeError:
        textfield.delete('0', 'end')
        textfield.insert(0, 'not found')
        progress.stop()
        progress.place_forget()

def getWeather(_=None):
    #Creating Loadingbar Thread
    loadingth = threading.Thread(target=loading)
    loadingth.daemon = True
    loadingth.start()
    

    



#Making Tkinter Window
root = tk.Tk()
root.title("Wheather App")
root.geometry("890x470+200+200")
root.configure(bg='#57adff')
root.resizable(False,False)


#App icon
app_icon = tk.PhotoImage(file='./images/weather.png')
root.iconphoto(False,app_icon)


#SearchBar
btn = roundbg.RoundedBox(root, width=400, height=25,btnbackground='#203243' , radius=100,relief='ridge',highlightthickness = 0).place(x=450,y=20)


#LoadingBar
progress = Progressbar()


#Searchbar components
#search icon
search_icon=Image.open('./images/search.png')
search_icon=search_icon.resize((30, 30))
search_icon=ImageTk.PhotoImage(search_icon)
search_label=tk.Button(root, image=search_icon,background='#203243',relief='flat',command=getWeather).place(x=464,y=31)

#SearchText
textfield = tk.Entry(root,justify='center',width=18,font=('poopins',20,'bold'),bg='#203243',border=0,fg='white')
textfield.place(x=502,y=31)
#textfield.focus()
textfield.bind('<Return>', getWeather)



#Info Label
info_label = roundbg.RoundedBox(root, btnbackground='#203243', width=250, height=180,radius=10,highlightthickness = 0).place(x=10,y=20)


#information
temperature_label = tk.Label(root, text='Temperature:',font=('Helvetica',11),fg='white',bg='#203243')
temperature_label.place(x=30,y=40)
humidity_label = tk.Label(root, text='Humidity:',font=('Helvetica',11),fg='white',bg='#203243')
humidity_label.place(x=30,y=65)
pressure_label = tk.Label(root, text='Pressure:',font=('Helvetica',11),fg='white',bg='#203243')
pressure_label.place(x=30,y=90)
windspeed_label = tk.Label(root, text='Windspeed:',font=('Helvetica',11),fg='white',bg='#203243')
windspeed_label.place(x=30,y=115)
description_label = tk.Label(root, text='Description:',font=('Helvetica',11),fg='white',bg='#203243')
description_label.place(x=30,y=140)

#Bottom Black Blackground
bottom_frame = tk.Frame(root,width=900,height=220,bg='#203243',padx=1,pady=2)
bottom_frame.pack(side='bottom')

# myscrollbar=tk.Scrollbar(root,orient="horizontal")
# myscrollbar.pack(side="bottom",fill="x")
# myscrollbar.config(command=bottom_frame.xview)

#Current Weather box
current_weather =  roundbg.RoundedBox(bottom_frame,btnforeground="red", btnborder='white', btnbackground='#2c455c', width=220, height=180,radius=20,highlightthickness=0).grid(row=0,column=0)

#Remaining Days box
roundbg.RoundedBox(bottom_frame,btnforeground="red", btnborder='white', btnbackground='#2c455c', width=112, height=170,radius=20,highlightthickness=0).grid(row=0,column=1)
roundbg.RoundedBox(bottom_frame,btnforeground="red", btnborder='white', btnbackground='#2c455c', width=112, height=170,radius=20,highlightthickness=0).grid(row=0,column=2)
roundbg.RoundedBox(bottom_frame,btnforeground="red", btnborder='white', btnbackground='#2c455c', width=112, height=170,radius=20,highlightthickness=0).grid(row=0,column=3)
roundbg.RoundedBox(bottom_frame,btnforeground="red", btnborder='white', btnbackground='#2c455c', width=112, height=170,radius=20,highlightthickness=0).grid(row=0,column=4)
roundbg.RoundedBox(bottom_frame,btnforeground="red", btnborder='white', btnbackground='#2c455c', width=112, height=170,radius=20,highlightthickness=0).grid(row=0,column=5)
roundbg.RoundedBox(bottom_frame,btnforeground="red", btnborder='white', btnbackground='#2c455c', width=112, height=170,radius=20,highlightthickness=0).grid(row=0,column=6)


#CLOCK
#time
current_time = datetime.now().strftime('%I:%M %p')
time = tk.Label(root,text=current_time,font=('Helvetica',40,'bold'),fg='white',bg='#57adff')
time.place(x=550,y=80)

#timezone
timezone = tk.Label(root,font=('Helvetica',20,'bold'),fg='white',bg='#57adff')
timezone.place(x=550,y=135)

#longitutde
long_lat = tk.Label(root,font=('Helvetica',12),fg='white',bg='#57adff')
long_lat.place(x=550,y=170)


#Info Value
temp_val = tk.Label(root,text="-",font=('Helvetica',11),fg='white',bg='#203243')
temp_val.place(x=124,y=40)
hum_val = tk.Label(root, text='-',font=('Helvetica',11),fg='white',bg='#203243')
hum_val.place(x=124,y=65)
press_val = tk.Label(root, text='-',font=('Helvetica',11),fg='white',bg='#203243')
press_val.place(x=124,y=90)
wind_val = tk.Label(root, text='-',font=('Helvetica',11),fg='white',bg='#203243')
wind_val.place(x=124,y=115)
des_val = tk.Label(root, text='-',font=('Helvetica',11),fg='white',bg='#203243')
des_val.place(x=125,y=140)

 #ImageTk.PhotoImage(Image.open('https://openweathermap.org/img/wn/01d.png'))

# 
#Cells for 7day info

#current cell
currentday_cell = tk.Frame(bottom_frame,bg='#2c455c', width=200, height=160)
currentday_cell.grid(row=0,column=0)

current_image = tk.Label(currentday_cell,bg='#2c455c')
current_image.place(x=1,y=15)

currentday_label = tk.Label(currentday_cell,font='arial 15 bold',bg='#2c455c',fg='white')
currentday_label.place(x=90,y=50)

currenttemp_label = tk.Label(currentday_cell,font='arial 13 bold',bg='#2c455c',fg='#57adff')
currenttemp_label.place(x=40,y=100)

#Day Two Cell
daytwo_cell = tk.Frame(bottom_frame,width=110, height=150,bg='#2c455c')
daytwo_cell.grid(row=0,column=1)

daytwo_label = tk.Label(daytwo_cell,font='arial 10 bold',bg='#2c455c',fg='white')
daytwo_label.grid(row = 0, column = 0,pady=5)
daytwo_image = tk.Label(daytwo_cell,bg='#2c455c')
daytwo_image.grid(row = 1, column = 0,sticky='N')
daytwotemp_label = tk.Label(daytwo_cell,font='arial 9 bold',bg='#2c455c',fg='white')
daytwotemp_label.grid(row = 2, column = 0)

#Day Three Cell
daythree_cell = tk.Frame(bottom_frame,width=110, height=150,bg='#2c455c')
daythree_cell.grid(row=0,column=2)

daythree_label = tk.Label(daythree_cell,font='arial 10 bold',bg='#2c455c',fg='white')
daythree_label.grid(row = 0, column = 0,pady=5)
daythree_image = tk.Label(daythree_cell,bg='#2c455c')
daythree_image.grid(row = 1, column = 0,sticky='N')
daythreetemp_label = tk.Label(daythree_cell,font='arial 9 bold',bg='#2c455c',fg='white')
daythreetemp_label.grid(row = 2, column = 0)

dayfour_cell = tk.Frame(bottom_frame,width=110, height=150,bg='#2c455c')
dayfour_cell.grid(row=0,column=3)
dayfour_label = tk.Label(dayfour_cell,font='arial 10 bold',bg='#2c455c',fg='white')
dayfour_label.grid(row = 0, column = 0,pady=5)
dayfour_image = tk.Label(dayfour_cell,bg='#2c455c')
dayfour_image.grid(row = 1, column = 0,sticky='N')
dayfourtemp_label = tk.Label(dayfour_cell,font='arial 9 bold',bg='#2c455c',fg='white')
dayfourtemp_label.grid(row = 2, column = 0)

dayfive_cell = tk.Frame(bottom_frame,width=110, height=150,bg='#2c455c')
dayfive_cell.grid(row=0,column=4)
dayfive_label = tk.Label(dayfive_cell,font='arial 10 bold',bg='#2c455c',fg='white')
dayfive_label.grid(row = 0, column = 0,pady=5)
dayfive_image = tk.Label(dayfive_cell,bg='#2c455c')
dayfive_image.grid(row = 1, column = 0,sticky='N')
dayfivetemp_label = tk.Label(dayfive_cell,font='arial 9 bold',bg='#2c455c',fg='white')
dayfivetemp_label.grid(row = 2, column = 0)

daysix_cell = tk.Frame(bottom_frame,width=110, height=150,bg='#2c455c')
daysix_cell.grid(row=0,column=5)
daysix_label = tk.Label(daysix_cell,font='arial 10 bold',bg='#2c455c',fg='white')
daysix_label.grid(row = 0, column = 0,pady=5)
daysix_image = tk.Label(daysix_cell,bg='#2c455c')
daysix_image.grid(row = 1, column = 0,sticky='N')
daysixtemp_label = tk.Label(daysix_cell,font='arial 9 bold',bg='#2c455c',fg='white')
daysixtemp_label.grid(row = 2, column = 0)

dayseven_cell = tk.Frame(bottom_frame,width=110, height=150,bg='#2c455c')
dayseven_cell.grid(row=0,column=6)
dayseven_label = tk.Label(dayseven_cell,font='arial 10 bold',bg='#2c455c',fg='white')
dayseven_label.grid(row = 0, column = 0,pady=5)
dayseven_image = tk.Label(dayseven_cell,bg='#2c455c')
dayseven_image.grid(row = 1, column = 0,sticky='N')
dayseventemp_label = tk.Label(dayseven_cell,font='arial 9 bold',bg='#2c455c',fg='white')
dayseventemp_label.grid(row = 2, column = 0)


root.mainloop()

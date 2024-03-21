from kivy.lang.builder import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivymd.uix.button import MDFlatButton
from kivy.properties import NumericProperty
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout
from kivy_garden.mapview import MapView, MapMarker
from kivy.core.window import  Window
import json
import requests
import math
import random as r

# Defining Window Size

Window.size = (360, 640)

help_str = '''
ScreenManager:
    WelcomeScreen:
    LoginScreen:
    SignupScreen:
    AQIScreen:
	DashBoard:
	WeatherScreen:
    MapScreen:
    MoreScreen:

# Login & Signup Option Screen

<WelcomeScreen>:
    name:'welcomescreen'
    Image:
        source:'images/wall3.jpg'
        size_hint:None,None
        size:'7000dp','7000dp'
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}    
    MDCard:
        size_hint: None, None
        size: 300, 350
        pos_hint: {"center_x": 0.5, "center_y": 0.67}
        elevation: 10
        padding: 25
        spacing: 25
        radius: [17, 17]
        orientation: 'vertical'
        MDLabel:
            text:'Green Earth'
            font_style:'H3'
            halign:'center'
            pos_hint: {'center_y':0.8}
        MDLabel:
            text:'Login/Signup'
            font_style:'H4'
            halign:'center'
            pos_hint: {'center_y':0.5}
        MDLabel:
            text:'Initiative to make the world a bit greener'
            font_style:'H6'
            halign:'center'
            pos_hint: {'center_y':0.4}
        Image:
            source:'images/logo1.png'
            size_hint:None,None
            size:'150dp','150dp'
            pos_hint: {'center_x': 0.5, 'center_y': 0.1}            
            
    MDRaisedButton:
        text:'Login'
        font_style:'H6'
        pos_hint : {'center_x':0.3,'center_y':0.3}
        size_hint: (0.10,0.1)
        on_press: 
            root.manager.current = 'loginscreen'
            root.manager.transition.direction = 'left'
    MDRaisedButton:
        text:'Signup'
        font_style:'H6'
        pos_hint : {'center_x':0.7,'center_y':0.3}
        size_hint: (0.10,0.1)
        on_press:
            root.manager.current = 'signupscreen'
            root.manager.transition.direction = 'left'

# Login Screen
        
<LoginScreen>:
    name:'loginscreen'
    Image:
        source:'images/wall3.jpg'
        size_hint:None,None
        size:'7000dp','7000dp'
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}    
        
        
    MDLabel:
        text:'Login'
        font_style:'H2'
        halign:'center'
        pos_hint: {'center_y':0.9}

    MDTextField:
        
        id:login_email
        pos_hint: {'center_y':0.6,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Email'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDTextField:
        id:login_password
        pos_hint: {'center_y':0.4,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Password'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"

    MDRaisedButton:
        text:'Login'
        size_hint: (0.13,0.07)
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press:
            app.login()
            app.username_changer() 
            
        

    MDTextButton:
        text: 'Create an account'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:
            root.manager.current = 'signupscreen'
            root.manager.transition.direction = 'up'

# Signup Screen

<SignupScreen>:
    name:'signupscreen'
    Image:
        source:'images/wall3.jpg'
        size_hint:None,None
        size:'7000dp','7000dp'
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}    
        
        
    MDLabel:
        text:'Signup'
        font_style:'H2'
        halign:'center'
        pos_hint: {'center_y':0.9}

    MDTextField:
        id:signup_email
        pos_hint: {'center_y':0.6,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Email'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDTextField:
        id:signup_username
        pos_hint: {'center_y':0.75,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Username'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
    MDTextField:
        id:signup_password
        pos_hint: {'center_y':0.4,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Password'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDRaisedButton:
        text:'Signup'
        size_hint: (0.13,0.07)
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: app.signup()

    MDTextButton:
        text: 'Already have an account'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:
            root.manager.current = 'loginscreen'
            root.manager.transition.direction = 'down'

# Dashboard Screen

<DashBoard>:
	name: 'dashboard'
    MDScreen:
	    MDBoxLayout:
	        orientation:'vertical'
	        MDBoxLayout:
	            size_hint_y:.25
	            padding:dp(25)
	            MDBoxLayout:
	                orientation:"vertical"
	                MDLabel:
	                    text:"DASHBOARD"
	                    font_style:"H4"
   
	        MDGridLayout:
	            size_hint_y:.75
	            cols:2
	            padding:[dp(15),dp(15),dp(15),dp(200)]
	            spacing:dp(15)
	            ElementCard:
	                image:"images/aqi.png"
	                text:"AQI"
					on_release:
                        root.manager.transition.direction = 'right'
                        root.manager.transition.duration = 0.5
						app.root.current = 'aqiscreen'

	            ElementCard:
	                image:"images/weather.png"
	                text:"Weather"
					on_release:
                        root.manager.transition.direction = 'left'
                        root.manager.transition.duration = 0.5
						app.root.current= 'weatherscreen'

	            ElementCard:
	                image:"images/map.png"
	                text:"Map"
                    on_release:
                        root.manager.transition.direction = 'right'
                        root.manager.transition.duration = 0.5
						app.root.current= 'mapsview'

	            ElementCard:
	                image:"images/tree.png"
	                text:"More+"
                    on_release:
                        root.manager.transition.direction = 'left'
                        root.manager.transition.duration = 0.5
						app.root.current= 'morescreen'

    MDRectangleFlatIconButton:
        text: 'Logout'
        icon: "logout"
        pos_hint: {"center_x":0.7, "center_y":0.8}
        on_press:
            root.manager.transition.direction = 'right'
            root.manager.transition.duration = 1
            root.manager.current = 'loginscreen'
    MDIconButton:
        icon: "format-color-fill"
        on_press: app.color()

<ElementCard@MDCard>:
    md_bg_color:69/255,140/255,86/255,1
    padding:dp(15)
    spacing:dp(15)
    radius:dp(25)
    ripple_behavior: True
    image:''
    text:""
    items_count:""
    subtext:''

    orientation:'vertical'
    Image:
        source:root.image
    MDBoxLayout:
        orientation:'vertical'
        MDLabel:
            halign:"center"
            text:root.text
            font_style:"H6"
        MDLabel:
            halign:"center"
            font_style:"Caption"
            text:root.subtext
        MDLabel:
            halign:"center"
            text:root.items_count

# Screen For Showing AQI Info.

<AqiScreen>:
	name: 'aqiscreen'
    MDScreen:  #aqi
	    MDLabel:
	        text:"AQI :"
	        font_style:"H4"
			pos_hint: {'center_x': 0.6, 'center_y': 0.9}
		MDRectangleFlatIconButton:
			icon: "home-variant-outline"
			text: "Dashboard"
			pos_hint: {'center_x': 0.5, 'center_y': 0.1}
			on_release:
				root.manager.transition.direction = 'left'
                root.manager.transition.duration = 0.5
				app.root.current= 'dashboard'
		MDCard:
			size_hint: None, None
			size: 300, 400
			pos_hint: {"center_x": 0.5, "center_y": 0.5}
			elevation: 10
			padding: 25
			spacing: 25
			radius: [17, 17]
			orientation: 'vertical'
			MDLabel
			    font_style:"H6"
				text: app.tmp2
				size_hint_y: None
				pos_hint: {'center_x': 0.5, 'center_y': 0.7}
				height: self.texture_size[1]
				padding: 0, "20dp"
				halign: "center"
				theme_text_color: "Primary"

# Screen For Showing Weather Info.

<WeatherScreen>:
    name: 'weatherscreen'
    MDScreen:   #weather
	    MDLabel:
	        text:"Weather :"
	        font_style:"H4"
			pos_hint: {'center_x': 0.6, 'center_y': 0.9}
		MDRectangleFlatIconButton:
			icon: "home-variant-outline"
			text: "Dashboard"
			# padding: 0, "20dp"
			# halign: "center"
			pos_hint: {'center_x': 0.5, 'center_y': 0.1}
			on_release:
				root.manager.transition.direction = 'right'
                root.manager.transition.duration = 0.5
				app.root.current= 'dashboard'
		MDCard:
			size_hint: None, None
			size: 300, 400
			pos_hint: {"center_x": 0.5, "center_y": 0.5}
			elevation: 10
			padding: 25
			spacing: 25
			orientation: 'vertical'
			radius: [17, 17]
			MDLabel
				text: app.tmp
				size_hint_y: None
				font_style:'H6'
				pos_hint: {'center_x': 0.5, 'center_y': 0.7}
				height: self.texture_size[1]
				padding: 0, "20dp"
				halign: "center"
				theme_text_color: "Primary"

# Screen For Integrating Maps & Markers

<MapScreen>:
    name: 'mapsview'
    MapView:
        id: map_view
        zoom: 17
        lat: app.latitude
        lon: app.longitude
        MapMarker:
            id: map_view_marker
            lat: app.latitude
            lon: app.longitude
            source: "images/marker.png"
        MapMarker:
            lat: 28.64482341359033
            lon: 77.28382301870869
            source: "images/leaf.png"

        MapMarker:
            lat: 28.645614293475692
            lon: 77.28689688947841
            source: "images/leaf.png"

        MapMarker:
            lat: 28.643015545071645
            lon: 77.28645691597825
            source: "images/leaf.png"
    
    MDRectangleFlatIconButton:
        icon: "home-variant-outline"
        text: "Dashboard"
        # padding: 0, "20dp"
        # halign: "center"
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        on_release:
            root.manager.transition.direction = 'left'
            root.manager.transition.duration = 0.5
            app.root.current= 'dashboard'

    MDCard:
        size_hint: None, None
        size: 320, 150
        pos_hint: {"center_x": 0.5, "center_y": 0.85}
        orientation: 'vertical'
        md_bg_color: 1, 1, 1, 0.5
        line_color: 0, 0, 0, 1
        padding: 10
        elevation: 10

        MDTextField:
            id: serlon
            hint_text: "lon"
            mode: "rectangle"
            text_color: "black"
            font_size: "18dp"
            input_filter: 'float'
            size_hint_x: 0.7
            size_hint_y: 0.7
            pos_hint: {"center_x": 0.5}

        MDTextField:
            id: serlat
            hint_text: "lat"
            mode: "rectangle"
            text_color: "black"
            font_size: "18dp"
            input_filter: 'float'
            size_hint_x: 0.7
            size_hint_y: 0.7
            pos_hint: {"center_x": 0.5}

        MDRectangleFlatButton:
            text: "Search"
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 1
            line_color: 0, 0, 0, 1
            font_size: "18dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.2}
            on_press: app.update()
            
    MDIconButton:
		icon: "bookmark-plus-outline"
		on_press:
		    import webbrowser
			webbrowser.open("https://smartform.wps.com/#/write/mb-2b6df0e313ea4f6db52343ffd2464087")      
			
			
			
# Screen For Showing User Suggestions & More

<MoreScreen>:
    name: 'morescreen'
    MDScreen:                                                                 
	    MDLabel:
	        text:"More+ :"
	        font_style:"H4"
			pos_hint: {'center_x': 0.6, 'center_y': 0.9}
		MDRectangleFlatIconButton:
			icon: "home-variant-outline"
			text: "Dashboard"
			# padding: 0, "20dp"
			# halign: "center"
			pos_hint: {'center_x': 0.5, 'center_y': 0.1}
			on_release:
				root.manager.transition.direction = 'right'
                root.manager.transition.duration = 0.5
				app.root.current= 'dashboard'
		MDCard:
			size_hint: None, None
			size: 300, 400
			pos_hint: {"center_x": 0.5, "center_y": 0.5}
			elevation: 10
			padding: 25
			spacing: 25
			orientation: 'vertical'
			radius: [17, 17]

             
            TwoLineIconListItem:
                pos_hint: {'center_x':0.4,'center_y':0.6}
                text: "Worldometer"
                secondary_text:"Environment stats"
                on_press:
                    import webbrowser
                    webbrowser.open("https://www.worldometers.info/#c23")                
                IconLeftWidget:
                    icon: "assistant"
                        
            TwoLineIconListItem:
                pos_hint: {'center_x':0.4,'center_y':0.5}
                text: "National Geographic"
                secondary_text:"Environment stories"
                on_press:
                    import webbrowser
                    webbrowser.open("https://www.nationalgeographic.com/environment/")
           
                IconLeftWidget:
                    icon: "newspaper"
                  
                        
            TwoLineIconListItem:
                pos_hint: {'center_x':0.4,'center_y':0.4}
                text: "r/environment"
                secondary_text:"Reddit on Environment"
                on_press:
                    import webbrowser
                    webbrowser.open("https://www.reddit.com/r/environment/new/")                
                IconLeftWidget:
                    icon: "reddit"
                   
                        
            TwoLineIconListItem:
                pos_hint: {'center_x':0.4,'center_y':0.3}
                text: "Grow Trees"
                secondary_text:"eTreeCertificate"
                on_press:
                    import webbrowser
                    webbrowser.open("https://www.grow-trees.com/projectdetails.php?id=70")
                IconLeftWidget:
                    icon: "tree"
                   
                        
                        
'''

# Defining Classes

class AQIScreen(Screen):
	pass
class DashBoard(Screen):
	pass
class WeatherScreen(Screen):
	pass
class WelcomeScreen(Screen):
    pass
class LoginScreen(Screen):
    pass
class SignupScreen(Screen):
    pass
class MapScreen(Screen):
    pass
class MoreScreen(Screen):
    pass

# Creating ScreenManager & Adding Screens
sm = ScreenManager()
sm.add_widget(WelcomeScreen(name = 'loginscreen'))
sm.add_widget(LoginScreen(name = 'loginscreen'))
sm.add_widget(SignupScreen(name = 'signupscreen'))


class LoginApp(MDApp):

# Weather API & (It's Logic)

    city = 'Delhi'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=bfb1135122ea63262f01b4af8de680b2&units=metric'.format(city)
    res = requests.get(url)
    data = res.json()
    temp = math.trunc(data["main"]["temp"])
    desc = data["weather"] [0] ["description"]
    humid = data ["main"] ["humidity"]
    wind = data ["wind"] ["speed"]
    pressure = data ["main"] ["pressure"]
    lat = data ["coord"] ["lat"]
    lon = data ["coord"] ["lon"]

    tmp = city + '\n Temperature = ' + str(temp) + ' °C\n' + '\n Description = ' + str(desc) + \
          '\n Wind = ' + str(wind) + 'm/s \n Humidity = ' + str(humid) + '% \n Pressure = ' + str(pressure) + 'hPa'

# AQI API & It's Logic

    url2 = 'http://api.openweathermap.org/data/2.5/air_pollution?lat={}&lon={}&appid=bfb1135122ea63262f01b4af8de680b2'.format(
        lat, lon)
    res2 = requests.get(url2)
    data2 = res2.json()
    aqi = data2 ["list"] [0] ["main"] ["aqi"]
    co = data2 ["list"] [0] ["components"] ["co"]
    o3 = data2 ["list"] [0] ["components"] ["o3"]
    pm10 = data2 ["list"] [0] ["components"] ["pm10"]

    tmp2 = city  + ' (lat:'+ str(lat)+',lon:'+ str(lon) + ')\n \n' + ' AQI (1-5)= ' + str(aqi) + \
           '\n co = ' + str(co) + ' μg/m3 \n o3 = ' + str(o3) + str(pm10) + ' μg/m3 \n pm10 = ' + str(pm10)  + ' μg/m3'

# Function for changing Theme Color

    def color(self):
        Window.clearcolor = (
            r.uniform(0, 1), r.uniform(0, 1),
            r.uniform(0, 1), 1
        )

# Main Build Function

    def build(self):
        self.strng = Builder.load_string(help_str)
        self.url  = "https://green-earth-329816-default-rtdb.firebaseio.com/.json"
        self.icon = "images/logo1.png"
        self.title = 'Green Earth'
        return self.strng

# On_Start Function For Defining Latitude & Longitude to show Location on Map

    def on_start(self):
        self.latitude = 28.64423021545164
        self.longitude = 77.28457403296781
        self.strng.get_screen("mapsview").ids.map_view.center_on(self.latitude, self.longitude)
        print(self.latitude)

# Function for Signup using Firebase

    def signup(self):
        signupEmail = self.strng.get_screen('signupscreen').ids.signup_email.text
        signupPassword = self.strng.get_screen('signupscreen').ids.signup_password.text
        signupUsername = self.strng.get_screen('signupscreen').ids.signup_username.text
        if signupEmail.split() == [] or signupPassword.split() == [] or signupUsername.split() == []:
            cancel_btn_username_dialogue = MDFlatButton(text = 'Retry',on_release = self.close_username_dialog)
            self.dialog = MDDialog(title = 'Invalid Input',text = 'Please Enter a valid Input',size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
        if len(signupUsername.split())>1:
            cancel_btn_username_dialogue = MDFlatButton(text = 'Retry',on_release = self.close_username_dialog)
            self.dialog = MDDialog(title = 'Invalid Username',text = 'Please enter username without space',size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
        else:
            print(signupEmail,signupPassword)
            signup_info = str({f'\"{signupEmail}\":{{"Password":\"{signupPassword}\","Username":\"{signupUsername}\"}}'})
            signup_info = signup_info.replace(".","-")
            signup_info = signup_info.replace("\'","")
            to_database = json.loads(signup_info)
            print((to_database))
            requests.patch(url = self.url,json = to_database)
            self.strng.get_screen('loginscreen').manager.current = 'loginscreen'
    auth = 'h7djIQJwDOj1gRbX0x6W4NrVp8pul9DV5nxovcFh'

# Function for Login using Firebase

    def login(self):
        loginEmail = self.strng.get_screen('loginscreen').ids.login_email.text
        loginPassword = self.strng.get_screen('loginscreen').ids.login_password.text

        self.login_check = False
        supported_loginEmail = loginEmail.replace('.','-')
        supported_loginPassword = loginPassword.replace('.','-')
        request  = requests.get(self.url+'?auth='+self.auth)
        data = request.json()
        emails= set()
        for key,value in data.items():
            emails.add(key)
        if supported_loginEmail in emails and supported_loginPassword == data[supported_loginEmail]['Password']:
            self.username = data[supported_loginEmail]['Username']
            self.login_check=True
            self.strng.get_screen('dashboard').manager.current = 'dashboard'
        else:
            print("user no longer exists")
    def close_username_dialog(self,obj):
        self.dialog.dismiss()
    def username_changer(self):
        if self.login_check:
            self.strng.get_screen('dashboard')

    # map parameters

    latitude = NumericProperty(50)
    longitude = NumericProperty(3)

 

# Getting latitude and longitude from TextFields

    # Get Latitude

    def get_gps_latitude(self):
        abc = self.strng.get_screen("mapsview").ids.serlat.text
        bcd = float(abc)
        self.latitude = bcd
        return self.latitude # rounding

    # Get Longitude

    def get_gps_longitude(self):
        abc = self.root.get_screen("mapsview").ids.serlon.text
        bcd = float(abc)
        self.longitude = bcd
        return self.longitude

    # Updating Location & Marker

    def update(self):
        self.latitude = self.get_gps_latitude()
        self.longitude = self.get_gps_longitude()
        self.strng.get_screen("mapsview").ids.map_view.center_on(self.latitude, self.longitude)

LoginApp().run()
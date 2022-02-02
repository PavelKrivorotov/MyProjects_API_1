


from kivy.app import App

from kivy.core.window import Window

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.spinner import Spinner
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout

from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class Registration(Screen):
    def __init__(self, **kwargs):
        super(Registration, self).__init__(**kwargs)

        self.root = GridLayout(rows=2)
        self.Menu = GridLayout(rows=1, size_hint_x=None, size_hint_y=None)
        self.Body = FloatLayout()

        self.LabelName = Label(text='Name:', font_size=18, size_hint=(0.15, 0.05), pos_hint={'x':0.25, 'y':0.72})
        self.LabelLastName = Label(text='Last Name:', font_size=18, size_hint=(0.15, 0.05), pos_hint={'x':0.25, 'y':0.65})
        self.LabelEmail = Label(text='Email:', font_size=18, size_hint=(0.15, 0.05), pos_hint={'x':0.25, 'y':0.58})
        self.LabelPassword = Label(text='Password:', font_size=18, size_hint=(0.15, 0.05), pos_hint={'x':0.25, 'y':0.51})
        self.LabelToken = Label(text='Введите токен:', font_size=18, size_hint=(0.15, 0.05), pos_hint={'x':0.20, 'y':0.25})


        self.TextName = TextInput(multiline=False, font_size=18, size_hint=(0.3, 0.05), pos_hint={'x':0.45, 'y':0.72})
        self.TextLastNmae = TextInput(multiline=False, font_size=18, size_hint=(0.3, 0.05), pos_hint={'x':0.45, 'y':0.65})
        self.TextEmail = TextInput(multiline=False, font_size=18, size_hint=(0.3, 0.05), pos_hint={'x':0.45, 'y':0.58})
        self.TextPassword = TextInput(multiline=False, password=True, font_size=18, size_hint=(0.3, 0.05), pos_hint={'x':0.45, 'y':0.51})
        self.TextToken = TextInput(multiline=False, font_size=18, size_hint=(0.5, 0.05), pos_hint={'x':0.35, 'y':0.25})


        self.BtnRegistration = Button(text='Registration', font_size=20, size_hint=(0.17, 0.08), pos_hint={'x':0.25, 'y':0.38})
        self.BtnBackToAuthoriastion = Button(text='Back', width=50, height=40, size_hint_x=None, size_hint_y=None)

        
        self.Body.add_widget(self.LabelEmail)
        self.Body.add_widget(self.LabelPassword)
        self.Body.add_widget(self.LabelName)
        self.Body.add_widget(self.LabelLastName)
        self.Body.add_widget(self.LabelToken)

        self.Body.add_widget(self.TextEmail)
        self.Body.add_widget(self.TextPassword)
        self.Body.add_widget(self.TextName)
        self.Body.add_widget(self.TextLastNmae)
        self.Body.add_widget(self.TextToken)

        self.Menu.add_widget(self.BtnBackToAuthoriastion)
        self.Body.add_widget(self.BtnRegistration)

        self.BtnBackToAuthoriastion.bind(on_press=self.btn_back_to_authoriation_click)
        self.BtnRegistration.bind(on_press=self.btn_registration_click)


        self.root.add_widget(self.Menu)
        self.root.add_widget(self.Body)

        self.add_widget(self.root)


    def btn_registration_click(self, instance):
        print('Send token activation to your Email!')


    def btn_back_to_authoriation_click(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'authorisation'


class Authorisation(Screen):
    def __init__(self, **kwargs):
        super(Authorisation, self).__init__(**kwargs)

        self.LabelEmail = Label(text='Email:', font_size=20, size_hint=(0.15, 0.05), pos_hint={'x':0.25, 'y':0.52})
        self.LabelPassword = Label(text='Password:', font_size=20, size_hint=(0.15, 0.05), pos_hint={'x':0.25, 'y':0.45})
        

        self.TextEmail = TextInput(multiline=False, font_size=15, size_hint=(0.3, 0.05), pos_hint={'x':0.45, 'y':0.52})
        self.TextPassword = TextInput(multiline=False, password=True, font_size=20, size_hint=(0.3, 0.05), pos_hint={'x':0.45, 'y':0.45})


        self.BtnLogin = Button(text='Login', font_size=20, size_hint=(0.3, 0.08), pos_hint={'x':0.45, 'y':0.34})
        self.BtnRegistration = Button(text='Registration', font_size=20, size_hint=(0.17, 0.08), pos_hint={'x':0.25, 'y':0.34})

        
        self.add_widget(self.LabelEmail)
        self.add_widget(self.LabelPassword)

        self.add_widget(self.TextEmail)
        self.add_widget(self.TextPassword)

        self.add_widget(self.BtnLogin)
        self.add_widget(self.BtnRegistration)


        self.BtnLogin.bind(on_press=self.btn_login_click)
        self.BtnRegistration.bind(on_press=self.btn_registration_click)
    

    def btn_login_click(self, instance):
        user_email = self.TextEmail._get_text()
        user_password = self.TextPassword._get_text()

        print(user_email, user_password)

        self.TextEmail._set_text('')
        user_password = self.TextPassword._set_text('')
        print('Okk')

        self.manager.transition.direction = 'left'
        self.manager.current = 'data'


    def btn_registration_click(self, instance):
        print('Open window registrate!')

        self.manager.transition.direction = 'left'
        self.manager.current = 'registration'


class Data(Screen):
    def __init__(self, **kwargs):
        super(Data, self).__init__(**kwargs)

        self.list_data = [ ] 

        self.root = GridLayout(rows=2)

        self.LayoutMenu = GridLayout(rows=1, cols=3, height=40, size_hint_y=None)

        self.Menu = Spinner(text='Items', values=('Match', 'Phisic') , height=40, size_hint_y=None)

        self.BtnBackToAuthoriastion = Button(text='Out', width=50 ,height=40, size_hint_y=None, size_hint_x=None)
        self.BtnSettings = Button(text='Settings', width=80, height=40, size_hint_y=None, size_hint_x=None)
        
        self.LayoutMenu.add_widget(self.BtnBackToAuthoriastion)
        self.LayoutMenu.add_widget(self.Menu)
        self.LayoutMenu.add_widget(self.BtnSettings)

        self.BtnBackToAuthoriastion.bind(on_press=self.btn_back_to_authoriastion_click)
        self.Menu.bind(text=self.btn_menu_click)
        self.BtnSettings.bind(on_press=self.btn_settings_click)

        self.root.add_widget(self.LayoutMenu)


        self.RootScrollLayout = GridLayout(rows=2, size_hint_y=None)

        self.ScrollLayout = GridLayout(cols=7, size_hint_y=None, height=40)

        self.ScrollWindow = ScrollView(size_hint=(1, None), size_hint_y=None, size=(Window.width, Window.height))


        self.LabelId = Label(text='Id', width=100, height=40, size_hint_y=None, size_hint_x=None)
        self.LabelName = Label(text='Name', height=40, size_hint_y=None)
        self.LabelLastName = Label(text='Last Name', height=40, size_hint_y=None)
        self.LabelBall = Label(text='Ball', width=100, height=40, size_hint_y=None, size_hint_x=None)
        self.LabelUpdate = Label(text='Update', width=100, height=40, size_hint_y=None)
        self.LabelDelete = Label(text='Delete', width=100, height=40, size_hint_y=None)
        self.LabelDate = Label(text=f'Last Date Update', height=40, size_hint_y=None)

        self.ScrollLayout.add_widget(self.LabelId)
        self.ScrollLayout.add_widget(self.LabelName)
        self.ScrollLayout.add_widget(self.LabelLastName)
        self.ScrollLayout.add_widget(self.LabelBall)
        self.ScrollLayout.add_widget(self.LabelUpdate)
        self.ScrollLayout.add_widget(self.LabelDelete)
        self.ScrollLayout.add_widget(self.LabelDate)

        self.RootScrollLayout.add_widget(self.ScrollLayout)
        self.RootScrollLayout.add_widget(self.ScrollWindow)

        self.root.add_widget(self.RootScrollLayout)


        self.add_widget(self.root)

    
    def btn_back_to_authoriastion_click(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'authorisation'
    

    def btn_menu_click(self, *args):
        print(self.Menu.text)

        # print(self.ScrollWindow.children)
        if len(self.ScrollWindow.children) > 0:
            self.ScrollWindow.remove_widget(self.ScrollLayout_1)

        self.ScrollLayout_1 = GridLayout(cols=7, spacing=10, size_hint_y=None)

        for i in range(10):
            self.LabelId = Label(text=f'{i + 1} {self.Menu.text}', width=100, height=40, size_hint_y=None, size_hint_x=None)
            self.LabelName = Label(text='Pavel', height=40, size_hint_y=None)
            self.LabelLastName = Label(text='Krivorotov', height=40, size_hint_y=None)
            self.LabelBall = Label(text=f'{i*1.25}', width=100, height=40, size_hint_y=None, size_hint_x=None)

            self.BtnUpdate = Button(text='Update', height=40, size_hint_y=None)
            self.BtnDelete = Button(text='Delete', height=40, size_hint_y=None)

            self.LabelDate = Label(text=f'29.01.2021 15:40', height=40, size_hint_y=None)


            self.ScrollLayout_1.add_widget(self.LabelId)
            self.ScrollLayout_1.add_widget(self.LabelName)
            self.ScrollLayout_1.add_widget(self.LabelLastName)
            self.ScrollLayout_1.add_widget(self.LabelBall)

            self.ScrollLayout_1.add_widget(self.BtnUpdate)
            self.ScrollLayout_1.add_widget(self.BtnDelete)
            self.ScrollLayout_1.add_widget(self.LabelDate)
            # self.ScrollLayout.add_widget(self.button)

            # self.button.bind(on_press=self.btn_button_click)

            # self.list_data.append((i, self.button))
        
        self.ScrollWindow.add_widget(self.ScrollLayout_1)
        
        print(self.list_data)
    
    
    def btn_button_click(self, instance):
        print(f'Вызвана кнопка --> {instance}')


    def btn_settings_click(self, instance):
        self.manager.transition.direction = 'left'
        self.manager.current = 'settings'


class Settings(Screen):
    def __init__(self, **kwargs):
        super(Settings, self).__init__(**kwargs)

        self.root = GridLayout(rows=2)

        self.BtnBackToData = Button(text='Back', width=50 ,height=40, size_hint_y=None, size_hint_x=None)

        self.root.add_widget(self.BtnBackToData)

        self.BtnBackToData.bind(on_press=self.btn_back_to_data_click)

        self.add_widget(self.root)
    

    def btn_back_to_data_click(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'data'


class ManagerWindow(ScreenManager):
    def __init__(self, **kwargs):
        super(ManagerWindow, self).__init__(**kwargs)
        
        self.add_widget(Authorisation(name='authorisation'))
        self.add_widget(Registration(name='registration'))
        self.add_widget(Data(name='data'))
        self.add_widget(Settings(name='settings'))

        self.current = 'authorisation'


class MyApp(App):
    def build(self):
        root = ManagerWindow()
        return root


if __name__ == '__main__':
    MyApp().run()
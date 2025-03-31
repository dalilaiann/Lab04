import flet as ft

class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self._spellButton = None
        self.txtIn = None
        self._modality = None
        self._langList = None
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None
        self._risultato=ft.ListView()
        self._frase=ft.Text("")
        self._parole=ft.Text("")
        self._tempo=ft.Text("")
        self._risultato.controls.extend([self._frase, self._parole, self._tempo])
        # define the UI elements and populate the page

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START),
        )
        self.page.update()

        # Add your stuff here

        #GESTIONE LINGUA
        self._txtOut=ft.ListView()
        self._control=ft.Text("", color="green")
        self._txtOut.controls.append(self._control)
        self._langList=ft.Dropdown(label="Select language", hint_text="Select language",options=[ft.DropdownOption("italian"), ft.DropdownOption("english"), ft.DropdownOption("spanish")], width=800, on_change=self.__controller.handleLanguage)
        row1=ft.Row([self._langList], alignment=ft.MainAxisAlignment.START)
        self.page.add(self._txtOut)
        self.page.add(row1)

        #GESTIONE MODALITA'
        self._txtOut1=ft.ListView()
        self._control1=ft.Text("", color="green")
        self._txtOut1.controls.append(self._control1)
        self._modality=ft.Dropdown(label="Search Modality", hint_text="Search Modality", options=[ft.DropdownOption("Default"), ft.DropdownOption("Linear"), ft.DropdownOption("Dichotomic")], width=250, on_change=self.__controller.handleModality)

       #GESTIONE TESTO
        self.txtOut3=ft.Text("", color="red")
        self.txtIn=ft.TextField(label="Add your sentence here", width=400)
        self._spellButton=ft.ElevatedButton(text="Spell Check", on_click=self.__controller.handleSpellCheck)
        row2=ft.Row([self._modality, self.txtIn, self._spellButton], alignment=ft.MainAxisAlignment.START)
        self.page.add(self._txtOut1)
        self.page.add(row2)

    def update(self):
        self.page.update()

    def setController(self, controller):
        self.__controller = controller

    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()

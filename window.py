import customtkinter as ctk
import importlib
from PIL import Image 

chosenSlot = []
updatedVars = {}

class login_window:
    def loadWidgets(self):
        # Create a frame to hold the login widgets
        self.loginFrame = ctk.CTkFrame(self)
        self.loginFrame.pack(pady=20, padx=20)

        # get the window widgets
        

        logo_image = ctk.CTkImage(light_image=Image.open("images/logo.png"), dark_image=Image.open("images/logo.png"), size=(self.winfo_screenwidth()/4, self.winfo_screenheight()/3))
        logo_label = ctk.CTkLabel(self.loginFrame, text="", image=logo_image)
        logo_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        intro_label = ctk.CTkLabel(self.loginFrame, text="Bem vindo Ao HeroConquest.\nClique no botão abaixo para selecionar o seu Save")
        intro_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        self.optionmenu_var = ctk.StringVar(value="Escolha o seu Save")
        self.optionmenu = ctk.CTkOptionMenu(self.loginFrame, values=["Primeiro Slot", "Segundo Slot", "Terceiro Slot", "Quarto Slot", "Quinto Slot"],
                                         variable=self.optionmenu_var)
        self.optionmenu.grid(row=2, column=0,columnspan=2, padx=5, pady=5)

        self.lgnButton = ctk.CTkButton(self.loginFrame, text="Login", command=lambda: login_window.login(self))
        self.lgnButton.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        
    def login(self):
        if self.optionmenu_var.get() == "Escolha o seu Save":
            ctk.CTkLabel(self.loginFrame, text="Escolha o seu Slot, e Tente novamente").grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        else:
            for widget in self.loginFrame.winfo_children(): widget.destroy()
            self.loginFrame.destroy()
            
            saveDic = {"Primeiro Slot": "aFirstSave", "Segundo Slot": "bSecondSave", "Terceiro Slot": "cThirdSave", "Quarto Slot": "dFourthSave", "Quinto Slot": "eFifthSave"}
            saves = importlib.import_module(f'saves.{saveDic[self.optionmenu_var.get()]}')
            game_window.loadWidgets(self, saves, saveDic[self.optionmenu_var.get()])

class game_window:
    def loadWidgets(self, currentSave, fileName):
        # Create a frame to hold the login widgets
        self.mainFrame = ctk.CTkFrame(self)
        self.mainFrame.pack(pady=20, padx=20)

        # Create the login widgets
        if currentSave.playerName == None:
            self.playerNameEntry = ctk.CTkEntry(self.mainFrame, placeholder_text="Insira seu nome", textvariable=currentSave.playerName)
            self.playerNameEntry.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
            self.updateButton = ctk.CTkButton(self.mainFrame, text="Login", command=lambda: game_window.postName(self, currentSave))
            self.updateButton.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        else:
            ctk.CTkLabel(self.mainFrame, text=f"Bem vindo {currentSave.playerName}").grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        chosenSlot.append(fileName)   


    def postName(self, currentSave):
        currentSave.playerName = self.playerNameEntry.get().capitalize()
        updatedVars.update({"playerName": currentSave.playerName})
        self.playerNameEntry.destroy()
        self.updateButton.destroy()        
        ctk.CTkLabel(self.mainFrame, text=f"Bem vindo {currentSave.playerName}").grid(row=0, column=0, columnspan=2, padx=5, pady=5)



 




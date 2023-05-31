import game as g_game
import customtkinter as ctk
import importlib

class login_window:
    def loadWidgets(self):
        self.loginFrame = ctk.CTkFrame(self)
        self.loginFrame.pack(pady=20, padx=20)
        try: 
            from PIL import Image
            logo_image = ctk.CTkImage(light_image=Image.open("images/logo.png"), dark_image=Image.open("images/logo.png"), size=(self.winfo_screenwidth()/4, self.winfo_screenheight()/3))
            logo_label = ctk.CTkLabel(self.loginFrame, text="", image=logo_image)
            logo_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        except: ctk.CTkLabel(self.loginFrame, text="Erro Ao Carregar a imagem, por favor verifique a biblioteca Pillow e tente novamente").grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.intro_label = ctk.CTkLabel(self.loginFrame, text="Bem vindo Ao HeroConquest.\nClique no botão abaixo para selecionar o seu Save")
        self.intro_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
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
            saveDic = {"Primeiro Slot": "aFirstSave", "Segundo Slot": "bSecondSave", "Terceiro Slot": "cThirdSave", "Quarto Slot": "dFourthSave", "Quinto Slot": "eFifthSave"}
            saves = importlib.import_module(f'saves.{saveDic[self.optionmenu_var.get()]}')
            g_game.varStorage.insert(0, saveDic[self.optionmenu_var.get()])

            if saves.playerName is None:
                self.optionmenu.destroy(), self.lgnButton.destroy()
                self.intro_label.configure(text="Bem vindo Ao HeroConquest.\nQual será o nome do seu Herói?")
                self.playerNameEntry = ctk.CTkEntry(self.loginFrame, placeholder_text="Insira seu nome", textvariable=saves.playerName)
                self.playerNameEntry.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
                self.updateButton = ctk.CTkButton(self.loginFrame, text="Atualizar Nome", command=lambda: login_window.postName(self, saves))
                self.updateButton.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
            else:
                for widget in self.loginFrame.winfo_children(): widget.destroy()
                self.loginFrame.destroy()
                g_game.game_window.loadWidgets(self,saves)
        
    def postName(window, currentSave):
        currentSave.playerName = window.playerNameEntry.get().capitalize()
        g_game.updatedVars.update({"playerName": currentSave.playerName})
        for widget in window.loginFrame.winfo_children(): widget.destroy()
        window.loginFrame.destroy()
        g_game.game_window.loadWidgets(window,currentSave)

def updateSaves(fileName, changedVars):
        import fileinput
        path = f'saves/{fileName}.py'
        for line in fileinput.input(path, inplace=True):
                for varName, varValue in changedVars.items():
                    if varName in line:
                        if isinstance(varValue, str):
                            line = f"{varName} = '{varValue}'\n"
                        else:
                            line = f"{varName} = {varValue}\n"
                print(line, end='')

def BackToMain(self):
    for mainWidget in self.winfo_children(): 
     if isinstance(mainWidget, ctk.CTkFrame):
         for widget in mainWidget.winfo_children(): widget.destroy()
         mainWidget.destroy()
    try: 
      filename = g_game.varStorage[0]
      updateSaves(filename, g_game.updatedVars)
    except: pass
    login_window.loadWidgets(self)

def main():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    app = ctk.CTk()
    app.title("Hero Conquest: alpha ver")
    app.geometry("800x640")
    app.minsize(600, 640)
    backBtn = ctk.CTkButton(app, text="<~", fg_color="red", text_color="white", corner_radius=100, command=lambda: BackToMain(app), height=25, width=30)
    backBtn.place(rely=0.01, relx=0.01)
    login_window.loadWidgets(app)
    return app

main().mainloop()
try: 
 filename = g_game.varStorage[0]
 updateSaves(filename, g_game.updatedVars)
except: print('Nenhuma ação necessária, fechando...')





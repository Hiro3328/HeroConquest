import customtkinter as ctk

varStorage = []
updatedVars = {}

class game_window:
    def loadWidgets(window, currentSave): 
        varStorage.append(window)
        window.playerAttrs = ctk.CTkFrame(window)
        window.playerAttrs.pack(pady=20, padx=20)
        
        ctk.CTkLabel(window.playerAttrs, text=f"Bem vindo {currentSave.playerName}").grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        
        window.mainFrame = ctk.CTkFrame(window)
        window.mainFrame.pack(pady=20, padx=20, fill="both", expand=True)       
    def checkSave(window, currentSave):
        if currentSave.playerName is None:
            window.playerAttrs = ctk.CTkFrame(window)
            window.playerAttrs.pack(pady=20, padx=20)
            window.playerNameEntry = ctk.CTkEntry(window.playerAttrs, placeholder_text="Insira seu nome", textvariable=currentSave.playerName)
            window.playerNameEntry.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
            window.updateButton = ctk.CTkButton(window.playerAttrs, text="Login", command=lambda: game_window.postName(window, currentSave))
            window.updateButton.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        else:
            game_window.loadWidgets(window,currentSave)

    def postName(window, currentSave):
        currentSave.playerName = window.playerNameEntry.get().capitalize()
        updatedVars.update({"playerName": currentSave.playerName})
        window.playerNameEntry.destroy()
        window.updateButton.destroy()
        window.playerAttrs.destroy()
        game_window.loadWidgets(window,currentSave)


            

        
        

        


 




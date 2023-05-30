import window as g_window
import customtkinter as ctk

def updateSaves():
    try:
        import fileinput
        fileName = g_window.chosenSlot[0]
        changedVars = g_window.updatedVars
        path = f'saves/{fileName}.py'
        for line in fileinput.input(path, inplace=True):
                for varName, varValue in changedVars.items():
                    if varName in line:
                        if isinstance(varValue, str):
                            line = f"{varName} = '{varValue}'\n"
                        else:
                            line = f"{varName} = {varValue}\n"
        print(line, end='')
    except: pass
def BackToMain(self):
    for mainWidget in self.winfo_children(): 
     if isinstance(mainWidget, ctk.CTkFrame):
         for widget in mainWidget.winfo_children(): widget.destroy()
         mainWidget.destroy()
    try: fileName = g_window.chosenSlot[0]; updateSaves()
    except: pass
    g_window.login_window.loadWidgets(self)

def main():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    app = ctk.CTk()
    app.title("Window")
    app.geometry("800x640")
    backBtn = ctk.CTkButton(app, text="← Voltar", fg_color="red", text_color="white", corner_radius=5, command=lambda: BackToMain(app))
    backBtn.place(rely=0.01, relx=0.01, relwidth=0.1, relheight=0.05)
    g_window.login_window.loadWidgets(app)
    return app

main().mainloop()

updateSaves()





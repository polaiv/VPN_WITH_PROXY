# VPN WITH PROXY BY POLAIV | https://github.com/polaiv



import tkinter
import winreg
import customtkinter
from PIL import Image

class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry('400x300')
        self.label = customtkinter.CTkLabel(self, text='Ошибка')
        self.label.pack(padx=20, pady=20)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry('495x595')
        self.title('VPN_WITH_PROXY')
        self.resizable(False, False)
        self.toplevel_window = None
        self.logo = customtkinter.CTkImage(dark_image=Image.open('vpn_logo.png'), size=(460, 460))
        self.logo_label = customtkinter.CTkLabel(master=self, text='', image=self.logo)
        self.logo_label.place(relx=0.5, rely=0.20, anchor=tkinter.CENTER)

        self.lbl_enable = customtkinter.CTkLabel(self, text='VPN был успешно включен ✅')
        self.lbl_disable = customtkinter.CTkLabel(self, text='VPN был успешно выключен ❌')

        self.btn = customtkinter.CTkButton(self, text="Включить VPN ✅", command=self.toggle_vpn)
        self.btn.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

    def toggle_vpn(self):
        if self.btn.cget("text") == "Включить VPN ✅":
            self.btn.configure(text="Выключить VPN ❌")
            self.set_proxy_enabled(True)  # Включить VPN
            self.lbl_disable.place_forget()  # Скрыть надпись о выключении VPN
            self.lbl_enable.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)
        else:
            self.btn.configure(text="Включить VPN ✅")
            self.set_proxy_enabled(False)  # Выключить VPN
            self.lbl_enable.place_forget()  # Скрыть надпись о включении VPN
            self.lbl_disable.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    def set_proxy_enabled(self, enabled):
        try:
            registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                          r'Software\Microsoft\Windows\CurrentVersion\Internet Settings',
                                          0, winreg.KEY_WRITE)

            if enabled:
                winreg.SetValueEx(registry_key, 'ProxyEnable', 0, winreg.REG_DWORD, 1)
            else:
                winreg.SetValueEx(registry_key, 'ProxyEnable', 0, winreg.REG_DWORD, 0)

            winreg.CloseKey(registry_key)
            # print('Прокси-сервер успешно', 'включен' if enabled else 'выключен')
        except Exception as e:
            self.open_toplevel()


if __name__ == '__main__':
    app = App()
    app.mainloop()

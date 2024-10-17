import PySimpleGUI as sg
sg.theme("DarkGreen4")
sg.theme_text_color("#FFFF00")
window = sg.Window(
    title="Profile",
    layout=[[sg.Text("NPM : 2210010456")],
            [sg.Text("Nama : Ryandy Rhamadhany")],
            [sg.Text("Kelas : 5E Teknik Informatika")],
            [sg.Text("Matkul : Pemrograman Visual 3")]
            ],
    size=(500,200),
)
window()
window.close()
import PySimpleGUI as sg
window = sg.Window(
    title="Latihan 1",
    layout=[[sg.Text("NPM : 2210010456")],
            [sg.Text("Nama : Ryandy Rhamadhany")],
            [sg.Text("Kelas : 5E Teknik Informatika")],
            [sg.Text("Matkul : Pemrograman Visual 3")]
            ],
    size=(400,200)
)
window()
window.close()
import PySimpleGUI as sg
import os
import io
from PIL import Image
# funkcija, lai iegūtu attēlu no failu saraksta no norādītāse mapes (direktorija)
def get_image_files(directory):
    images_files=[f for f in os.listdir(directory) if f.lower().endswith(('.png', '.jpeg', '.jpg', '.gif'))]
    return images_files
# funkcija, lai parādītu attēlus
def show_gallery(image_files, selected_index, window):
    if selected_index<len(image_files):
        filename=os.path.join(directory, image_files[selected_index])
        image=Image.open(filename)
        image.thumbnail((400,400))
        bio=io.BytesIO()

menu_def=[['File', ['Close']], ['HELP', ['About']]]
layout=[
    [sg.Menu(menu_def)],
    [sg.Text('Izvēlies mapi ar attēliem:'), sg.Input(key='-DIR-', enable_events=True),sg.FolderBrowse()],
    [sg.Image(key='-IMAGE-', size=(400,400) )],
    [sg.Text("Attēls:"), sg.Text("0 / 0",key='-INDEX-')],
    [sg.Button('Iziet'), sg.Button('Iepriekš'), sg.Button('Nākamais')],
]

window=sg.Window('Attēlu galerija', layout, finalize=True)
directory=''
while True:
    event, values=window.read()
    if event in (sg.WINDOW_CLOSED, 'Iziet', 'Close'):
        break
    if event=='About':
        sg.popup("Darba autore: A.Caune")
        if event == 'DIR':
             directory=values['DIR']
             selected_index = 0
             image_files=get_image_files(directory)
             show_gallery(image_files, selected_index, window)
    if event == 'Iepriekš':
        if selected_index>0:
            selected_index-= 1
            show_gallery(image_files, selected_index, window)
    
    if event == 'Nākamais':
        if selected_index<len(image_files)-1:
            selected_index+=1
            show_gallery(image_files, selected_index, window)








    window.close()


import subprocess
import webbrowser
import random
import os
import pathlib

music = [
    'https://youtu.be/wAPCSnAhhC8?t=14',
    'https://youtu.be/lTRiuFIWV54?t=17',
    'https://youtu.be/-FlxM_0S2lA?t=39',
    'https://youtu.be/qvUWA45GOMg?t=33',
    'https://youtu.be/1TVlO05Ugjw?t=3',
    'https://youtu.be/z4WCaWJgOqM?t=7',
    'https://www.youtube.com/watch?v=H9yfuYDoGf4',
    'https://www.youtube.com/watch?v=H5ohDQ-umHM',
    'https://www.youtube.com/watch?v=woAHwpOLmyY',
    'https://www.youtube.com/watch?v=M6USc22nFnY',
    'https://www.youtube.com/watch?v=rVN1B-tUpgs&list=PLCaYobZ79uQrZOWJNbtSPb2vq39LAy_pv',
    'https://www.youtube.com/watch?v=eqispO2Bi2k&list=PLSaAi5XOwA7O1eDCn1lMZ4L1YGNZwXvvu',
    'https://www.youtube.com/watch?v=gYSU72ZBvB4'
    'https://www.youtube.com/watch?v=VGMrcfpg0h8'
    'https://www.youtube.com/watch?v=8F1-1j_ZDgc'
]


class OpenLastFiles:
    def open_gamedev(self, path, cat):
        art = False
        game = False
        script = False

        for subdirectories, b, Files in os.walk(path):
            for file_name in Files:
                file_loc = subdirectories + os.path.sep + file_name
                extention = file_loc.split('.')[-1]
                if extention == 'godot':
                    game = True
                    subprocess.Popen(
                        ['E:/Godot_v3.2.3-stable_win64.exe', file_loc])
                if extention == 'trelby':
                    script = True
                    subprocess.Popen(
                        ["C:/Program Files (x86)/KIT/Scenarist/Scenarist.exe", file_loc])
                if extention == 'kra':
                    art = True
                    subprocess.Popen(
                        ["C:/Program Files/Krita (x64)/bin/krita.exe", file_loc])

        MissingProjects().check(cat, art=art, game=game, script=script)

        webbrowser.open_new_tab(
            'https://docs.godotengine.org/en/stable/')
        webbrowser.open(random.choice(music))
        webbrowser.open("http://localhost/")

    def open_comic(self, path, cat):
        art = False
        svg = False
        img = False

        for subdirectories, b, Files in os.walk(path):
            for file_name in Files:
                file_loc = subdirectories + os.path.sep + file_name
                extention = file_loc.split('.')[-1]
                if extention == 'kra':
                    art = True
                    subprocess.Popen(
                        ["C:/Program Files/Krita (x64)/bin/krita.exe", file_loc])
                if extention == 'svg':
                    svg = True
                    subprocess.Popen(
                        ["C:/Program Files/Inkscape/bin/inkscape.exe", file_loc])
                if extention == 'gimp' or extention == 'png' or extention == 'jpg':
                    img = True
                    subprocess.Pop(
                        ["C:/Program Files/GIMP 2/bin/gimp-2.10.exe", file_loc])

        MissingProjects().check(cat, art=art, svg=svg, img=img)
        webbrowser.open(random.choice(music))
        webbrowser.open("http://localhost/")

    def open_art(self, path, cat):
        art = False
        ref = False
        for subdirectories, b, Files in os.walk(path):
            for file_name in Files:
                file_loc = subdirectories + os.path.sep + file_name
                extention = file_loc.split('.')[-1]
                if extention == 'pur':
                    art = True
                    subprocess.Popen(
                        ["C:\Program Files\PureRef\PureRef.exe", file_loc])
                if extention == 'kra':
                    ref = True
                    subprocess.Popen(
                        ["C:/Program Files/Krita (x64)/bin/krita.exe", file_loc])

        MissingProjects().check(cat, art=art, ref=ref)

        webbrowser.open('https://in.pinterest.com/')
        webbrowser.open(random.choice(music))
        webbrowser.open("http://localhost/")


class NewProjectFiles:
    def open_gamedev(self):
        subprocess.Popen(
            ['E:/Godot_v3.2.3-stable_win64.exe'])
        subprocess.Popen(
            ["C:/Program Files (x86)/KIT/Scenarist/Scenarist.exe"])
        subprocess.Popen(
            ["C:/Program Files/Krita (x64)/bin/krita.exe"])

        webbrowser.open_new_tab('https://docs.godotengine.org/en/stable/')
        webbrowser.open(random.choice(music))

    def open_art(self):
        subprocess.Popen(["C:\Program Files\PureRef\PureRef.exe"])
        subprocess.Popen(["C:/Program Files/Krita (x64)/bin/krita.exe"])

        webbrowser.open('https://in.pinterest.com/')
        webbrowser.open(random.choice(music))

    def open_comic(self):
        subprocess.Popen(["C:/Program Files/Krita (x64)/bin/krita.exe"])
        subprocess.Popen(["C:/Program Files/Inkscape/bin/inkscape.exe"])
        subprocess.Popen(["C:/Program Files/GIMP 2/bin/gimp-2.10.exe"])

        webbrowser.open(random.choice(music))


class MissingProjects():
    def check(self, cat, art=False, game=False, script=False, img=False, svg=False, ref=False):
        if cat == 'gamedev':
            if art == False:
                subprocess.Popen(
                    ["C:/Program Files/Krita (x64)/bin/krita.exe"])
            if game == False:
                subprocess.Popen(
                    ['E:/Godot_v3.2.3-stable_win64.exe'])
            if script == False:
                subprocess.Popen(
                    ["C:/Program Files (x86)/KIT/Scenarist/Scenarist.exe"])

        if cat == 'art':
            if art == False:
                subprocess.Popen(
                    ["C:/Program Files/Krita (x64)/bin/krita.exe"])
            if ref == False:
                subprocess.Popen(["C:\Program Files\PureRef\PureRef.exe"])

        if cat == 'comic':
            if art == False:
                subprocess.Popen(
                    ["C:/Program Files/Krita (x64)/bin/krita.exe"])
            if svg == False:
                subprocess.Popen(
                    ["C:/Program Files/Inkscape/bin/inkscape.exe"])
            if img == False:
                subprocess.Popen(["C:/Program Files/GIMP 2/bin/gimp-2.10.exe"])


# OpenLastFiles().open_gamedev(
    # 'G:/Creative Project/gamedev/Project Lake', 'gamedev')

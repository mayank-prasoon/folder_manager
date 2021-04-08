import os
import databasemanager as DM
import sqlite3


class FolderManager:
    """ this class will build the folder based on the """

    def build_folder(self, path, project_name, cat):
        """ the function will create a folder for the project"""

        p_path = str(path) + '/' + cat.casefold() + \
            '/' + str(project_name)

        if cat.casefold() == 'gamedev':
            location = DataHandler().add_database(p_path, project_name, cat)
            FolderManager().create_subfolder_gamedev(project_name, location, cat)
        elif cat.casefold() == 'comic':
            location = DataHandler().add_database(p_path, project_name, cat)
            FolderManager().create_subfolder_comic(project_name, location, cat)
        elif cat.casefold() == 'art':
            location = DataHandler().add_database(p_path, project_name, cat)
            FolderManager().create_subfolder_art(project_name, location, cat)
        else:
            print("this category doesn't exist\n")
            print("please choose from following:")
            available_category = ['1. comic', '2. gamedev', '3. art']
            for x in available_category:
                print(x)
            c = input("\ntype the name: ")
            FolderManager().build_folder(path, project_name, c.casefold())

    def create_subfolder_comic(self, project_name, path, cat):
        """creates sub folder for the comic projects"""

        try:
            os.makedirs(path)
        except FileExistsError:
            print("the project folder already exits\n")

        print(str(project_name) + ': ' + str(path) + ':' +
              '\nall the folders are made properly\n')

        x = ['blender assest/model/character', 'blender assest/model/props', 'blender assest/model/scene',
             'blender assest/texture', 'blender project', 'raw image', 'edited image',
             'drawing', 'blank page', 'inkscape', 'finished page']
        for a in x:
            os.makedirs(str(path) + '/' + str(a))

    def create_subfolder_gamedev(self, project_name, path, cat):
        """creates sub folders for the gamedev projects"""

        try:
            os.makedirs(path)
        except FileExistsError:
            print("the project folder already exits\n")

        print(str(project_name) + ':' + str(path) + ':' +
              '\nall the folders are made properly\n')

        x = ['assets/music/lyrics', 'assets/music/ambience', 'assets/art/character/stills',
             'assets/art/character/animations', 'assets/art/environments', 'assets/art/props/stills',
             'assets/art/props/animations', 'assets/art/tiles', 'assets/art kit', 'assets/art/svg', 'assets/art/icons', 'assets/cutsene',
             'assets/art/blender assest/model/character', 'assets/art/blender assest/model/props',
             'assets/art/blender assest/texture', 'assets/art/blender project', 'npc/scripts', 'npc/scene', 'player/scripts', 'player/scene',
             'gamedata', 'singletones/scene', 'singletones/scripts', 'enemy/scene', 'enemy/scripts', 'level/scripts', 'level/scene']
        for a in x:
            os.makedirs(str(path) + '/' + str(a))

    def create_subfolder_art(self, project_name, path, cat):
        """creates sub folders for the the art project"""

        try:
            os.makedirs(path)
        except FileExistsError:
            print("the project folder already exits\n")

        print(str(project_name) + ':' + str(path) + ':' +
              '\nall the folders are made properly\n')

        x = ['pureref', 'reference', 'krita',
             'export/instagram', 'export/best quality']
        for a in x:
            os.makedirs(str(path) + '/' + str(a))


class DataHandler:
    def add_database(self, project_path, project_name, cat):
        """add things to the database"""

        try:
            print(project_path)
            DM.DatabaseManager().add_path(project_name, cat, project_path)
            path_enter = True
            return project_path
        except sqlite3.IntegrityError:
            project_path = str(project_path) + '/' + cat.casefold() + \
                '/' + input(
                'the project folder already exist.\n Please choose is a new name: ')
            return project_path

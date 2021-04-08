from tkinter import Tk
from tkinter.filedialog import askdirectory

import databasemanager as DM
import foldercreator as fc
import os
import exicutesoftware
import tomatotimer as tt


dm = DM.DatabaseManager()


class Welcome:
    def welcome(self):
        welcome = input(
            "\twelcome to the software\nplease choose from the following command....\n1. last\n2. all\n3. new\n4. setting\n5. exit\n\t")
        if welcome == 'last' or welcome == '1':
            project_list = dm.search_all()
            print("this was the last project you were working on: " +
                  str(project_list[-1][1] + ' | ' + project_list[-1][2] + ' | ' + project_list[-1][5]))
            Project().lastproject()

        if welcome == 'new' or welcome == '3':
            print("please complete the following in order to start a new project....\n\n")
            Project().new_project(askdirectory(title='Select the location'),
                                  input('name of the project: '), input("\ncategory of the project: "))
        if welcome == 'all' or welcome == '2':
            Project().all_project()
        if welcome == 'setting' or welcome == '4':
            pass
        if welcome == 'exit' or welcome == '5':
            pass


class Project:
    def all_project(self):
        """dispaly all the projects"""

        print(
            'these are all your project please choose one from the following\n')
        for y in range(len(dm.search_all())):
            print(y, dm.search_all()[y][1], dm.search_all()[y][2],
                  dm.search_all()[y][5])
        try:
            num = input('\n\topen: ')
            print(str(dm.search_all()[int(num)][3]))

            try:
                time = input("please set the alarm: ")
            except:
                print("what ever you typed, it was not a not integer")
                time = input("please set the alarm: ")

            Project().openproject(str(dm.search_all()[int(num)][3]), str(
                dm.search_all()[int(num)][2]))
            tt.TomatoTimer().break_time(time)
            tt.TomatoTimer().add_work_hour(num, time)
        except:
            print('an error has occur:\n\t' + str(num) +
                  ' is not a number\nplease choose the number like 1,2,3')
            Welcome().welcome()

    def openproject(self, location, cat):
        """Opens a project that was called"""

        location = str(location)
        location = os.path.realpath(location)
        RunProgram().run(cat, location)
        os.startfile(location)

    def lastproject(self):
        """Last project which was produced"""

        if input('should if open = ' + str(dm.search_all()[-1][3]) + '\n (yes/no)\n\t').casefold() == 'yes':
            location = str(dm.search_all()[-1][3])
            cat = str(dm.search_all()[-1][2])
            location = os.path.realpath(location)
            try:
                time = input("please set the alarm: ")
            except:
                print("what ever you choose was not a not integer")
                time = input("please set the alarm: ")
            RunProgram().run(cat, location)
            os.startfile(location)
            tt.TomatoTimer().break_time(time)
            tt.TomatoTimer().add_work_hour(-1, time)
        else:
            print('home page...')
            Welcome().welcome()

    def new_project(self, location, name, cat):
        """Creates a new project"""

        fc.FolderManager().build_folder(location, name, cat)
        if input('do you want to open all the programs: ') == 'yes':
            if cat == 'art':
                exicutesoftware.NewProjectFiles().open_art()
            if cat == 'comic':
                exicutesoftware.NewProjectFiles().open_comic()
            if cat == 'gamedev':
                exicutesoftware.NewProjectFiles().open_gamedev()
        os.startfile(location)


class RunProgram:
    def run(self, cat, location):
        if input('do you want to open all the programs: ') == 'yes':
            if cat == 'art':
                exicutesoftware.OpenLastFiles().open_art(location, 'art')
            if cat == 'comic':
                exicutesoftware.OpenLastFiles().open_comic(location, 'comic')
            if cat == 'gamedev':
                exicutesoftware.OpenLastFiles().open_gamedev(location, 'gamedev')
        else:
            pass


a = Welcome().welcome()

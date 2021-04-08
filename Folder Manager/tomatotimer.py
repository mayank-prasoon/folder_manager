import time
import webbrowser
import databasemanager as dm


class TomatoTimer:
    """Simple tool to manage the time"""

    def time_convert(self, sec):
        mins = sec // 60
        sec = sec % 60
        hours = mins // 60
        mins = mins % 60
        print("Time Lapsed = {0}:{1}:{2}".format(
            int(hours), int(mins), round(sec, 2)))

    def start_timer(self):
        start_time = time.time()

    def stop_timer(self):
        end_time = time.time()
        time_lapsed = end_time - TomatoTimer().start_time
        TomatoTimer().time_convert(time_lapsed)

    def break_time(self, t):
        t = int(t) * 60
        print("\ntimer started...\n")
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print("\t" + timer, end="\r")
            time.sleep(1)
            t -= 1
        print('time has up, its time for a break!!')
        webbrowser.open("file:///C:/Users/MAYANK/Music/Videoder/alarm.mp3")

    def add_work_hour(self, Pid="", time=""):
        """Access database and update the time"""

        rows = dm.DatabaseManager().search_all()[int(Pid)]
        Pid = rows[0]
        hour, mins = divmod(int(rows[6]), 60)
        time = int(rows[6]) + int(time)
        print("you worked ~ " + str(hour) + ":" +
              str(mins) + " min on the last project")
        dm.DatabaseManager().add_time(Pid=Pid, time=time)

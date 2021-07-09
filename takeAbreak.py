from plyer import notification
import time
def Notifyme(title, message):
    try:
        notification.notify(
            title = title,
            message = message,
            app_icon = "C:/Users/Admin/PycharmProjects/firstprog/break.ico",
            timeout = 2
        )
    except Exception as ex:
        print(ex)

if __name__ == '__main__':
    try:
        while True:
            Notifyme("Hey User", "Take A break For 20 Seconds")
            time.sleep(5)
    except Exception as ex:
        print(ex)
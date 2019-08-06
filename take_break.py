"""
Set an alarm to take a break by playing a youtube video
"""
import webbrowser
import time


def main():
    """
    Test function
    :return: none
    """
    video_address = "https://youtu.be/W16bk86xIY0"
    i = 3
    while i:
        # Delay "sleep"
        time.sleep(60*60)
        webbrowser.open(video_address)
        i -= 1
        print("It is time to take a break, is: " time.ctime())


if __name__ == '__main__':
    main()
    exit(0)
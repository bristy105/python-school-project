"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

Example program about storing objects in
a data structure (list in this case).
"""

class Time:
    """
    A simple example class to model time (hours & minutes)
    in a Python program. We are talking about 24 hour time here.
    """

    def __init__(self, hh = 0, mm = 0):
        self.__hh = hh
        self.__mm = mm

    def __str__(self):
        """
        Special function for converting a time object to a string.
        """

        return f"{self.__hh}:{self.__mm:02d}"

    def __int__(self):
        """
        Special function for converting time object to an integer
        value telling how many minutes hass passed since midnight.
        """

        return self.__mm + self.__hh * 60

    def difference_in_minutes(self, time_object):
        return int(time_object) - int(self)

    def __sub__(self, time_object):
        """
        Special function for implementing substraction operator "-".
        """

        time_difference = int(time_object) - int(self)

        hours = time_difference // 60
        minutes = time_difference % 60

        result_object = Time(hours, minutes)
        return result_object

    def __lt__(self, time_object):
        """
        Special function for implementing less-than operator "<".
        """

        return self.difference_in_minutes(time_object) > 0


def main():
    timetable = [ Time( 6, 30), Time(10, 15), Time(14, 15),
                  Time(16, 20), Time(17, 20), Time(20) ]

    hours_now = int(input("Enter the hours now: "))
    minutes_now = int(input("Enter the minutes now: "))

    time_now = Time(hours_now, minutes_now)

    for time in timetable:
        if time_now < time:
            print("Next bus departs at:", time)
            print("Time left before departure:", time_now - time)
            return

    print("No buses departing today!")


if __name__ == "__main__":
    main()

"""
Author: Manvir Kaur
KUID: 3064194
Date: 11/29/2021
Lab: lab11
Last modified: 12/06/2021
Purpose: Driver's License Records Data
"""


class DriversLicense:
    def __init__(self, dl_number, f_name, l_name, age, voter):
        self._dl_number = dl_number
        self._f_name = f_name
        self._l_name = l_name
        self._age = age
        self._voter = voter

    def get_dl_number(self):
        return self._dl_number

    def get_f_name(self):
        return self._f_name

    def get_l_name(self):
        return self._l_name

    def get_age(self):
        return self._age

    def get_voter(self):
        return self._voter

    def __eq__(self, other):
        if self._dl_number == other._dl_number:
            return True
        else:
            return False

    def __ne__(self, other):
        if self._dl_number != other._dl_number:
            return True
        else:
            return False

    def __str__(self):
        return f'{self._l_name}, {self._f_name} ({self._age}): {self._dl_number}'


class DMV:
    def __init__(self, filename):
        self.filename = filename
        self.drivers = []

        file_name = open(self.filename, "r")
        num = int(file_name.readline())
        for n in range(num):
            line = file_name.readline().strip()
            line = line.replace('\t', ' ')
            line = line.split(' ')
            driver = DriversLicense(int(line[0].strip()), line[1], line[2], int(line[3]), line[4])
            self.drivers.append(driver)
        file_name.close()

    def run(self):
        choice = 0
        while choice != 5:
            print("1) Print all Drivers Info \n2) Print all young, unregistered voters \n3) Print drivers by first "
                  "initial \n4) Print driver with id \n5) Quit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.all_drivers()
            elif choice == 2:
                self.young_nonvoters()
            elif choice == 3:
                self.first_initial()
            elif choice == 4:
                self.driver_with_id()

    def all_drivers(self):
        print("")
        for driver in self.drivers:
            print(driver)
        print("")

    def young_nonvoters(self):
        print("")
        for driver in self.drivers:
            if 18 <= driver.get_age() <= 24 and driver.get_voter() == "N":
                print(driver)
        print("")

    def first_initial(self):
        print("")
        char = input("Enter a single character for the first initial you want to search: ")
        x = False
        for driver in self.drivers:
            if driver.get_f_name()[0].lower() == char.lower():
                print(driver)
                x = True
        if not x:
            print("No record found.")
        print("")

    def driver_with_id(self):
        print("")
        id_num = int(input("Enter an id: "))
        x = False
        for driver in self.drivers:
            if driver.get_dl_number() == id_num:
                print(driver)
                x = True
        if not x:
            print("No record found.")
        print("")


def main():
    filename = input("Enter a file: ")
    myDMV = DMV(filename)
    myDMV.run()


if __name__ == "__main__":
    main()

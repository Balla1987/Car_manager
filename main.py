def main():
    print "Welcome to the Car-manager program!"
    print "#" * 10
    print ""

    cars = []

    while True:
        print "Please choose one of these option:"
        print "To see the list, please enter: a"
        print "To add new cars, to the list: b"
        print "To delete one of the cars: c"
        print "To change on of the parameters: d"
        print "To exit the program: f"

        user_choice = raw_input("Please enter a character:")

        if user_choice.lower() == "a":
            allCarModells(cars)
        elif user_choice.lower() == "b":
            new_car(cars)
        elif user_choice.lower() == "c":
            deleteCars(cars)
        elif user_choice.lower() == "d":
            modifyCars(cars)
        elif user_choice.lower() == "f":
            print "Thank you, see you next time!"
            break
        else:
            print "Please enter a valid character!"
            continue

class Cars(object):
    def __init__(self, brand, model, kilometers, general_service_date):
        self.brand = brand
        self.model = model
        self.kilometers = kilometers
        self.general_service_date = general_service_date

def new_car(cars):
        brand = raw_input("Please add new brand!")
        model = raw_input("Please add the new model!")
        try:
            kilometers = float(raw_input("Please add the actual kilometer stand!"))
        except ValueError:
            print "Sorry, that's not a valuable kilometers!"
            return
        try:
            general_service_date = float(raw_input("Please add the general service date(year, month)!"))
        except ValueError:
            print "Sorry, that's not a valuable service date!"
            return

        new = Cars(brand=brand, model=model, kilometers=kilometers, general_service_date=general_service_date)
        cars.append(new)

        print ""
        print "%s %s is successfully add to your list" % (brand, model)

def allCarModells(cars):
        for index, auto in enumerate(cars):
            print "ID:" + str(index)
            print auto.brand
            print auto.model
            print auto.kilometers
            print auto.general_service_date

        if not cars:
            print "You don't have any cars on the system!"

def deleteCars(cars):
    print "Please select, which car want you delete!"
    print ""

    for index, auto in enumerate(cars):
        print str(index) + " " + auto.brand + " " + auto.model
    print ""

    selected_id = raw_input("Which car would you like to delete? (enter ID number): ")
    selected_contact = cars[int(selected_id)]

    cars.remove(selected_contact)

    print ""
    print "Car is deleted!"

def modifyCars(cars):
    print "Please select, which car want you edit!"
    print ""

    for index, auto in enumerate(cars):
        print str(index) + " " + auto.brand + " " + auto.model
    print ""

    selected_id = raw_input("Which car would you like to edit? (enter ID number): ")
    selected_contact = cars[int(selected_id)]

    try:
        new_kilometers = float(raw_input("Enter the new kilometers!"))
        selected_contact.kilometers = new_kilometers
    except ValueError:
        print "Please enter a valid kilometer stand!"
        return

    print ""
    print "Kilometers upgraded!"

    try:
        new_general_service_date = float(raw_input("Enter the new general_service_date!"))
        selected_contact.general_service_date = new_general_service_date
    except:
        print "Please enter a valid general service date!"
        return

    print ""
    print "General service date updated!"

if __name__ == "__main__":
    main()

#declare function name generate_report with argument name main_tank,external_tank,hydrogen_tank
def generate_report(main_tank,external_tank,hydrogen_tank):
    return print("Fuel Report:\n\tMain Tank: {}%\n\tExternal Tank: {}%\n\tHydrogen Tank: {}%".format(main_tank,external_tank,hydrogen_tank))

generate_report(80,70,75)

#create function fuel_report with keyword argument fuel_tanks
def fuel_report(**fuel_tanks):
    print("Fuel Report:")
    for key,value in fuel_tanks.items():
        print("\t{}: {}%".format(key,value))

fuel_report(Main_Tank=80,External_Tank=70,Hydrogen_tank=75)
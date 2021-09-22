import CarClass as CC

def main():

    vehicle = CC.Car(2016,'Acura')

    #accelerate car
    vehicle.accelerate()
    print('Current speed:',vehicle.get_speed())
    vehicle.accelerate()
    print('Current speed:',vehicle.get_speed())
    vehicle.accelerate()
    print('Current speed:',vehicle.get_speed())
    vehicle.accelerate()
    print('Current speed:',vehicle.get_speed())
    vehicle.accelerate()
    print('Current speed:',vehicle.get_speed())

    #brake car
    print()
    vehicle.brake()
    print('Current speed:',vehicle.get_speed())
    vehicle.brake()
    print('Current speed:',vehicle.get_speed())
    vehicle.brake()
    print('Current speed:',vehicle.get_speed())
    vehicle.brake()
    print('Current speed:',vehicle.get_speed())
    vehicle.brake()
    print('Current speed:',vehicle.get_speed())

main()
    
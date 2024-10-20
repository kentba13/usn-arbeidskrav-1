from car import Car
from fuel_type import FuelType

def main():
    yearly_km = 10000

    #El-bil objekt
    electrical_car = Car(FuelType.EL, yearly_km)
    #Bensin bil objekt
    gasoline_car = Car(FuelType.BENSIN, yearly_km)
    
    print("El-bil kostnader:")
    print(electrical_car)
    
    print("\nBensin bil kostnader:")
    print(gasoline_car)
    
    print("\nKostnads differanse:")
    
    '''
    sammenligner priser for begge bil typene
    Bruk av f-string eller literal string interpolation: https://peps.python.org/pep-0498/
    .2f er en float-point format specifier, tilsier at det skal være 2 desimaler
    '''
    # Forsikring
    insurance_difference = abs(electrical_car.insurance - gasoline_car.insurance)
    if electrical_car.insurance < gasoline_car.insurance:
        print(f"El-bil har billigere forsikrings kostnader: {electrical_car.insurance:.2f} kr | {insurance_difference:.2f} kr billigere enn bensin")
    else:
        print(f"Bensin bil har billigere forsikrings kostnader: {gasoline_car.insurance:.2f} kr | {insurance_difference:.2f} kr billigere enn elektrisk")

    # Drivstoff
    fuel_difference = abs(electrical_car.fuel_cost - gasoline_car.fuel_cost)
    if electrical_car.fuel_cost < gasoline_car.fuel_cost:
        print(f"El-bil har billigere drivstoff kostnader: {electrical_car.fuel_cost:.2f} kr | {fuel_difference:.2f} kr billigere enn bensin")
    else:
        print(f"Bensin bil har billigere drivstoff kostnader: {gasoline_car.fuel_cost:.2f} kr | {fuel_difference:.2f} kr billigere enn elektrisk")

    # Bom avgift
    toll_difference = abs(electrical_car.toll - gasoline_car.toll)
    if electrical_car.toll < gasoline_car.toll:
        print(f"El-bil har billigere bom avgift: {electrical_car.toll:.2f} kr | {toll_difference:.2f} kr billigere enn bensin")
    else:
        print(f"Bensin bil har billigere bom avgift: {gasoline_car.toll:.2f} kr | {toll_difference:.2f} kr billigere enn elektrisk")

    # Årlig totale kostnader
    total_cost_difference = abs(electrical_car.annual_cost - gasoline_car.annual_cost)
    if electrical_car.annual_cost < gasoline_car.annual_cost:
        print(f"El-bil er total billigere: {electrical_car.annual_cost:.2f} | {total_cost_difference:.2f} kr billigere enn bensin")
    else:
        print(f"Bensin bil er totalt billigere: {gasoline_car.annual_cost:.2f} kr | {total_cost_difference:.2f} kr billigere enn elektrisk")

if __name__ == '__main__':
    main()
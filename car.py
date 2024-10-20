from fuel_type import FuelType
import datetime
import calendar

class Car:
    
    # Klasse konstanter
    EL_INSURANCE_COST = 5000.00       # Årlig forsikring for el-biler
    GASOLINE_INSURANCE_COST = 7500.00 # Årlig forsikring for bensin bil
    
    TRAFFIC_FEE_COST = 8.38           # Daglig trafikkforsikringsavgift
    
    EL_FUEL_PER_KM = 0.20             # kWh pr. km for el-bil
    EL_PRICE = 2.00                   # Pris per kWh
    BENSIN_FUEL_PER_KM = 1.00         # Bensin kostnader pr kilometer
    
    EL_TOLL_FEE = 0.10                # Bomavgift for elektriske biler
    BENSIN_TOLL_FEE= 0.30             # Bomavgift for bensin biler
    
    '''
    Konstruktør
    '''
    def __init__(self, type: type, yearly_km):
        self.type = type
        self.yearly_km = yearly_km
        self.insurance = self.get_insurance_cost()
        self.traffic_fee = self.get_traffic_fee()
        self.fuel_cost = self.get_fuel_cost()
        self.toll = self.get_toll()
        self.annual_cost = self.get_annual_cost()
    

    '''
    Utregning av forsikring basert på type bil
    '''
    def get_insurance_cost(self):
        if self.type == FuelType.EL:
            return self.EL_INSURANCE_COST #Årlig forsikring Elbil
        elif self.type == FuelType.BENSIN:
            return self.GASOLINE_INSURANCE_COST #Årlig forsikring bensin
        else:
            return ValueError("Ikke støtte for type bil")


    '''
    Håndtering av årlig trafikk avgift, håndterer også skuddår
    '''
    def get_traffic_fee(self):
        year = datetime.datetime.now().year
        days_in_year = 366 if calendar.isleap(year) else 365
        return self.TRAFFIC_FEE_COST * 365

    '''
    Utregning av drivstoff basert på type bil
    '''
    def get_fuel_cost(self):
        if self.type == FuelType.EL:
            pr_km = self.EL_FUEL_PER_KM
            price_kwh = self.EL_PRICE
            return self.yearly_km * pr_km * price_kwh
        elif self.type == FuelType.BENSIN:
            pr_km = self.BENSIN_FUEL_PER_KM
            return self.yearly_km * pr_km
        else:
            raise ValueError("Ikke støtte for type bil")
    
    '''
    Bomavgift basert på typen bil
    '''
    def get_toll(self):
        if self.type == FuelType.EL:
            return self.EL_TOLL_FEE * self.yearly_km
        elif self.type == FuelType.BENSIN:
            return self.BENSIN_TOLL_FEE * self.yearly_km
        else:
            raise ValueError("Ikke støtte for type bil")

    def get_annual_cost(self):
        return self.insurance + self.traffic_fee + self.fuel_cost + self.toll
    
    '''
    Representerer Car objektet som string
    '''
    def __str__(self):
        return(f"Type: {self.type.value.capitalize()}\n"
                f"Km/år: {self.yearly_km} km"
                f"\nForsikring: {self.insurance} kr"
                f"\nTrafikkforsikringsavgift: {self.traffic_fee:.2f} kr"
                f"\nDrivstoffbruk: {self.fuel_cost:.2f} kr"
                f"\nBomavgift: {self.toll:.2f} kr"
                f"\nÅrlige kostnader totalt: {self.annual_cost:.2f} kr")
# initialise the by_bus and by_car parameters and default distances for car and bus travellers
by_bus = [20, 20, 20, 3, 20, 21]
by_car = [1, 1, 3, 1, 2, 2, 12, 12]
# initialise individual number
individual_number = 0.91783

# define the single function
def by_bus_greener_from_home_greater_than_by_car(by_bus, by_car):

    # multiply bus travel default distances x 0.91783
    adjusted_bus_distances = [distance * individual_number for distance in by_bus]
    
    # multiply car travel default distances x 0.91783
    adjusted_car_distances = [distance * individual_number for distance in by_car]

    # count number of bus travel distances that are greater than 14
    bus_greener_count = sum(1 for distance in adjusted_bus_distances if distance > 14)
    
    # count number of car travel distances that are greater than 7.5
    car_greener_count = sum(1 for distance in adjusted_car_distances if distance > 7.5)

    # divide number of tipping point bus travel distances by the number of total bus travel distances and x 100
    bus_percentage = (bus_greener_count / len(by_bus)) * 100

    # divide number of tipping point car travel distances by the number of total car travel distances and x 100
    car_percentage = (car_greener_count / len(by_car)) * 100

    # if the percentage of tipping point bus travellers is greater than the percentage of tipping point car travellers
    if bus_percentage > car_percentage:
    # return “True”
        return True
    # else, return “False”
    else:
        return False




from geopy import distance
from config_data.config import COLLEGE_LAT, COLLEGE_LON


def calculate_distance(lat, lon):
    """
    Вычисляет дистанцию между заданными координатами геолокации
    """
    college_location = (COLLEGE_LAT, COLLEGE_LON)
    student_location = (lat, lon)
    dist = distance.distance(college_location, student_location).meters
    return dist


# COLLEGE_LAT = 42.907180514571536
# COLLEGE_LON = 71.36578494856592

# my_lat = 42.92346942215383
# my_lon = 71.39973128206051

# print(calculate_distance(COLLEGE_LAT, COLLEGE_LON, my_lat, my_lon))

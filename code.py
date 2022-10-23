def get_nearest_exit(row_number):
    if row_number < 15:
        location = 'front'

    elif row_number < 30:
        location = 'middle'

    else:
        location = 'back'

    return location


def get_daily_movie():
    print('Retrieving the movie set to play on today\'s flight...')
    return 'Parasite'


def get_licensed_movies():
    print('Retrieving the list of licensed movies from the database...')
    licensed_movies = ['Parasite', 'Nomadland', 'Roma']
    return licensed_movies


def get_wifi_status():
    print('Checking WiFi signal...')
    print('WiFi is inactive')
    return False


def get_device_temp():
    print('Reading the temperature of the entertainment system device...')
    return 40


def get_maximum_display_brightness():
    print('Calculating maximum display brightness in nits...')
    return 399.99999999


def get_daily_movies():
    print('Retrieving the movie set to play on today\'s flight...')
    return ['Parasite', 'Nomadland', 'Roma', 'Black Widow', 'Spiral']


# Означає, що зараз у нас регулярний літак (звичайний без media onboarding systems)
def regional_jet():
    return True


class FormError(Exception):
    pass


def issue_survey():
    print('Opening customer survey')
    raise FormError('An error occurred when opening customer survey form!')


def log_customer_complaint():
    print('Opening customer complaint form')
    print('Logged customer complaint')
    return 'Success'

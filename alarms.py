import warnings


class PowerError(Exception):
    pass


class GasolineLevelWarning(Warning):
    pass


def power_outage_detected(outage_detected):
    if outage_detected:
        raise PowerError('A power outage has been detected somewhere in the system')
    else:
        print('All systems receiving power')


def gasoline_level_check(liters):
    if liters < 200:
        warnings.warn('Gasoline level has fallen below 200 liters', GasolineLevelWarning)
    else:
        print('Gasoline level are adequate')

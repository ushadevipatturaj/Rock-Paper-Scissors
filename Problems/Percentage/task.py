def get_percentage(rate, decimalpt=None):
    if decimalpt is not None:
        return str(round((rate * 100), decimalpt)) + "%"
    return str(int((rate * 100))) + "%"

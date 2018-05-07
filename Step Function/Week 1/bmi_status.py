# def bmi_status(mass, height):
#     """For adults only. Mass should be in kilograms and height in metres."""
#     bmi = compute_bmi(mass, height)
#
#     if bmi < 25:
#         status = "NORMAL"
#     elif bmi < 29:
#         status = "OVERWEIGHT"
#     else:
#         status = "OBESE"
#
#     return status


def bmi_status(mass, height, is_adult):
    """Mass should be in kilograms and height in metres."""
    bmi = compute_bmi(mass, height)

    if is_adult:
        if bmi < 25:
            status = "NORMAL"
        elif bmi < 29:
            status = "OVERWEIGHT"
        else:
            status = "OBESE"
    else:
        if bmi < 22:
            status = "NORMAL"
        elif bmi < 25:
            status = "OVERWEIGHT"
        else:
            status = "OBESE"

    return status

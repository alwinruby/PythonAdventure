# def bmi_status_child(mass, height):
#     """For children only. Mass should be in kilograms and height in metres."""
#     bmi = mass / (height ** 2)
#     print("Body mass index is {0:.1f}".format(bmi))
#
#     if bmi < 22:
#         status = "NORMAL"
#     elif bmi < 25:
#         status = "OVERWEIGHT"
#     else:
#         status = "OBESE"
#
#     return status
#
# print(bmi_status_child(45, 1.3))


def bmi_status_child(mass, height):
    """For children only. Mass should be in kilograms and height in metres."""
    bmi = compute_bmi(mass, height)

    if bmi < 22:
        status = "NORMAL"
    elif bmi < 25:
        status = "OVERWEIGHT"
    else:
        status = "OBESE"

    return status

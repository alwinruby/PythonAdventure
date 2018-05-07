# Calculate the BMI status of each of the three musketeers, by using a loop and the bmi_status() function which you modified in the previous section, to handle both adult and children.
#
# Use the following dictionary:
#
# musketeers = {
#
#     "Athos":{
#         "mass":65,
#         "height":1.75
#     },
#
#     "Porthos ":{
#         "mass":75,
#         "height":1.62
#     },
#     "Aramis":{
#         "mass":95,
#         "height":1.8
#     }
# }

musketeers = {
    "Athos":{
        "mass":65,
        "height":1.75
    },

    "Porthos ":{
        "mass":75,
        "height":1.62
    },
    "Aramis":{
        "mass":95,
        "height":1.8
    }

}

for name,body_stat in musketeers.items():
    mass = body_stat['mass']
    height = body_stat['height']
    print('The BMI status of {0} is {1}'.format(name,bmi_status(mass,height, True)))

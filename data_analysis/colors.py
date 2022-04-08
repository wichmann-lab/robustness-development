"""
Define color scheme
"""


def rgb(r, g, b, divide_by=255.0):
    """Convenience function: return colour in [0, 1]."""
    return (r/divide_by, g/divide_by, b/divide_by)

age5 = rgb(165,15,21)
age4 = rgb(222,45,38)
age3 = rgb(251,106,74)
age2 = rgb(252,146,114)
age1 = rgb(252,187,161)

vgg19 = rgb(188,189,220)
resnext = rgb(158,202,225)
bitm = rgb(107,174,214)
swsl = rgb(33,113,181)
swag = rgb(8,48,107)

errorK_DNN = rgb(55,126,184)

palette = [age1, age2, age5, errorK_DNN, age1, age1, age2, age1, age2, age5]
palette2 = [age1, age2, age5, errorK_DNN, age2, age5, age5, errorK_DNN, errorK_DNN, errorK_DNN]
marker_error_box_mean = rgb(51,160,44)
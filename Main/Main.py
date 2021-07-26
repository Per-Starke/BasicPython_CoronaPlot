from visualization.plot import *

val = input("What plot do you want to see? Type in the corresponding number and hit return, then wait "
            "until the plot shows up!\n"
            "'1' for 'Total incidence',\n"
            "'2' for 'Incidence per age group',\n"
            "'3' for 'Incidende per sex',\n"
            "'4' for 'Incidence per state'\n")

repeat = True

while repeat:
    if val == "1":
        plot_incidence_total()
        repeat = False
    elif val == "2":
        plot_incidence_var_age()
        repeat = False
    elif val == "3":
        plot_incidence_var_sex()
        repeat = False
    elif val == "4":
        plot_incidence_var_state()
        repeat = False
    else:
        print("No valid input! ")
        val = input("What plot do you want to see? Type\n"
                    "'1' for 'Total incidence',\n"
                    "'2' for 'Incidence per age group',\n"
                    "'3' for 'Incidende per sex',\n"
                    "'4' for 'Incidence per state'\n")

plt.show()

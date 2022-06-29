from console_output import bcolors
from colorama import Fore, Style

def printGreeting():
    print("Hello! Thank you for flying wiht us!")
    print("\n\n")
    print(bcolors.OKCYAN,"            ###                                                              ")
    print(bcolors.OKCYAN,"           #   #                                                             ")
    print(bcolors.OKCYAN," #######    #    #                                                           ")
    print(bcolors.OKCYAN,"  ##   ###   #    #                                                          ")
    print(bcolors.OKCYAN,"    ##  ######    ###O###O###O###O###                                        ")
    print(bcolors.OKCYAN,"     ##                            || #                                      ")
    print(bcolors.OKCYAN,"     ##      0  []    O    O    O  || #                                      ")
    print(bcolors.OKCYAN,"       #######    ###O###O###O###O###                                        ")
    print(bcolors.OKCYAN,"            #    #                                                           ")
    print(bcolors.OKCYAN,"           #    #                                                            ")
    print(bcolors.OKCYAN,"          #    #                                                             ")
    print(bcolors.OKCYAN,"           ###                                                               ")
    print(Style.RESET_ALL, "\n\n")
    print("Would you like to find an airport or see all airports?")

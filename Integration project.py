#Andrew A Krupp
#Integration project

#Idea: quantify the ratio of playtime spent to meaningful loot gain in the FPS-MMO Destiny2

#What is Meaningful Loot?
#In Destiny 2 almost all activities grant rewards in the form of materials, armor, weapons, or gear.

#meaningful_materials= Enhancment cores, Enhancement Prisms, Ascendant shards, and Upgrade Modules
#meaningful_armor= Armor with stat rolls higher than 60
#meaningful_weapons= Weapon rewards that have desireable perks, masterwork bonuses, and archetypes (the "god roll")
#meaningful_gear= Shaders, sparrows, ships, and ornaments gained that are not already owned by the player

#To put it simply, an experienced Destiny 2 player automatically dismantles all items that are not included "meaningful" guidelines that I described above.
#ONLY MEANINGFUL LOOT REWARDS MATTER

#Destiny 2 determines quality and type of rewards based on what activity the player is participating in

#Purpose of this program: discover what activity is most efficient at gaining meaningful rewards for the time spent

print('Welcome to my Integration project!')

user_name = input('What is your name? ')
print('My name is Andrew Krupp, known as KD on steam, the creator of this program.')
user_steam_name = input('What is your steam Username? ')

print('This program is designed to help you,', user_name + ', optimize your time spent in Destiny 2')
#used the + string operator here to attach the comma to the variable for the users name to keep grammar

user_average_time_spent = input('On Average, how much time do you spend in Destiny 2 every season (in hours)? ')
user_average_time_spent_num = float(user_average_time_spent)

user_average_loot = input('If you had to guess, how much gear or legendary materials that you gain throughout a season do you end up keeping? ')
user_average_loot_num = float(user_average_loot)


average_loot_gain = (user_average_loot_num / user_average_time_spent_num)
#used division operator to calculate a ratio for loot gain to time spent in hours

floor_average_loot_gain = (user_average_loot_num // user_average_time_spent_num)
#used floor division operator to calculate the whole number amount of loot gained, i.e. removed remainder

modulus_average_loot_gain = (user_average_loot_num % user_average_time_spent_num)
#used modulus to display the remainder when dividing

print('This is the amount of loot you gain per hour every season:', average_loot_gain)


print('Whole number amount because you cannot have a partial piece of loot in Destiny 2:', floor_average_loot_gain)

print('remainder for the curious:', modulus_average_loot_gain)
print()

user_rhetoric_answer = input('Seems low right? ')
while user_rhetoric_answer != 'yes':
    #!= for a string, meaning "if the user does not enter 'yes', print the next statement
    print("You were supposed to say yes... Are you sure you're answering truthfully? restarting...")
    user_rhetoric_answer = input('Seems low right? ')
else:
    print('It is', 'very '*5 + 'low for a game all about gaining that sweet loot (for some players, at least).')
#here, I used a while loop to mess with the user a bit.
print()

print('This program was written between 01', '15', '21', sep = '/', end= ' and ')
print('02', '04', '21', sep = '/', end = '')

print(', so things may have changed by the time you,', user_name + ', are using this program. But at the time of this programs creation there are two types of loot in Destiny 2.')
print()

print('That is the reason for the creation of this program: to help you,', user_name + ', determine how to best optomize the way to get one of these types of loot consistently')
print()

print('------------------------------------------------------------------------------')

#In Destiny 2, blue loot is extremely useless. It is called blue because of the background behind the gear image, and it is immediately thrown in the trash or 'dismantled'. This is unless the player is leveling, in which case the blue gear will give very small increases in power until a cap, after which the gear becomes useless again.

user_amount_guess_blue_loot = input('How many blues do you think you get throught any season? ')
user_amount_guess_blue_loot_num = float(user_amount_guess_blue_loot)

bungie_loot_amount_per_hour = 30
#source: Bungie.net       . They provide statistics through a complicated to get to link.

print('According to Bungie Statistics, a player recieves 30 pieces of gear loot every hour of playtime. So, if we do the math....')
print()

user_amount_blue_loot =  bungie_loot_amount_per_hour * user_average_time_spent_num
#used multiplication operator here to calculate the approximate amount of blues gained per season

exponent_user_anount_blue_loot = bungie_loot_amount_per_hour ** user_average_time_spent_num
#used exponent operator for no paticular reason other than it is required by sprint 1. It raises the first number to the power of the second number.

addition_user_amount_blue_loot = bungie_loot_amount_per_hour + user_average_time_spent_num
#used addition operator for no paticular reason other than it is required by sprint 1. It adds the first number and second number together

subtraction_user_amount_blue_loot = bungie_loot_amount_per_hour - user_average_time_spent_num
#used subtraction operator for no paticular reason other than it is required by sprint 1. It subtracts the first number from the second number.

print('You gain ', user_amount_blue_loot, 'blues every season. Now that is a truly stupid amount of meaningless loot.')
print(exponent_user_anount_blue_loot)
print(addition_user_amount_blue_loot)
print(subtraction_user_amount_blue_loot)
print()
print('Lets talk about meaningful loot.')
print()
print('Meaningful loot (as described by me, and most of the community) is loot you actually use/keep during or after the season you get it in')
print('Meaningful look includes: Enhancment cores, Enhancement Prisms, Ascendant shards, Upgrade Modules, Armor with stat rolls higher than 60, Weapon rewards that have desireable perks, masterwork bonuses, and archetypes (the "god roll"),Shaders, sparrows, ships, and ornaments gained that are not already owned by the player.')
print()
for row in range(5):
    for column in range(5):
        print("*" + " ", end=" ")
    print()
    #here I use an integrated 'for' loop to create a clear separation in the parts of my program
print('Everything else is useless and is not worth your time. So how do you get this meaningful loot? Here is the calculator:')
print()


def calculate_strikes():
    meaningless_strike_loot = int(input('How much loot did you delete after your play-session? '))
    meaningful_strike_loot = int(input('How much loot did you keep after your play-session? '))
    strike_time_hours = int(input('How much time did you spend in your play session (in hours)? '))


    strike_loot = meaningful_strike_loot / strike_time_hours
    print('For strikes:', strike_loot, 'per hour')
    print()

def calculate_crucible():
    meaningless_crucible_loot = int(input('How much loot did you delete after your play-session? '))
    meaningful_crucible_loot = int(input('How much loot did you keep after your play-session? '))
    crucible_time_hours = int(input('How much time did you spend in your play session (in hours)? '))


    crucible_loot = meaningful_crucible_loot / crucible_time_hours
    print('For crucible:', crucible_loot, 'per hour')
    print()

def calculate_gambit():
    meaningless_gambit_loot = int(input('How much loot did you delete after your play-session? '))
    meaningful_gambit_loot = int(input('How much loot did you keep after your play-session? '))
    gambit_time_hours = int(input('How much time did you spend in your play session (in hours)? '))


    gambit_loot = meaningful_gambit_loot / gambit_time_hours
    print('For gambit:', gambit_loot, 'per hour')
    print()

def calculate_nightfalls():
    meaningless_nightfall_loot = int(input('How much loot did you delete after your play-session? '))
    meaningful_nightfall_loot = int(input('How much loot did you keep after your play-session? '))
    nightfall_time_hours = int(input('How much time did you spend in your play session (in hours)? '))

    nightfall_loot = meaningful_nightfall_loot / nightfall_time_hours
    print('For Nightfalls:', nightfall_loot, 'per hour')
    print()

def calculate_raids(x, y):

    raid_loot = x / y
    print('For Raids:', raid_loot, 'per hour')
    print()
    #This is the function I made that has parameters. It basically works the same way as the others, but it takes the arguments in the main function.

def calculate_seasonal():
    meaningless_seasonal_loot = int(input('How much loot did you delete after your play-session? '))
    meaningful_seasonal_loot = int(input('How much loot did you keep after your play-session? '))
    seasonal_time_hours = int(input('How much time did you spend in your play session (in hours)? '))

    seasonal_loot = meaningful_seasonal_loot / seasonal_time_hours
    print('For Seasonal Activities:', seasonal_loot, 'per hour')
    print()

def main():
    print("Welcome to the D2 efficiency calculator. Please choose an option: ")
    print('1 = Strikes \n 2 = Crucible \n 3 = Gambit')
    print('4 = Nightfalls \n 5 = Raids \n 6 = Seasonal Activity')
    user_choice = int(input('Choice: '))
    if user_choice == 1:
        calculate_strikes()
    elif user_choice == 2:
        calculate_crucible()
    elif user_choice == 3:
        calculate_gambit()
    elif user_choice == 4:
        calculate_nightfalls()
    elif user_choice == 5:
        meaningless_raid_loot = int(input('How much loot did you delete after your play-session? '))
        meaningful_raid_loot = int(input('How much loot did you keep after your play-session? '))
        raid_time_hours = int(input('How much time did you spend in your play session (in hours)? '))
        calculate_raids(meaningful_raid_loot, raid_time_hours)
        #sending arguments to my function that has parameters
    elif user_choice == 6:
        calculate_seasonal()
    else:
        print('invalid choice. restarting... ')
        main()
#I turned the end part of my previous program into more of a calculator with a menu by creating functions for each game activity
main()

user_input_boolean_test = int(input('enter a number that is an integer and not -13: '))
if user_input_boolean_test > 1:
    print('congrats! that number is larger than 1!')
elif user_input_boolean_test < 1 and user_input_boolean_test > -1:
    print('congrats! that number is 0')
elif user_input_boolean_test == 1 or user_input_boolean_test == -1:
    print('congrats! that number is either 1 or -1!')
elif user_input_boolean_test < -1 and user_input_boolean_test != -13:
    print('congrats! that is a negative integer smaller than -1!!')
elif not(user_input_boolean_test == -13):
    print('you did not enter -13, I just changed the way the computer interpreted it :)')
    #users will never see this option because even if -13 is picked, the not operator makes it so that line is not run
else:
    print("Invalid input detected. Non-integers and -13 are not allowed. You are a rebel, I'm calling the police ...")
#here, I played around a bit because i got bored of my original program and still needed to add booleans to my project

print("Thank you for using my program! Hopefully my programing and Destiny 2 will improve enough for this program to be obsolete in a year or so!")


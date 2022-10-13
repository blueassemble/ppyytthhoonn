loaded_config = """# Rocket Ship Configuration File!
fuel_tanks=4
oxygen_tanks=3
initial_propulsion_level=84
$ End of file"""

# parse loaded_config into a dictionary
parsed_config = {}
for line in loaded_config.splitlines():
    # try to split the line into key and value
    try:
        key, value = line.split("=")
        parsed_config[key] = value
    except ValueError:
        print("Unable to parse: {}".format(line))
        continue

# print the parsed config
print(parsed_config)


true_values = ['yes', 'y']
false_values = ['no', 'n']

#declare function str_to_bool to convert string to boolean with one parameter value
def str_to_bool(value):
    #convert value to lower case
    value = value.lower()
    #if value is in true_values return True
    if value in true_values:
        return True
    #if value is in false_values return False
    elif value in false_values:
        return False
    #if value is not in true_values or false_values raise ValueError
    else:
        raise ValueError("Unable to convert {} to bool".format(value))

#get input from user to convert to boolean
user_input = input("Enter yes or no: ")
#call function str_to_bool with parameter user_input
converted_value = str_to_bool(user_input)
#print converted_value
print(converted_value)
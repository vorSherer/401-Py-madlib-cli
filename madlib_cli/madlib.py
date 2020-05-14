def welcome():
    '''
    Welcome message to the user, explaining the Madlib process and command line interactions.
    '''
    print(dedent('''
    ***********************************************
    ** Welcome to Madlibs-cli! Provide answers   **
    ** to the prompts given;   For example,      **
    **    a 'noun' is a person, place, or thing; **
    **    a 'plural' means more than one item    **
    **    a 'verb' is an action word;            **
    **    an adjective describes a noun          **
    ** (like 'cold', 'slippery' or 'green') and  **
    **    an 'adverb' typically ends in '-ly.'   **
    ** Press enter after each entry. When all    **
    ** entries have been received, the resulting **
    ** Madlib will be displayed.  Enjoy!         **
    ***********************************************
    '''))


def read_template(path):
    '''
    Takes in a path to text file and returns a stripped string of the file’s contents.
    '''
    with open(path) as template:
        contents = template.read()
    return contents


# def getKeys(formatString):
#     '''formatString is a format string with embedded dictionary keys.
#     Return a list containing all the keys from the format string.'''

#     keyList = list()
#     end = 0
#     repetitions = formatString.count('{')
#     for i in range(repetitions):
#         start = formatString.find('{', end) + 1
#         end = formatString.find('}', start)
#         key = formatString[start : end]
#         keyList.append(key)

#     return keyList



def madlib_parser():
    '''
    Takes in a template string and returns a string with language parts removed and a separate list of those language parts.
    '''
    pass

def template_merge():
    '''
    Takes in a “bare” template and a list of user entered language parts, and returns a string with the language parts inserted into the template.
    '''
    pass

# if __name__ == "__main__":
#     welcome
    
import datetime

# Group Name : i want to cry

# Group Members :  1. Mandhiren Singh Gurdev Singh
#                  2. Shuen Y'ng Tan
#                  3. Eng Jie Lee
#                  4. Steve Jevon Rahardjo

### WELCOME TO OUR ASSESSMENT 3, FIT1045 SEM 1 2022 :) ###


# Note : I shall use the Google Style format for my docstrings.
#        To access the docstrings, type help(function_name) in the
#        if __name__ == "__main__": section, for example, help(make_person)


def make_person(this_id, name, date_of_birth):
    '''
    Creates a Python dict with the person's properties. The key is a string and
    the value is the respective property.

    Args:
      this_id (int): The integer ID which should be assigned to the produced dict object.
      name (string): The string name representing this person's full name.
      date_of_birth (datetime.date):  A date object representing the date of birth of this person.

    Returns:
      dict: Returns the person dictionary holding these properties.

   Notes:
      Description, args and returns for this function are obtained from this
      slide : https://edstem.org/au/courses/7542/lessons/20930/slides/149067
    '''


    # This block of code creates the dictionary for a specific person based on the input arguments.
    person_properties_dict = {'friends': [],
                              'history': [],
                              'id': this_id,
                              'name': name,
                              'date_of_birth': date_of_birth}

    return person_properties_dict


def find_friendX_inY(person_X, person_Y):
    '''
    Looks for person_X's ID in the friend list of person_Y,
    passing back the position it is found at (or None if not found)

    Args:
      person_X (dict): The dictionary (as defined in the assignment) of the person to look for.
      person_Y (dict): The dictionary (as defined in the assignment) of the person whose friend list we will search within.

    Returns:
      int: Returns the position of person_X's ID within person_Y's friend list (or None if not found)

   Notes:
      Description, args and returns for this function are obtained from this
      slide : https://edstem.org/au/courses/7542/lessons/20930/slides/149067
    '''

    # The code block below gets the friend list of Person Y, as well as the ID of Person X
    person_Y_friend_list = person_Y['friends']
    person_X_id = person_X['id']


    # The code block below checks if person X's ID is in the friends list of person Y
    # by iterating through the int IDs in person_Y_friend_list, and checking if person X's ID
    # is equal to the int ID in Person Y's friend list, pos_of_person_X_in_Y is initialised
    # with the default return value of None (if X's ID is not in Y's friendlist)
    pos_of_person_X_in_Y = None
    for i in range(len(person_Y_friend_list)):
        if person_X_id == person_Y_friend_list[i]:
            pos_of_person_X_in_Y = i

    return pos_of_person_X_in_Y


def make_friendship(person_X, person_Y):
    '''
    Add the IDs of person_X and person_Y to one another's friends list

    Args:
      person_X (dict): The dictionary (as defined in the assignment) of the person X.
      person_Y (dict): The dictionary (as defined in the assignment) of the person Y.

    Returns:
      Does not return anything (None).

   Notes:
      Description, args and returns for this function are obtained from this
      slide : https://edstem.org/au/courses/7542/lessons/20930/slides/149067
    '''

    # The code below gets the IDs and friend lists of person_X and person_Y
    person_X_id = person_X['id']
    person_X_friend_list = person_X['friends']
    person_Y_id = person_Y['id']
    person_Y_friend_list = person_Y['friends']


    # The code block below appends the IDs of Person X and Person Y to one
    # another's friend list.
    # This is done by first checking if the person is trying to add themselves by
    # checking whether their IDs are the same. Then, we check whether they are in each
    # other's friend list by using the find_friendX_inY() function, and append the respective
    # IDs to the friend lists.
    if (person_X_id != person_Y_id) and (find_friendX_inY(person_X, person_Y) == None):
        person_Y_friend_list.append(person_X_id)

    if (person_X_id != person_Y_id) and (find_friendX_inY(person_Y, person_X) == None):
        person_X_friend_list.append(person_Y_id)


    return None


def end_friendship(person_X, person_Y):
    '''
    Go through the friends lists of both people and remove the ID of each from the other's
    dictionary as defined in the assignment.

    Args:
      person_X (dict): The dictionary (as defined in the assignment) of the person X.
      person_Y (dict): The dictionary (as defined in the assignment) of the person Y.

    Returns:
      Does not return anything (None).

   Notes:
      Description, args and returns for this function are obtained from this
      slide : https://edstem.org/au/courses/7542/lessons/20930/slides/149067
    '''

    # Get the IDs and friend lists of person_X and person_Y
    person_X_id = person_X['id']
    person_X_friend_list = person_X['friends']
    person_Y_id = person_Y['id']
    person_Y_friend_list = person_Y['friends']


    # The code block below removes the IDs of Person X and Person Y from one
    # another's friend list.
    # We check whether they are in each other's friend list by using the
    # find_friendX_inY() function, and remove the respective IDs from the friend lists.
    if (find_friendX_inY(person_X, person_Y) != None):
        person_Y_friend_list.remove(person_X_id)

    if (find_friendX_inY(person_Y, person_X) != None):
        person_X_friend_list.remove(person_Y_id)

    return None


def birthday_within_X_days_of_Y(person, days, comparison_date):
    '''
    We consider both the 'date_of_birth' property of person and the given comparison_date.
    If this comparison date is no more than days on either side of the
    birthday day in the closest year we should return True and otherwise False

    Args:
      person (dict): The dictionary (as defined in the assignment) of the person to look within.
      days (int): The number of days (maximum) between the comparison date and birthday in the same year.
      comparison_date (datetime.date): The date to compare with.

    Returns:
      bool: True if birthday is within days(arg) days, else False

   Notes:
      Description, args and returns for this function are obtained from this
      slide : https://edstem.org/au/courses/7542/lessons/20930/slides/149067
    '''

    # Gets date of birth of person and the year of the comparison date.
    person_DOB = person['date_of_birth'] #datetime object
    comparison_date_year = comparison_date.year


    # The code below is non-trivial. It takes the minimum absolute difference with the comparison_date at the
    # year before, current year and year after of the person's DOB, then it gets the number of days between
    # the two dates by using.days. Basically, it standardises the comparison date's year with the month and
    # day of the person's DOB, then it subtracts the comparison_date datetime.date obj to obtain a timedelta,
    # then I extracted out the .days from it to obtain the comparison num of days.
    comparison_days = (min(((datetime.date(comparison_date_year + i, person_DOB.month, person_DOB.day) - comparison_date).days for i in (-1, 0, 1)), key=abs))


    # This code below just checks if the comparison value is lesser than the number of days and sets
    # the respective bool value to is_within_range appropriately.
    if abs(comparison_days) <= days:
        is_within_range = True
    else:
        is_within_range = False

    return is_within_range


def add_person(dict_of_people, name, date_of_birth):
    '''
    Add a new person to a Python dictionary dict_of_people containing a set of person dicts (as defined in part 1)
    and returns the ID of the newly added person.

    Args:
      dict_of_people (dict): The structure holding people using the ID as key. Values are person dictionaries.
      name (string): A string representing this person's full name.
      date_of_birth (datetime.date): A date object representing the date of birth of this person.

    Returns:
      int: The integer ID of the person just added.

   Notes:
      Description, args and returns for this function are obtained from this
      slide : https://edstem.org/au/courses/7542/lessons/20930/slides/149114
    '''

    # The code block below gets the highest ID of person amongst the people in
    # the people dictionary.
    # If the length of the dictionary is not zero, we get the max values of the list
    # of ID keys in the dictionary (to obtain the highest ID). Else, the highest ID is 0.
    if len(dict_of_people) != 0:
        highest_existing_id = max(list(dict_of_people.keys()))
    else:
        highest_existing_id = 0


    # The code below sets person's ID by using the highest existing ID, creates a new
    # person based on that ID, name and DOB, and finally adds the person to the people_dict
    # by using the person's ID and person_dict.
    person_id = highest_existing_id + 1
    person_dict = make_person(person_id, name, date_of_birth)
    dict_of_people[person_id] = person_dict


    return person_id



def get_person_by_id(dict_of_people, find_id):
    '''
    Accesses the person dict (as defined in part 1) in the dict_of_people matching the ID find_id.

    Args:
      dict_of_people (dict): The structure holding people using the ID as key. Values are person dictionaries.
      find_id (int): The ID of the person dict to retrieve.

    Returns:
      dict: The dictionary of the person matching the ID given or None if no such ID exists.

   Notes:
      Description, args and returns for this function are obtained from this
      slide : https://edstem.org/au/courses/7542/lessons/20930/slides/149114
    '''

    # The code block below checks if the ID is in the dict_of_people, then
    # returns the matching dictionary of the person by using the ID.
    # This is done by checking whether the ID is in the keys of the dict_of_people,
    # then setting the matching dictionary appropriately.
    if find_id in list(dict_of_people.keys()):
        matching_dict = dict_of_people[find_id]
    else:
        matching_dict = None

    return matching_dict



def convert_lines_to_friendships(lines):
    '''
    Reads a list of strings with a pre-defined format (from assignment specs) and creates
    a dictionary of person dictionary objects, finally returns the full dictionary once
    complete.

    Args:
      lines (list): List of strings with a pre-defined format (from assignment specs).

    Returns:
      dict: The dictionary of the person dictionary objects.

   Notes:
      Description, args and returns for this function are obtained from this
      slide : https://edstem.org/au/courses/7542/lessons/20930/slides/149117
    '''


    # Initialisation of variables to use later.
    friendship_list_names = []
    friendship_list_DOB = []
    nested_list_of_friend_pairs = []
    network_dictionary = {}


    # The code block below gets the names and DOBs of the friends and stores
    # them in friendship_list_names and friendship_list_DOB respectively.
    #
    # It basically works by using the fact that if "<->" is in the string, a
    # connection is found. I replaced the "<->" with ",", then I split the
    # data based on "," and appended the names and DOB to the friendship_list_names
    # and friendship_list_DOB respectively by using an if clause (if its not already in the list)
    # Finally, we need to make a friendship between them (later on),
    # so I made a nested list nested_list_of_friend_pairs to use later on.

    for i in range(len(lines)):
        if "<->" in lines[i]: # if a connection is found, make a friendship between them
                friendship_list_csv = lines[i].replace("<->", ",")
                friendship_list = friendship_list_csv.split(",")
                nested_list_of_friend_pairs.append([friendship_list[0], friendship_list[2]])

                if friendship_list[0] not in friendship_list_names:
                    friendship_list_names.append(friendship_list[0])
                    friendship_list_DOB.append(datetime.datetime.strptime(friendship_list[1], "%Y-%m-%d").date())

                if friendship_list[2] not in friendship_list_names:
                    friendship_list_names.append(friendship_list[2])
                    friendship_list_DOB.append(datetime.datetime.strptime(friendship_list[3], "%Y-%m-%d").date())

        else:
            friendship_list = lines[i].split(",")


            if friendship_list[0] not in friendship_list_names:
                friendship_list_names.append(friendship_list[0])
                friendship_list_DOB.append(datetime.datetime.strptime(friendship_list[1], "%Y-%m-%d").date())



    # The code block below adds the people in friendship_list_names using their DOBs in friendship_list_DOB
    # and also appends the IDs of each individual in the people_dict by calling the add_person() function
    # with each name and DOB. This worked by iterating through the friendship_list_names using a for loop and
    # calling add_person() in each iteration.
    list_of_IDs = []
    for i in range(len(friendship_list_names)):
        list_of_IDs.append(add_person(network_dictionary, friendship_list_names[i], friendship_list_DOB[i]))


    # The code below creates a dict to store IDs based on the names using dict comprehension, this basically maps
    # the names to the IDs of each individual so that I can use it to update the network dictionary later on, with ease.
    names_to_IDs_dict = {key:value for key, value in zip(friendship_list_names, list_of_IDs)}


    # The code block below updates the network dictionary by iterating through the nested_list_of_friend_pairs we
    # made earlier, and making a friendship between them using our make_friendship() function.
    for i in range(len(nested_list_of_friend_pairs)):
        make_friendship(network_dictionary[names_to_IDs_dict[nested_list_of_friend_pairs[i][0]]], network_dictionary[names_to_IDs_dict[nested_list_of_friend_pairs[i][1]]])

    return network_dictionary



def new_post(content, owner, tagged):
    '''
    Creates a tuple containing the text content, ID of the author and list of tagged IDs (in this order).

    Args:
      content (string): String content (assume this will be plain text; e.g. no links)
      owner (dict): The dictionary representing the author of the post.
      tagged (list): The list of integer IDs of friends the author is attempting to tag in this post.

    Returns:
      tuple: The tuple holding the finalised post (with only valid friends tagged)

   Notes:
      Description, args and returns for this function are obtained from this
      slide : https://edstem.org/au/courses/7542/lessons/20930/slides/149126
    '''

    valid_friends_tags_list = []


    # The code block below checks the validity of the tagged people and makes the finalised tuple.
    # This works by iterating through the tagged people by the author and check whether the tagged people are in
    # his friend list, to get the valid tags. Then, the respective tuple is created self-explanatorily, and appended
    # to the history of the author.
    for i in range(len(tagged)):
        if tagged[i] in owner["friends"]:
            valid_friends_tags_list.append(tagged[i])

    finalised_post_tuple = (content, owner["id"], valid_friends_tags_list)
    owner["history"].append(finalised_post_tuple)


    return finalised_post_tuple


def birthdays_within_a_week_of(person_id, people_dict, comparison):
    '''
    Looks through the friends of the person in the people dict with ID matching person_id
    and creates a list of IDs for those friends of person_id who have a birthday within 7
    days (either side) of the comparison date.

    Args:
      person_id (int): The integer ID of the person to look at.
      people_dict (dict): The structure (as defined in part 2) holding all unique people.
      comparison (datetime.date): The date to compare birthdays against.

    Returns:
      tuple: A list of IDs of all friends of person_id who have a birthday upcoming (or past)
             within 7 days of the comparison date.

   Notes:
      Description, args and returns for this function are obtained from this
      slide : https://edstem.org/au/courses/7542/lessons/20930/slides/149127
    '''


    # The code block below gets the list of IDs within a week of comparison date.
    # This works by initialising final list of IDs to store the list of IDs of all friends of person_id
    # who have a birthday upcoming (or past) within 7 days of the comparison date, and obtaining the friend
    # list of the selected person from the people_dict. Then, we iterate through the friend list of the
    # selected person and checks if the birthday of the person is within 7 days of the comparison.
    # If it is, then append their ID to the list.

    final_id_list = []
    friend_list_of_selected_person = people_dict[person_id]["friends"]

    for i in range(len(friend_list_of_selected_person)):
        if birthday_within_X_days_of_Y(people_dict[friend_list_of_selected_person[i]], 7, comparison):
            final_id_list.append(friend_list_of_selected_person[i])


    return final_id_list


def make_birthday_posts(people_dict, from_person_id, for_people_ids):
    '''
    Given a list of IDs representing the friends of from_person_id with upcoming birthdays,
    it makes and returns a list of birthday posts.

    Args:
      people_dict (dict): The structure (as defined in part 2) holding all unique people.
      from_person_id (int): The integer ID of the person to look at.
      for_people_ids (list): The list of friends of from_person_id with birthdays coming up.

    Returns:
      list: A list of birthday posts created.

   Notes:
      Description, args and returns for this function are obtained from this
      slide : https://edstem.org/au/courses/7542/lessons/20930/slides/149127
    '''


    # The code block below makes a list of birthday strings for people in for_people_ids
    # by iterating through the list of people that we want to wish, then store the wishes in a list
    list_of_bday_strings = []
    for i in range(len(for_people_ids)):
        list_of_bday_strings.append(f"Happy birthday {people_dict[for_people_ids[i]]['name']}! Hope you have a good one!")


    # The code block below makes a list of birthday posts (which are tuples) for people in
    # for_people_ids by iterating through for_people_ids and appending the tuples to the list of birthday posts.
    list_of_birthday_posts = []
    for i in range(len(for_people_ids)):
        list_of_birthday_posts.append(new_post(list_of_bday_strings[i], people_dict[from_person_id], [for_people_ids[i]]))


    return list_of_birthday_posts



if __name__ == "__main__":

    dhiren = make_person(1, "Dhiren", datetime.date(2000, 4, 28))

    print(dhiren)

    # Testing with example values.
    # people = ['Fred,2022-02-01<->Jenny,2004-11-18',
    #           'Jiang,1942-09-16<->Sasha,1834-02-02',
    #           'Corey,2015-05-22',
    #           'Sasha,1834-02-02<->Amir,1981-08-11']
    #
    # dict_network = convert_lines_to_friendships(people)
    #
    # print(dict_network)
import datetime

class Person:
    """A class to represent an individual person as previously defined through step 1.

    Attributes:
        id (int): id of person
        name (str): name of person
        date_of_birth (datetime.date): date of birth of person
        friends (list): list of integers (which will be the ids corresponding to the friend)
        history (list): list of posts made by this person

    """

    def __init__(self, this_id, name, date_of_birth):
        """
        Constructs all the necessary attributes for the Person object.

        Args:
            this_id (int): id of person
            name (str): name of person
            date_of_birth (datetime.date): date of birth of person

        """
        self.id = this_id
        self.name = name
        self.date_of_birth = date_of_birth
        self.friends = []
        self.history = []


    def birthday_within_X_days_of_Y(self, days, comparison_date):
        '''
        We consider both the 'date_of_birth' attribute of person and the given comparison_date.
        If this comparison date is no more than days on either side of the
        birthday day in the closest year we should return True and otherwise False

        Args:
          days (int): The number of days (maximum) between the comparison date and birthday in the same year.
          comparison_date (datetime.date): The date to compare with.

        Returns:
          bool: True if birthday is within days(arg) days, else False

       Notes:
          Description, args and returns for this function are obtained from this
          slide : https://edstem.org/au/courses/7542/lessons/20930/slides/149128
        '''


        # Gets date of birth of person and the year of the comparison date.
        person_DOB = self.date_of_birth
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



    def make_friendship(self, other_person):
        '''
        Add the IDs of two people to one another's friend lists.

        Args:
          other_person (Person): The Person instance of other person.

        Returns:
          Does not return anything (None).

       Notes:
          Description, args and returns for this function are obtained from this
          slide : https://edstem.org/au/courses/7542/lessons/20930/slides/149128
        '''

        # The code below gets the IDs and friend lists of person_X and person_Y
        person_X_id = self.id
        person_X_friend_list = self.friends
        person_Y_id = other_person.id
        person_Y_friend_list = other_person.friends


        # The code block below appends the IDs the two people to one
        # another's friend list.
        # This is done by first checking if the person is trying to add themselves by
        # checking whether their IDs are the same. Then, we check whether they are in each
        # other's friend list by using the find_my_friend() method, and append the respective
        # IDs to the friend lists.
        if (person_X_id != person_Y_id) and (self.find_my_friend(other_person) == None):
            person_Y_friend_list.append(person_X_id)

        if (person_X_id != person_Y_id) and (other_person.find_my_friend(self) == None):
            person_X_friend_list.append(person_Y_id)

        return None


    def end_friendship(self, other_person):
        '''
        Removes the IDs of two people from one another's friend lists.

        Args:
          other_person (Person): The Person instance of other person.

        Returns:
          Does not return anything (None).

       Notes:
          Description, args and returns for this function are obtained from this
          slide : https://edstem.org/au/courses/7542/lessons/20930/slides/149128
        '''

        # Get the IDs and friend lists of person_X and person_Y
        person_X_id = self.id
        person_X_friend_list = self.friends
        person_Y_id = other_person.id
        person_Y_friend_list = other_person.friends


        # The code block below removes the IDs of the people from one
        # another's friend list.
        # We check whether they are in each other's friend list by using the
        # find_my_friend() method, and remove the respective IDs from the friend lists.
        if (self.find_my_friend(other_person) != None):
            person_Y_friend_list.remove(person_X_id)

        if (other_person.find_my_friend(self) != None):
            person_X_friend_list.remove(person_Y_id)

        return None



    def find_my_friend(self, other_person):
        '''
        Looks for self's ID in the friend list of other_person,
        passing back the position it is found at (or None if not found)

        Args:
          other_person (Person): The Person instance of other person.

        Returns:
          int: Returns the position of self instance ID within other_person's friend list (or None if not found)

       Notes:
          Description, args and returns for this function are obtained from this
          slide : https://edstem.org/au/courses/7542/lessons/20930/slides/149128
        '''

        # The code block below gets the friend list of Person Y (other_person), as well as the ID of Person X (self)
        person_Y_friend_list = other_person.friends
        person_X_id = self.id


        # The code block below checks if person X's ID is in the friends list of person Y
        # by iterating through the int IDs in person_Y_friend_list, and checking if person X's ID
        # is equal to the int ID in Person Y's friend list, pos_of_person_X_in_Y is initialised
        # with the default return value of None (if X's ID is not in Y's friendlist)
        pos_of_person_X_in_Y = None  # initialising with None
        for i in range(len(person_Y_friend_list)):
            if person_X_id == person_Y_friend_list[i]:
                pos_of_person_X_in_Y = i

        return pos_of_person_X_in_Y



    def make_post(self, content, tagged):
        '''
        Creates a tuple containing the text content, ID of the author and list of tagged IDs (in this order).

        Args:
          content (string): String content (assume this will be plain text; e.g. no links).
          tagged (list): The list of integer IDs of friends the author is attempting to tag in this post.

        Returns:
          tuple: The tuple holding the finalised post (with only valid friends tagged)

       Notes:
          Description, args and returns for this function are obtained from this
          slide : https://edstem.org/au/courses/7542/lessons/20930/slides/149128
        '''

        valid_friends_tags_list = []


        # The code block below checks the validity of the tagged people and makes the finalised tuple.
        # This works by iterating through the tagged people by the author and check whether the tagged people are in
        # his friend list, to get the valid tags. Then, the respective tuple is created self-explanatorily, and appended
        # to the history of the author.
        for i in range(len(tagged)):
            if tagged[i] in self.friends:
                valid_friends_tags_list.append(tagged[i])

        finalised_post_tuple = (content, self.id, valid_friends_tags_list)
        self.history.append(finalised_post_tuple)

        return finalised_post_tuple



    def __str__(self):
        '''
        Represents each instance of the Person class with a string.
        '''
        return f"{self.id} ({self.name}, {self.date_of_birth}) --> {str(self.friends)[1:-1]}"





class SocialNetwork:
    """A class to represent the group of all Person instances in the social network as initially defined in part 2
       and posts they have created.


    Attributes:
        people (dict): a dictionary as defined in part 2 except each person is represented using the Person class rather
                       than the dict from part 1.
        posts (list): a list of posts made by people in the network in order of creation.

    """

    def __init__(self, people_friendship_data, post_history):
        """
        Constructs all the necessary attributes for the SocialNetwork object.

        Args:
            people_friendship_data (list): list of strings with a pre-defined format (from assignment specs).
            post_history (list): list of posts (as would be generated by the make_post method) listed in order of creation

        """

        self.people = {}
        self.posts = []


        # The code below processes people_friendship_data
        # Initialisation of variables to use later.
        friendship_list_names = []
        friendship_list_DOB = []
        nested_list_of_friend_pairs = []


        # The code block below gets the names and DOBs of the friends and stores
        # them in friendship_list_names and friendship_list_DOB respectively.
        #
        # It basically works by using the fact that if "<->" is in the string, a
        # connection is found. I replaced the "<->" with ",", then I split the
        # data based on "," and appended the names and DOB to the friendship_list_names
        # and friendship_list_DOB respectively by using an if clause (if its not already in the list)
        # Finally, we need to make a friendship between them (later on),
        # so I made a nested list nested_list_of_friend_pairs to use later on.
        for i in range(len(people_friendship_data)):
            if "<->" in people_friendship_data[i]:  # if a connection is found, make a friendship between them
                friendship_list_csv = people_friendship_data[i].replace("<->", ",")
                friendship_list = friendship_list_csv.split(",")
                nested_list_of_friend_pairs.append([friendship_list[0], friendship_list[2]])

                if friendship_list[0] not in friendship_list_names:
                    friendship_list_names.append(friendship_list[0])
                    friendship_list_DOB.append(datetime.datetime.strptime(friendship_list[1], "%Y-%m-%d").date())

                if friendship_list[2] not in friendship_list_names:
                    friendship_list_names.append(friendship_list[2])
                    friendship_list_DOB.append(datetime.datetime.strptime(friendship_list[3], "%Y-%m-%d").date())

            else:
                friendship_list = people_friendship_data[i].split(",")

                if friendship_list[0] not in friendship_list_names:
                    friendship_list_names.append(friendship_list[0])
                    friendship_list_DOB.append(datetime.datetime.strptime(friendship_list[1], "%Y-%m-%d").date())



        # The code block below adds the people in friendship_list_names using their DOBs in friendship_list_DOB
        # and also appends the IDs of each individual in the self.people by calling the add_person() function
        # with each name and DOB. This worked by iterating through the friendship_list_names using a for loop and
        # calling add_person() in each iteration.
        list_of_IDs = []
        for i in range(len(friendship_list_names)):
            list_of_IDs.append(self.add_person(friendship_list_names[i], friendship_list_DOB[i]))


        # The code below creates a dict to store IDs based on the names using dict comprehension, this basically maps
        # the names to the IDs of each individual so that I can use it to update the network dictionary later on, with ease.
        names_to_IDs_dict = {key: value for key, value in zip(friendship_list_names, list_of_IDs)}


        # The code block below updates the self.people by iterating through the nested_list_of_friend_pairs we
        # made earlier, and appending it to a nested_list_of_friend_pairs_IDs, then using these IDs to
        # make a friendship between them using our make_friendship() function in another for loop.
        nested_list_of_friend_pairs_IDs = []
        for i in range(len(nested_list_of_friend_pairs)):
            nested_list_of_friend_pairs_IDs.append([names_to_IDs_dict[nested_list_of_friend_pairs[i][0]], names_to_IDs_dict[nested_list_of_friend_pairs[i][1]]])

        for i in range(len(nested_list_of_friend_pairs_IDs)):
            P1 = self.people[nested_list_of_friend_pairs_IDs[i][0]]
            P2 = self.people[nested_list_of_friend_pairs_IDs[i][1]]
            P1.make_friendship(P2)




    def add_person(self, name, date_of_birth):
        '''
        Add a new person to self.people and returns the ID of the newly added person.

        Args:
          name (string): A string representing this person's full name.
          date_of_birth (datetime.date): A date object representing the date of birth of this person.

        Returns:
          int: The integer ID of the person just added.

       Notes:
          Description, args and returns for this function are obtained from this
          slide : https://edstem.org/au/courses/7542/lessons/20930/slides/149128
        '''

        # The code block below gets the highest ID of person amongst the people in
        # self.people.
        # If the length of the dictionary (self.people) is not zero, we get the max values of the list
        # of ID keys in the dictionary (to obtain the highest ID). Else, the highest ID is 0.
        if len(self.people) != 0:
            highest_existing_id = max(list(self.people.keys()))
        else:
            highest_existing_id = 0


        # The code below sets person's ID by using the highest existing ID, creates a new
        # person based on that ID, name and DOB, and finally adds the person to self.people
        # by using the person's ID and person_dict.
        person_id = highest_existing_id + 1
        person_dict = Person(person_id, name, date_of_birth)
        self.people[person_id] = person_dict


        return person_id




    def get_person_by_id(self, find_id):
        '''
        Add a new person to self.people and returns the ID of the newly added person.

        Args:
          find_id (int): The ID of the Person instance to retrieve.

        Returns:
          dict: The dictionary of the person matching the ID given or None if no such ID exists.

       Notes:
          Description, args and returns for this function are obtained from this
          slide : https://edstem.org/au/courses/7542/lessons/20930/slides/149128
        '''



        # The code block below checks if the ID is in the dict_of_people, then
        # returns the matching dictionary of the person by using the ID.
        # This is done by checking whether the ID is in the keys of the dict_of_people,
        # then setting the matching dictionary appropriately.
        if find_id in list(self.people.keys()):
            matching_dict = self.people[find_id]
        else:
            matching_dict = None

        return matching_dict



    def make_birthday_posts(self, from_person_id, comparison_date, range_of_days=7):
        '''
        Determines appropriate friends from_person_id who have birthday within a week(for task 6)
        or within a range_of_days (task 7) on either side of comparison_date. Produces birthday
        posts for each of these friends and appear in both the author's history attribute and
        the posts attribute of this SocialNetwork instance.

        Args:
          from_person_id (int): The integer ID of the person to look at.
          comparison_date (datetime.date): The comparison date object.

        Returns:
          Does not return anything (None).

       Notes:
          Description, args and returns for this function are obtained from this
          slide : https://edstem.org/au/courses/7542/lessons/20930/slides/149128
        '''

        # The code block below obtains the Person instance corresponding with from_person_id,
        # and obtains their friend list.
        from_person_obj = self.people[from_person_id]
        friendlist_from_person_ID = from_person_obj.friends


        # The code block below checks whether the DOB of each friend in their friend list
        # is within a week of the comparison date (task 6) or within range_of_days of the
        # comparison date (task 7). If it is, then the friend's ID is appended to a list
        # called friendlist_within_a_week.
        friendlist_within_a_week = []
        for i in range(len(friendlist_from_person_ID)):
            friend_obj = self.people[friendlist_from_person_ID[i]]
            if friend_obj.birthday_within_X_days_of_Y(range_of_days, comparison_date):
                friendlist_within_a_week.append(friendlist_from_person_ID[i])


        # The code block below makes a list of birthday strings for people in friendlist_within_a_week
        # then store the wishes in a list called list_of_bday_strings.
        list_of_bday_strings = []
        for i in range(len(friendlist_within_a_week)):
            list_of_bday_strings.append(f"Happy birthday {self.people[friendlist_within_a_week[i]].name}! Hope you have a good one!")


        # The code block below appends the posts to self.posts using a for loop which
        # iterates through our friendlist_within_a_week and using .make_post() on our
        # person object with each bday string in the list_of_bday_string and list of ID
        # (1 specific ID for each iteration) of the person we want to make a post to.
        for i in range(len(friendlist_within_a_week)):
            post = from_person_obj.make_post(list_of_bday_strings[i], [friendlist_within_a_week[i]])
            self.posts.append(post)


    def __str__(self):
        '''
        Represents the instance of the SocialNetwork class with a string.
        '''

        # The code block below concatenates each Person instance in self.people to
        # string_representation, then prints them out in a new line.
        # This is done by looping through self.people and concatenating each instance
        # of the Person in each iteration.
        string_representation = ""
        for i in self.people:
            string_representation += str(self.people[i]) + "\n"

        return string_representation





# TASK 7 FUNCTIONS (task7_sorted_bday_messages() is to be called in the if __name__ == "__main__": section)

def remove_duplicates(duplicate_list):
    '''
    Removes duplicate elements from a list

    Args:
      duplicate_list (list): A list which may or may not contain duplicates.

    Returns:
      list: List without duplicate elements

    Notes:
      I will use this function to solve task 7.
    '''

    # The code block below iterates through every element in the duplicate_list
    # and appends the element to the new_list (no duplicates) if it is not in the new_list.
    new_list = []
    for element in duplicate_list:
        if element not in new_list:
            new_list.append(element)
    return new_list


def task7_sorted_bday_messages():
    '''
    Function to be called in if __name__ == "__main__": section to complete Task 7

    Args:
      No arguments.

    Returns:
      No return value.

   Notes:
      Description, args and returns for this function are obtained from this
      slide : https://edstem.org/au/courses/7542/lessons/20930/slides/149114
    '''


    # The code block below creates a SocialNetwork instance called ExampleSocialNetwork
    # with the friendship_data below
    friendship_data = ['Fred,2022-02-01<->Jenny,2004-11-18',
                        'Jiang,1942-09-16<->Sasha,1234-02-02',
                        'Corey,2015-05-22',
                        'Sasha,1834-02-02<->Amir,1981-08-11']

    ExampleSocialNetwork = SocialNetwork(friendship_data, 1)


    # This block of code will aim to create a list of dates (datetime.date) in the current year (2022).
    # First, I get the start date and end date of 2022, and create a fixed one_day_delta.
    start_date = datetime.date(2022, 1, 1)
    end_date = datetime.date(2022, 12, 31)
    one_day_delta = datetime.timedelta(days=1)

    # Then, I iterate through the start date till the end date and append the start_date to
    # the list_of_dates_in_2022. In the end, I will get the entire list of datetime.date objects for
    # the year 2022 stored in list_of_dates_in_2022.
    list_of_dates_in_2022 = []
    while start_date <= end_date:
        list_of_dates_in_2022.append(start_date)
        start_date += one_day_delta


    # This code block makes each Person in the network check for and make (as appropriate) birthday posts
    # for each of their friends with a birthday falling on that exact day.
    # It works by iterating through the IDs in our SocialNetwork instance to obtain the wisher's
    # ID (from_person_id), then it iterates through the friend list of the wisher to get the day and month
    # of the friend's (to-be-wished) DOB, then it iterates through every single day of the year in the
    # list_of_dates_in_2022 and checks if the friend's DOB month and day is equal to the date month and date
    # day in each iteration. If it is, then we add the date to the bday_list. The bday_list is then sorted in
    # ascending order using sorted().
    # However, self.posts is not sorted in ascending order of birthdays at this stage (YET).
    # There will also be duplicate posts, which we will remove with our remove_duplicates() function later.
    bday_list = []
    for i in range(1, len(ExampleSocialNetwork.people) + 1):
        for j in range(len(ExampleSocialNetwork.people[i].friends)):
            friend_id = ExampleSocialNetwork.people[i].friends[j]
            DOB_of_friend = ExampleSocialNetwork.people[friend_id].date_of_birth
            DOB_day = DOB_of_friend.day
            DOB_month = DOB_of_friend.month
            for k in range(len(list_of_dates_in_2022)):
                date_day = list_of_dates_in_2022[k].day
                date_month = list_of_dates_in_2022[k].month
                if DOB_month == date_month and DOB_day == date_day:
                    bday_list.append(list_of_dates_in_2022[k])

    bday_list_sorted = sorted(bday_list)



    # The code block below aims to obtain the sorted friend ID list (based on increasing order of bdays) in order to
    # sort ExampleSocialNetwork.posts() in ascending order of birthdays.
    # I iterate through each Person in the .people attribute, then I iterate through the friend list of that person
    # to obtain each ID of the Person's friends, then i iterated through the bday_list_sorted to obtain the
    # corresponding friend ID, which I append to friend_id_list. Then, I remove duplicates by calling my
    # remove_duplicates() function.
    # Then, I created a dictionary that maps datetime objects in bday list to the ID in friend_id_list.
    # Now, since each datetime object corresponds to a friend_id, I just used another for loop to iterate through
    # the bday_list_sorted, since it is already sorted in ascending order, and append the corresponding IDs using my
    # dictionary to sorted_friend_id_list. I realised by debugging that the sorted_friend_id_list was sorted in reverse,
    # so I used the .reverse() method on it to make it in the right order.
    friend_id_list = []
    for i in range(1, len(ExampleSocialNetwork.people) + 1):
        for j in range(len(ExampleSocialNetwork.people[i].friends)):
            friend_id = ExampleSocialNetwork.people[i].friends[j]
            for k in range(len(bday_list_sorted)):
                if DOB_day == bday_list_sorted[k].day and DOB_month == bday_list_sorted[k].month:
                    friend_id_list.append(friend_id)

    friend_id_list = remove_duplicates(friend_id_list)

    from_datetime_obj_to_from_person_ID_dict = {key: value for key, value in zip(bday_list, friend_id_list)}

    sorted_friend_id_list = []
    for i in range(len(bday_list_sorted)):
        sorted_friend_id_list.append(from_datetime_obj_to_from_person_ID_dict[bday_list_sorted[i]])

    sorted_friend_id_list.reverse()



    # The code block below makes sorted birthday posts (in ascending order or birthdays in a year) by updating the
    # ExampleSocialNetwork.posts attribute and prints them out to the console.
    # I used two for loops. One for making the birthday posts by iterating through the bday_list_sorted and using
    # the make_birthday_posts function with the lists we've sorted earlier. Another for loop is used just to iterate
    # through the list ExampleSocialNetwork.posts and print each post out in the list.
    ExampleSocialNetwork.posts = []
    for m in range(len(bday_list_sorted)):
        ExampleSocialNetwork.make_birthday_posts(sorted_friend_id_list[m], bday_list_sorted[m], 0)


    # The code block below just iterates through .posts and prints each post out.
    for i in range(len(ExampleSocialNetwork.posts)):
        print(ExampleSocialNetwork.posts[i])




if __name__ == "__main__":
    task7_sorted_bday_messages()






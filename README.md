# Room-roomies
Trying to find where and how to live as a student in Madrid is a mess. There are dozens of platforms to search but none of them adapt their offer to your expectations. Pictures and descriptions in those apps usually do not match with the reality you are searching for. Moreover, if you have an idea of what you want but your knowledge about Madrid is limited, it's very difficult to have a clue about where to start searching. In the case of finding roommates, it's even harder. Most of the time, the only possibility that you have is to offer your intentions of having a roommate through social media, with all the risks and inconveniences that this solution has attached. Our product will transform all this complex process into a very simplified and personalized experience.
There are 2 files: main and functions_one. In the main, the databases are implemented as hash tables and it is where the program runs. But many of the tasks are runned through function defined in the 2nd file.
*The main*
The program is implemented with a while loop so it runs indefinetely until it encounters a break. If there is not a username defined, it gives us the option to log in or sign up. Whatever you choose, it will call a function with that same name that performs the action. After being logged in, we have an interface that gives us 5 options:
-Change the user (log in or sign up with another user) -> set user_name to 0 so the program has to ask to log in again
-Assign the importance of each category of questions to ask some questions or others -> calls the categories function as well as the questions one to avoid the user forgetting
-Score the importance of certain questions and afirmaciones -> calls the questions function
-See your matches -> calls the matches function
-Log out -> breaks the loop

*Functions_one.py*
Contains all the functions called from the main, and from within the file.
The signup function asks for a new username and makes sure it doesn't already exist. If it does, it asks you if what you really want is to log in, calling a function or the other depending on your response. If it doesn't exist, it defines it in the hash tables.
The log in function works in the same way.
The categories function presents the different categories of questions and asks you to distribute 10 points between the different categories. If you distribute more than 10 points it asks you to do it again, if you distribute less you also have to repeat it again, if you only press "enter" it assigns a 0.
The questions function asks only the questions of the categories with an assigned value higher than 0, and only allows values between 0 and 10 included. At the end of each section it multiplies the mean of the answers of each category by the weight assigned.
The matches function calculates the distances of the user's answers with rest answers of the rest of users in the dataset, calculated the affinity and prints it in a sorted order using a quicksort algorithm.

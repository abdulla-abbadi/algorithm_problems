import random
"""
Input:
A pool of applicants:
    applicants = [(username, number_of_tickets), (username, number_of_tickets), (username, number_of_tickets)]
Available tickets: 
    available_tickets = integer 

Output:
list of randomly picked applicants until we reach the available_tickets capacity
[(username, number_of_tickets),(username, number_of_tickets), ...]
"""

def lottery(applicants:list, available_seats:int):
    winner_applicants = []
    while available_seats and applicants:
        random_index = random.choice(range(0, len(applicants)))
        remaining_tickets = (available_seats - applicants[random_index]["number_of_tickets"])
        if (remaining_tickets < 0):
            applicant = applicants.pop(random_index)
            applicant["number_of_tickets"] = available_seats
            winner_applicants.append(applicant)
            break
        else:
            applicant = applicants.pop(random_index)
            available_seats -= applicant["number_of_tickets"]
            winner_applicants.append(applicant)
    return winner_applicants

applicants_list = [
                    {"name":'Ali', "number_of_tickets": 2},
                    {"name":'Ali', "number_of_tickets": 1},
                    {"name":'Ali', "number_of_tickets": 2},
                    {"name":'Ali', "number_of_tickets": 1}
                ]
available_seats = 9
print(lottery(applicants=applicants_list, available_seats=available_seats))
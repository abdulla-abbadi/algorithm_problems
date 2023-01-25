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
        remaining_tickets = (available_seats - applicants[random_index][1])
        if (remaining_tickets < 0):
            applicant = applicants.pop(random_index)
            applicant[1] = available_seats
            winner_applicants.append(applicant)
            break
        else:
            applicant = applicants.pop(random_index)
            available_seats -= applicant[1]
            winner_applicants.append(applicant)
    return winner_applicants

applicants_pool = [['Ali', 2],['Tom', 1],['Fran', 1],['Hyat', 2]]
available_seats = 9
print(lottery(applicants=applicants_pool, available_seats=available_seats))
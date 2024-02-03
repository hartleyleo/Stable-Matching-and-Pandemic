import sys

#globals:
#two dictionaries 
resident_preferences = dict()
hospital_preferences = dict()


def print_output():
    pass


'''
    Here is the algorithm:
• Every hospital ranks the resident candidates in order of preference.
• Similarly, every resident candidate ranks the hospital in order of preference.
• Each resident applies to the hospital it prefers most.
• Then, each hospital considers all the applicants they have received, and
replies “maybe” to the resident they like best (of the ones that applied to that hospital) and “no” to all the rest. Thus, the resident is now tentatively matched to that hospital.
• As long as there are unmatched residents, each unmatched resident applies to the most-preferred hospital to which they have not yet applied, regardless of whether or not that hospital is tentatively matched.
• Each hopsital reviews the new offers, and either:
– replies “maybe” if it is not yet tentatively matched or if it prefer
this resident to the one it was previously matched to (if it rejects its previously-matched resident, that resident becomes unmatched)
1
– or replies “no” if it is tentatively matched and it prefers the existing match to the new applicant


def StableMatching(S, R)
  let M = {}
  for s \in S:
    set s to free
  for r \in R:
    set r to free
  while some student s \in S is free and has not proposed to every residency:
    let r = first residency in s's list to which they have not proposed
    if r is free:
      add (s,r) to M
    else if r prefers s to its current student s'
      remove (s',r) from M
      add (s,r) to M

'''
def stable_matching(resident_preferences, hospital_preferences):
    #let M be the empty set of matches
    matching_dict = dict()

    #for hospital in hospitals:
        #set each hospitals' match to free (still needs a match)
    hos_proposals = {hos: None for hos in hospital_preferences}
    
    #for each resident in residents:
        #set each residents' match to free (still need a match)
    res_proposals = {res: None for res in resident_preferences}
    
    #while some resident in the list of Residents is not free and has not proposed to every hospital:
    while None in res_proposals.values():
        pass
        #let current_hospital = the first residency in the residents' list which they haven't proposed

        #if current_hospital is free:
            #add the pair (resident, current_hospital) to M
        #else if current_hospital prefers the new resident to its current resident
            #remove the current pair(resident', current_hospital)
            #add (resident, current_hospital)
    pass 




def getMatchLen():
    try:
        with open(sys.argv[1], 'r') as file_input:
            size = int(file_input.readline())
        return size
    except FileNotFoundError:
        sys.exit(1)
    except IOError:
        sys.exit(1)



#TODO: Get rid of new line characters
def parser(resident_preferences, hospital_prefences, size):
    #open the file
    try:
        with open(sys.argv[1], 'r') as file_input:
            file_input.readline()
            for i in range(size):
                line = file_input.readline()
                entry = line.split(" ")
                resident_preferences[entry[0]] = list(entry[1:])
         
            for i in range(size):
                line = file_input.readline()
                entry = line.split(" ")
                hospital_prefences[entry[0]] = list(entry[0:])


    except FileNotFoundError:
        sys.exit(1)
    except IOError:
        sys.exit(1)



def main():
    if len(sys.argv) != 2:
        sys.exit(1)

    try:
        parser(resident_preferences, hospital_preferences, getMatchLen())
    except IOError:
        sys.exit(1)

    #stable_matching(resident_preferences, hospital_preferences)

    #print_output()

if __name__ == "__main__":
    main()


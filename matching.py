import sys

#globals:
resident_preferences = []
hospital_preferences = []

def getArrLen():
    try:
        with open(sys.argv[1], 'r') as file_input:
            size = int(file_input.readline())
        return size
    except FileNotFoundError:
        sys.exit(1)
    except IOError:
        sys.exit(1)



#TODO: Get rid of new line characters
def parser(resident_preferences, hospital_prefences):
    #open the file
    try:
        with open(sys.argv[1], 'r') as file_input:
            file_input.readline()
            for i in range(len(resident_preferences)):
                line = file_input.readline()
                entry = line.split(" ")
                resident_preferences[i] = list(entry[0:])
                #print(resident_preferences[i])
            
            for i in range(len(hospital_prefences)):
                line = file_input.readline()
                entry = line.split(" ")
                resident_preferences[i] = list(entry[0:])
                #print(resident_preferences[i])
    except FileNotFoundError:
        sys.exit(1)
    except IOError:
        sys.exit(1)



def main():
    if len(sys.argv) != 2:
        sys.exit(1)

    size = getArrLen()
    resident_preferences = [[0] * (size + 1)] * (size) #res 2-D array
    hospital_preferences = [[0] * (size + 1)] * (size) #hos 2-D array

    parser(resident_preferences, hospital_preferences)

if __name__ == "__main__":
    main()


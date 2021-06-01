"""Generate sales report showing total melons each salesperson sold."""


salespeople = []
melons_sold = []

f = open('sales-report.txt')            #open file with salesperson data
for line in f:
    line = line.rstrip()
    entries = line.split('|')           #separate each line wherever there's a |

    salesperson = entries[0]            #the first item of each line is the salesperson
    melons = int(entries[2])            #the number of melons sold is the 3rd item of each line

    if salesperson in salespeople:      #if the salesperson is in the list of salespeople
        position = salespeople.index(salesperson)
                                        #define a variable called position, gets the index of that salesperson in the list of salespeople
        melons_sold[position] += melons #adds however many melons to the melons_sold list at the position index
    else:
        salespeople.append(salesperson) #otherwise, add the salesperson to the list of salespeaple
        melons_sold.append(melons)      #add the number of melons sold to the end of the melons_sold list


for i in range(len(salespeople)):      #for each number until the length of the salespeople list
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
                                        #print statement
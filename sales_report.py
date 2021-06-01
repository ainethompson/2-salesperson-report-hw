"""Generate sales report showing total melons each salesperson sold."""


salespeople = []
melons_sold = []

f = open('sales-report.txt')            #loop over each line in file object
for line in f:
    line = line.rstrip()                #remove trailing whitespace
    entries = line.split('|')           #create list of data

    salesperson = entries[0]            #get name of salesperson
    melons = int(entries[2])            #get number of melons they've sold

# If the salesperson is already in `salespeople`, increment the no. of
# melons they've sold.

#otherwise, add the salesperson to the list of salespeaple
#add the number of melons sold to the melons_sold list

    if salesperson in salespeople:      
        position = salespeople.index(salesperson)
                                       # find the position where the salesperson is stored in the list of salespeople
        melons_sold[position] += melons 
    else:                               # use that position to index into melons_sold
        salespeople.append(salesperson) 
        melons_sold.append(melons)     


for i in range(len(salespeople)):      # Loop over indices of `salespeople` and use it to index into `salespeople` and `melons_sold`.
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
                                        #print the data
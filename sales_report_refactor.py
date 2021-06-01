
def get_melons_sold_by_salesperson(filename):

    sales = {}
    with open(filename) as f:
        for line in f:
            line = line.rstrip()
            
            salesperson, total_dollars, melons_sold = line.split('|')

            if salesperson in sales:
                sales[salesperson] += int(melons_sold)
            else:
                sales[salesperson] = int(melons_sold)

        return sales


def print_sales_report(sales):
    for salesperson, melons_sold in sales.items():
        print(f'{salesperson} sold {melons_sold} melons')


print_sales_report(get_melons_sold_by_salesperson("sales-report.txt"))
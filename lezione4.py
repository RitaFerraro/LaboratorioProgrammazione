class CSVFile:
    def __init__(self, name):
        self.name = name
    def get_data(self):
        data = []
        my_file = open(self.name, 'r')
        for line in my_file:
            elements = line.split(',')
            if elements[0] != 'Date':
                elements[1] = elements[1][0:-1]
                data.append(elements)
        my_file.close()
        if len(data)==0:
            return None
        return data
Shampoo = CSVFile('shampoo_sales.csv')
print(Shampoo.name)
Shampoo_values = Shampoo.get_data()
print (Shampoo_values)

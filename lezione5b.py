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
class NumericalCSVFile(CSVFile):
    def get_data(self):
        data = super().get_data()
        numerical_data=[]
        for item in data:
            try:
                item[1]=float(item[1])
                numerical_data.append(item)
            except ValueError:
               print('Errore. Non posso convertire "item[1]" a valore numerico')
               print('Ho avuto un errore di VALORE. "item[1]" valeva "{}"'.     format((item[1])))
            except TypeError:
                print('Errore. Non posso convertire "item[1]" a valore numerico')
                print('Ho avuto un errore di TIPO. "item[1]" valeva "{}"'. format(type(item[1])))
            except Exception as e:
                print('Errore. Non posso convertire "item[1]" a valore numerico')
                print('Ho avuto un errore generico. "{}"'. format(e))
        return numerical_data


#Shampoo = NumericalCSVFile('shampoo_sales.csv')
#Shampoo_data=Shampoo.get_data()
#print(Shampoo_data)
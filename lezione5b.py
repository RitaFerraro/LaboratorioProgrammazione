class CSVFile: 
    def __init__(self, name):
            self.name = name
    def get_data(self):
        data = []
        try:
            my_file = open(self.name, 'r')
            for line in my_file:
                elements = line.split(',')
                if elements[0] != 'Date':
                    elements[1] = elements[1][0:-1]
                    data.append(elements)
            my_file.close()
            return data
        except Exception:
            print('Errore. Non posso  istanziare il mio oggetto visto che il file "{}" non esiste.'.format(self.name))  
class NumericalCSVFile(CSVFile):
    def get_data(self):
        data = super().get_data()
        numerical_data=[]
        if data != None:
            try:
                for  item in data:
                    for i in range(1, len(item)): 
                        try:
                            item[i]=float(item[i])
                            numerical_data.append(item)
                        except ValueError:
                            print("Errore. Non posso convertire '{}'' a valore numerico.".format((item[1])))
                            print('Ho avuto un errore di VALORE. "item[1]" valeva "{}"'.     format((item[1])))
                        except TypeError:
                            print('Errore. Non posso convertire "item[1]" a valore numerico')
                            print('Ho avuto un errore di TIPO. "item[1]" valeva "{}"'. format(type(item[1])))
                        except Exception as e:
                            print('Errore. Non posso convertire "item[1]" a valore numerico')
                            print('Ho avuto un errore generico. "{}"'. format(e))
            except Exception:
                print('Errore. Il file da cui voglio estrarre i dati numerici on esiste')
        return numerical_data


#Shampoo = NumericalCSVFile('shampoo_sales.csv')
#Shampoo_data=Shampoo.get_data()
#print(Shampoo_data)
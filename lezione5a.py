class CSVFile: 
    def __init__(self, name):
            self.name = name
    def get_data(self):
        try:
            data = []
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
    
Video = CSVFile('video_sales.csv')        
Video_values = Video.get_data()

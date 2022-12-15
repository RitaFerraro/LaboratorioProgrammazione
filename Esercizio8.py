class Model():

    def fit(self, data):
        raise NotImplementedError('Metodo non implementato')

    def predict(self, data):
        raise NotImplementedError('Metodo non implementato')


class IncrementModel(Model): 

    def predict(self, data):
        if type(data)!=list:
            raise Exception('Errore nel tipo"{}"'.format(data))
    
        i=0
        for item in data:
            try:
                actual_value=float(item) 
            except Exception as e:
                print("il formato dell'elemento {'item'} della lista non `e valido".format(item))
                return None
            i=i+1

        prediction= (i*actual_value-data[0])/(i-1)
        return prediction

#Modello=IncrementModel(Model)
#dati=[50,52,60]
#predict(self,dati)
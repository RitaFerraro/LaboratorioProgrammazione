
#===================================================================
#Esercizio Lezione 6
#===================================================================

#Modifico l'oggetto CSV file se il nome del file non e' una stringa
class CSVFile: 
    def __init__(self, name):
        
        #se name e' una stringa setto il nome del file altrimenti alzo un'eccezione
        if type(name) is str:
            self.name = name

            #Inizializzo a vera una variabile nella classe per dire che il file e' leggibile, provo a leggere una riga
            self.can_read = True
            try:
                my_file = open(self.name, 'r')
                my_file.readline()
            #Se non riesco a leggere una riga metto falsa la variabile e stampo un messaggio di errore                
            except Exception as e:
                self.can_read = False
                print('Errore in apertura del file: "{}"'.format(e))
                
        else:
            raise Exception('Ho avuto un errore. Il nome del file "{}" non e una stringa'.format(name) )
    
    #Modifico la funzione get_data in modo da leggere solo un intervallo di righe, per questo aggiungo gli argomenti start e end in modo opzionale, cioe' non devo essere obbligato ad inserirli, per   questo li inizializzo a None    
    
    def get_data(self, start=None, end=None):
         # se non riuscivo a leggere il file esco
        
        if not self.can_read:
            print('Errore, il file e illeggibile')
            return None
        
        if start is not None and type(start)!=int:
            raise Exception('parametro start non valido')
        
        if end is not None and type(end)!=int:
            raise Exception('parametro end non valido')

                
        if start is not None and start<=0:
            raise Exception('Il parametro start "{}" non e` un indice accettabile '.format(start))
        
        if end is None:
            
            if start is None:
                start=1
    
            
            data=[]
            my_file = open(self.name, 'r')  
            i=1
            for line in my_file: 
                if i>=start:
                    if i==1:
                        elements=[]
                    else:
                        elements = line.split(',')
                        elements[-1]=elements[-1].strip()
                        data.append(elements)
                i=i+1
            my_file.close
            if i<=start: 
                raise Exception('Errore. Il parametro "{}" inserito come start non e` accettabile in quanto inizia dopo la fine del file'.format(start))
            return data
        
        else:
            if start is None:
                start=1
            if start>end:
                raise Exception('Errore. Il parametro "{}" inserito come start risulta maggiore del parametro "{}" inserito come end'.format(start, end))
            
            
            data=[]
            my_file = open(self.name, 'r')
            i=1   
            for line in my_file:
                if i>= start and i<=end: 
                    if i==1:
                        elements=[]
                    else:
                        elements = line.split(',')
                        elements[-1]=elements[-1].strip()
                        data.append(elements)
                i=i+1
            my_file.close
            if i<=start: 
                raise Exception('Il parametro "{}" inserito come start inizia dopo la fine del file'.format(start))
            if i>start and i<=end: 
                raise Exception('Errore nel parametro  end  "{}", va oltre la fine del file.'.format(end))
            return data

#===============================================================================================================# Le mie prove
#===============================================================================================================       
#Shampoo=CSVFile('shampoo_sales.csv')        
#Shampoo_data=Shampoo.get_data(1,40)
#print (len(Shampoo_data))
#print(Shampoo_data)
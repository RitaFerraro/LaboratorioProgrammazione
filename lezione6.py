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
        
        start_type=type(start)
        end_type=type(end)

        # se non riuscivo a leggere il file esco
        if not self.can_read:
            print('Errore, il file e illeggibile')
            return None

        # se l'argomento start viene indicato ma non e' un intero esco:
        if start is not None and start_type != int:
            raise Exception('Errore. Errore dato dal parametro "{}"'.format(start))
        
        # se l'argomento end viene indicato ma non e' un intero esco:
        if end is not None and end_type != int:
            raise Exception('Errore. Errore dato dal parametro "{}"'.format(end))

        #se l'argomento start e' un intero ma minore di 1, esco:
        if start_type == int and start <1:
            raise Exception('Errore. Errore dato dal parametro"{}"'.format(start))
            
        # se l'argomento end e' un intero ma minore di 1, esco
        if end_type == int and end <1:
            raise Exception('Errore. Errore dato dal parametro"{}"'.format (end))

        #==================================================================
        # se start e end non vengono indicati mi tengo la vecchia get_data
        #==================================================================
        if  start is None and end is None : 
            data = []
            my_file = open(self.name, 'r')
            for line in my_file:
                if not line:
                    print('il file ')
                    break
                elements = line.split(',')
                elements[-1]=elements[-1].strip()
                if elements[0]!= 'Date':
                    data.append(elements)
    
            my_file.close
        #======================================================================================
        # se viene indicato almeno uno tra start e end e sono numeri comincio ad analizzare i                casi:
        #======================================================================================
        else:
            data = []
            my_file = open(self.name, 'r')
            file_lines=[] 
            for line in my_file:
                try:
                    line=my_file.readline()
                    file_lines.append(line)
                except:
                     print('riga illeggibile')
            
            #cerco di sapere quanto e' lungo il file
            lunghezza= len(file_lines)
            my_file.close
            
            #=================================================
            # Ci sono sia start che end
            #=====================================================
            if start_type == int and end_type == int and end-start>=1:
                
                #se start o end vanno oltre il numero di righe del file esco:
                if start>=lunghezza or end>lunghezza:
                    
                    raise Exception('intervallo di righe da leggere non e compatibile con il numero di righe del file')
                else:
                    
                    for i in range(start, end+1):
                        try:
                            
                            #my_file.readline()
                            line=file_lines[i]
                            #print(line)
                        except Exception as e:
                            self.can_read = False
                        
                        if not self.can_read:
                            raise Exception('Riga non leggibile')
                        else:
                            #if line!="":
                            elements = line.split(',')
                            elements[-1]=elements[-1].strip()
                            data.append(elements)
                            #else:
                                #break
                    
                    
         #====================================
            #c'e' o solo end o solo start  
        #=========================================
            else:
                if start is None and end_type == int:
                    #print('Ecco end "{}"'.format(end))
                    # non voglio che end sia maggiore del numero di righe del file
                    if end> lunghezza:
                        
                        raise Exception('Errore. Mi chiedi di leggere oltre la lunghezza del file')
                    else:
                        
                        for i in range(1, end+1):
                            
                            
                            line=file_lines[i]
                            #if line!= "":
                            elements = line.split(',')
                            elements[-1]=elements[-1].strip()
                            data.append(elements)
                            #else:
                            #    my_file.close()
                            #    break
                        
                
                if start_type == int and end is None: 

                    # non voglio che start sia maggiore o uguale al numero di righe del file
                    if start>=lunghezza:
                        raise Exception('Errore.Start inizia dopo la fine del file')
                    
                    else:
                       
                        i=start
                        while i>= start and i<lunghezza:
                            
                            try:
                                line=file_lines[i]
            
                            except  Exception:
                                self.can_read=False
                            
                            if not self.can_read:
                                raise Exception('Riga illeggibile')
                            else:
                                #if line!="":
                                elements = line.split(',')
                                elements[-1]=elements[-1].strip()
                                data.append(elements)
                            i=i+1
                                #else:
                                # 
                                #    break
                        
                
                #se l'argomento end e' minore di start esco:
                if start_type == int and end_type == int and end-start <= 0:
                    raise Exception('Errore')
                    
            return data

#==========================================================================================
#PROVE
#============================================================================================
Shampoo=CSVFile('prova_vuota.csv')        
Shampoo_data=Shampoo.get_data()
print(Shampoo_data)
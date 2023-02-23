#==================================================================================================
    #L'ECCEZIONE:
#==================================================================================================

class ExamException(Exception):
    pass

#==================================================================================================
    #LA CLASSE:
#==================================================================================================

class CSVTimeSeriesFile:
    def __init__(self, name):
        self.name = name
    def get_data(self):
        data = []
#==================================================================================================
# Provo ad aprire il mio file. Se il file non esiste o illeggibile Python dovrebbe segnalare errore e bloccarsi ma nella consegna c'e' scritto che devo alzare un'eccezione, ma cosi' ne vengono alzate due, una da python e una da me. Non so se ho fatto bene.
        try:
            my_file = open(self.name, 'r')
            for line in my_file:
                elements = line.split(',')
                if elements[0] != 'date':
#==================================================================================================
# Nella consegna c'e' scritto che il numero dei passeggeri deve considerarsi un intero positivo e se non lo e' non bisogna  accettarlo. Solo che il valore me lo passa come stringa, allora provo a convertirlo in intero e se non ci riesce segnalo errore. Poi lo accetto e lo appendo alla mia lista solo se e' un intero positivo.

                    try:
                        elements[1] = int(elements[1][0:-1]) 
                    except(Exception):
                        print('Non posso  convertire  il valore  passeggeri  a numero intero. Ignoro                         tale dato "{}"'.format(elements[1]))   
                    if type(elements[1])==int and elements[1]>0:
                            data.append(elements)
                    elif elements[1][0:-1]=='':
                            print('Uno dei valori che non sono riuscita a convertire ad intero era mancante, lo sostituisco con il valore None. ')
                            elements[1]=None
                            data.append(elements)
        except:
            raise ExamException('Errore: file non esistente o illeggibile')
        my_file.close()
#==================================================================================================
# Cerco se c'e' un timestamp duplicato e in caso affermativo alzo un eccezione
        insieme_date ={elements[0] for elements  in data}
        if len(insieme_date) !=len(data):
            raise ExamException('Errore: almeno un timestamp duplicato')
#==================================================================================================
# Cerco se c'e' un timestamp fuori ordine e in caso affermativo alzo un eccezione. Per far cio' tolgo il - che separa il mese dall'anno e convergo da stringa ad intero
        lista_timestamp=[int(elements[0].replace("-","")) for elements in data]
        l=len(lista_timestamp)
        for i in range(1,l):
            if lista_timestamp[i]<lista_timestamp[i-1]:
                raise ExamException('Errore: almeno un timestamp fuori ordine')
#==================================================================================================
        if len(data)==0:
            return None
        return data
#==================================================================================================
    


#==================================================================================================
# FUNZIONE AUSILIARIA: Definisco una funzione ausiliaria che ha come input la mia time_series e un anno e restituisce una lista con i 12 valori del numero di passeggeri per ogni mese di quell'anno (i valori mancanti sono stati sostituiti da None nella get_data)
#==================================================================================================
def passenger_year(time_series, year):
    passengers =[]
    for elements in time_series:
        if year in elements[0] and elements[1] is not None:
            passengers.append(elements[1])
        elif year in elements[0] and elements[1] is None:
             passengers.append(None)
    return passengers

    
#==================================================================================================
# FUNZIONE AUSILIARIA: Definisco una funzione ausiliaria che ha come input la mia time_series e un anno e restituisce una lista con gli 11 valori delle differenze tra il valore del numero di passeggeri di un mese e quello del mese precedente.Una differenza che contiene None diventa None.
#==================================================================================================
def diff_passenger_year(time_series, year):
    passengers = passenger_year(time_series, year)
    diff = []
    for i in range(0,11):
        if passengers[i+1] is not None and passengers[i] is not None:
            diff.append(passengers[i+1]-passengers[i])
        else:
            diff.append(None)
    return diff

    
#==================================================================================================
# FUNZIONE PRINCIPALE: prende in input time_series e una coppia di anni consecutivi e restituisce una lista di 11 elementi True oppure False a seconda se la variazione tra ciascuna coppia di mesi(consecutivi) per i due anni  e' simile oppure no.
#==================================================================================================
def detect_similar_monthly_variations(time_series, years):
    dates=[elements[0][0:4] for elements in time_series]
    if years[0] not in dates or years[1] not in dates:
        raise ExamException("Errore: almeno uno degli  anni inseriti non e' presente.")
    if abs(int(years[1])-int(years[0]))!=1:
        print("Errore in input: gli anni inseriti non sono consecutivi")
    simil_variations=[]
    diff0 = diff_passenger_year(time_series, years[0])
    diff1 = diff_passenger_year(time_series, years[1])
    for i in range(0,11):
        if diff0[i] is not None and diff1[i] is not None and abs(diff1[i]- diff0[i])<=2:
            simil_variations.append(True)
        else:
            simil_variations.append(False)
    return simil_variations

    #==================================================================================================
# FINE. Del suggerimento "se riuscite a leggere due valori (data e temperatura(immagino passeggeri)) ma c'e' un campo di troppo sulla stessa riga questo non e' da considerarsi un'errore e non bisogna ignorare quella riga" non sono riuscita a tenerne conto.   
#==================================================================================================                
#time_series_file =CSVTimeSeriesFile(name = 'data.csv')
#time_series = time_series_file.get_data()


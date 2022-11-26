#Esercizio Lezione 3: scrivere una funzione che sommi tutti i valori degli shampo del file passato come argomento

def sum_csv(file_name):
# Inizializzo una lista vuota per salvare i valori
    values = []
    # apro e leggo il file linea per linea 
    my_file = open(file_name, 'r')
    for line in my_file:
        #faccio lo split di ogni linea sulla virgola
        elements = line.split(',')
        #se il primo elemento non e' la parola Date
        if (elements[0]!='Date'):
            #aggiorno la data e il valore
            value = elements[1]
            date = elements[0]
            #e aggiungo alla mia lista dei soli valori quest'ultimo valore
            values.append(float(value))
    my_file.close()
    if len(values)==0:
        return None
    else:
        sum=0
        for item in values:
            sum=item+sum
        return sum
#provo la mia funzione sul file shampo_sales.csv
print(sum_csv("shampoo_sales.csv"))

import csv
def carica_da_file(file_path):
    """Carica i libri dal file"""
    # TODO
    try:
        infile=open(str(file_path),"r")
    except FileNotFoundError:
        print("File not found")
        return None
    dizionario={}
    infile.seek(0)
    riga=infile.readline()
    for riga in infile:
        riga=riga.strip('\n')
        riga=riga.split(',')
        if riga[4] not in dizionario:
            dizionario[riga[4]]=[]
        dizionario[riga[4]].append(riga)
    print("BIBLIOTECA CARICATA CON SUCCESSO")
    infile.close()
    return dizionario




def aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path):
    """Aggiunge un libro nella biblioteca"""
    # TODO
    try:
        file=open(str(file_path),"a",newline="")
        outfile=csv.writer(file)
    except FileNotFoundError:
        return None

    presente=False
    if str(sezione) in biblioteca.keys():
        for sezioni in biblioteca.keys():
            for i in range (len(biblioteca[sezioni])):
                if titolo in biblioteca[sezioni][i]:
                    presente=True
                    return None
        nuovo_libro=(str(titolo)+","+str(autore)+","+str(anno)+","+str(pagine)+","+str(sezione))
        nuovo_libro=nuovo_libro.strip('\n')
        nuovo_libro=nuovo_libro.split(",")
        biblioteca[str(sezione)].append(nuovo_libro)
        print(f'libro aggiunto {nuovo_libro}')
        outfile.writerow(nuovo_libro)
        file.close()
        return True

    else:
        return None





def cerca_libro(biblioteca, titolo):
    """Cerca un libro nella biblioteca dato il titolo"""
    # TODO
    presente=False
    for sezione in biblioteca.keys():
        for i in range (len(biblioteca[sezione])):
            if titolo in biblioteca[str(sezione)][i]:
                presente=True
                return ", ".join(biblioteca[sezione][i])
    if presente==False:
        return None



def elenco_libri_sezione_per_titolo(biblioteca, sezione):
    """Ordina i titoli di una data sezione della biblioteca in ordine alfabetico"""
    # TODO
    elenco_libri=[]
    if str(sezione) in biblioteca.keys():
        for sezioni in str(biblioteca.keys()):
            if str(sezione)==sezioni:
                for i in range (len(biblioteca[str(sezione)])):
                    elenco_libri.append(biblioteca[str(sezione)][i][0])

        elenco_libri=sorted(elenco_libri)
        return elenco_libri


    else:
        return None


def main():
    biblioteca = []
    file_path = "biblioteca.csv"

    while True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Carica biblioteca da file")
        print("2. Aggiungi un nuovo libro")
        print("3. Cerca un libro per titolo")
        print("4. Ordina titoli di una sezione")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                biblioteca = carica_da_file(file_path)
                if biblioteca is not None:
                    break

        elif scelta == "2":
            if not biblioteca:
                print("Prima carica la biblioteca da file.")
                continue

            titolo = input("Titolo del libro: ").strip()
            autore = input("Autore: ").strip()
            try:
                anno = int(input("Anno di pubblicazione: ").strip())
                pagine = int(input("Numero di pagine: ").strip())
                sezione = int(input("Sezione: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per anno, pagine e sezione.")
                continue

            libro = aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path)
            if libro:
                print(f"Libro aggiunto con successo!")
            else:
                print("Non è stato possibile aggiungere il libro.")

        elif scelta == "3":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            titolo = input("Inserisci il titolo del libro da cercare: ").strip()
            risultato = cerca_libro(biblioteca, titolo)
            if risultato:
                print(f"Libro trovato: {risultato}")
            else:
                print("Libro non trovato.")

        elif scelta == "4":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            try:
                sezione = int(input("Inserisci numero della sezione da ordinare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_libri_sezione_per_titolo(biblioteca, sezione)
            if titoli is not None:
                print(f'\nSezione {sezione} ordinata:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()


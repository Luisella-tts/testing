import pandas as pd

# Parametri base
costi_fissi = 6000             # €/mese
costo_variabile_per_cliente = 150
prezzo_per_cliente = 500
clienti_scenari = [5, 10, 15, 18, 20, 25, 30, 40, 50]

# Calcolo
dati = []
for clienti in clienti_scenari:
    ricavi = clienti * prezzo_per_cliente
    costi_variabili = clienti * costo_variabile_per_cliente
    totale_costi = costi_fissi + costi_variabili
    utile = ricavi - totale_costi
    dati.append([clienti, ricavi, totale_costi, utile])

# Creiamo tabella
df = pd.DataFrame(dati, columns=["Clienti", "Ricavi (€)", "Costi totali (€)", "Utile (€)"])

print(df)

# Salva in Excel per analisi
df.to_excel("piano_startup.xlsx", index=False)

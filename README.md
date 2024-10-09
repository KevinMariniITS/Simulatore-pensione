# Simulatore-pensione
 L'obiettivo di questo notebook è cercare di estimare quale sarà la rendita contributiva mensile di un futuro pensionato, il metodo di calcolo terrà conto del pieno calcolo contributivo, ovvero di tutta la forza lavoro che avvierà la propria carriera lavorativa in un intervallo di tempo successivo alla riforma Fornero del 2011(senza considerare il vincolo dell'anzianità contrib)

## Rapporto mef di riferimento:
https://www.rgs.mef.gov.it/_Documenti/VERSIONE-I/Attivit--i/Spesa-soci/Attivita_di_previsione_RGS/2023/Rapporto-2023.pdf

#### La pensione è calcolata usando il metodo di calcolo contributivo.
#### *PB= ct * M*
##### dove: 
#### *ct = coefficiente di trasformazione*
#### *M = montante contributivo* 


*"ossia la somma di tutti i contributi
versati durante l’intera vita lavorativa e capitalizzati ad un tasso
pari alla media mobile su 5 anni del tasso di crescita nominale del
PIL. La normativa prevede che tali coefficienti vengano rivisti ogni
3 anni (2 anni per gli adeguamenti successivi a quello avente
decorrenza 2019) conformemente alle modifiche nella speranza di
vita. Per il periodo 2023-2024 i predetti coefficienti vanno da un
minimo di 4,270% a 57 anni ad un valore di 5,723% a 67 anni
(fino ad un massimo di 6,655% a 71 anni)."*

*"L’aliquota di
contribuzione utilizzata per calcolare l’ammontare di contributi
versati annualmente è il 33% per i lavoratori dipendenti ed il 20%
per gli autonomi fino al 2011 poi gradualmente crescente al 24%
a partire dal 1° gennaio 2018 (per i lavoratori cocopro al 27% per
gli anni 2012 e 2013 poi crescente fino ad arrivare al 33% dal
2018). Tale contribuzione è calcolata sui redditi fino ad un
massimale di 113.520 euro nel 2023.*"


Presi i dati OCSE, un ventiduenne entrano nel mondo del lavoro da 4 anni (2020-2024) potrebbe aderire alla pensione ad un'età minima pari a 71 anni.
Preso atto anche di queste previsioni scarsamente incoraggianti, il modello si basa su una arbitraria compensazione di modelli premianti e punitivi, sia sulla base delle normative attualmente vigenti + alcuni criteri di scelta applicati dall'autore del codice.

https://www.oecd-ilibrary.org/docserver/678055dd-en.pdf?expires=1727993957&id=id&accname=guest&checksum=872D38C1D162FFBCE0F30907AA087510 (pag.43)

### Fattori premianti:
1) Possibilità di intraprendere una carriera lavorativa continuativa e con adeguati meccanismi di crescita salariale (scatti d'anzianità + salti di lvl ogni 5 anni); vale sia per lavoratori autonomi che lavoratori dipendenti.
2) Libertà di scelta rispetto all'età pensionabile, potendo così avere una visione maggiormente responsabilizzante rispetto ai contributi versati durante la propria carriera lavorativa; consapevoli del fatto che tale condizionalità risulterebbe insostenibile per il bilancio INPS, questa libertà può essere rimossa inserendo l'applicazione della legge Fornero all'interno del medesimo codice.
3) Applicazione della massima aliquota contributiva per i contratti di apprendistato, senza tener conto degli sgravi per aziende aventi meno di 9 dipendenti, così come per lo sgravio del 100% a carico dei datori di lavoro a 12 mesi dal passaggio da contratto di appr. al contratto a tempo indet. (fino ad un tetto max di 3000 euro con la normativa attuale).
4) Sempre con l'applicazione della Legge Fornero, possibilità di riscattare gli anni di Laurea (Triennale 3 anni + Magistrale 2 anni) + il riconoscimento del servizio civile universale, utili per abbattere gli anni necessari per l'ottenimento dell'età pensionabile.
5) Per gli autonomi l'aliquota contributiva è del 26,7%, senza tenere conto delle differenze fra le singole casse professionale nel tentativo di massimizzare la cifra versata.

### Fattori punitivi:
0) Rimozione del periodo di tirocinio dal computo della pensione (vista la normativa il periodo di stage non prevede il versamento di contributi).
1) Piena attuazione del metodo contributivo (seppur senza il vincolo di anzianità contributiva, seppur come descritto prima si può aggiungere come condizione stringente)
2) In ragione del punto 1), rimozione di opzione donna, quota 102,103 eccetera; per le donne si potrà avere una riduzione del periodo d'anzianità contributiva fino ad un massimo di 2 anni in caso di un numero di figli avuti >= a 2. Ciò sempre in caso di applicazione della legge Fornero.
3) Possibilità di vedere la pensione mensile attesa inferiore in caso di carriera lavorativa discontinua o fortemente discontinua (applicando rispettivamente una riduzione della pensione attesa di 1 dev_std e 1.75 dev_std).
4) Mancata applicazione dei meccanismi di detrazione d'imposta sulle pensioni; pur consapevoli del fatto che tale congettura possa risultare fortemente regressiva per gli assegni pensionistici più bassi.
5) Applicazione degli scaglioni IRPEF pre-riforma governo Meloni. Non trattandosi di una riforma strutturale, non si ha ancora la certezza delle sua copertura piena e sostenibile a medio-lungo termine.
6) In ragione delle previsioni OSCE, slittamento dei coeff. di trasformazione di 5 anni, oltre al fatto di aver preso come riferimento i coefficienti degli anni 2019-2020 (vedi fonti sotto)
7) I lavoratori autonomi avranno una pensione più bassa in ragione di minori contributi versati.



## Altre Fonti:
Fonte per la ricerca dei requisiti di pensionabilità: https://www.fiscoetasse.com/approfondimenti/12731-eta-e-requisiti-per-andare-in-pensione-2024.html

Fonte per l'applicazione del metodo contributivo: https://www.ipsoa.it/guide/calcolo-pensione

Aliquote irpef (pre-riforma gov.Meloni + riforma gov.Meloni): https://www.agenziaentrate.gov.it/portale/imposta-sul-reddito-delle-persone-fisiche-irpef-/aliquote-e-calcolo-dell-irpef

Normativa sui contratti di apprendistato: https://www.ipsoa.it/documents/quotidiano/2024/02/28/apprendistato-professionalizzante-incentivo-under-30-conviene-assunzioni#:~:text=Nel%202024%20i%20datori%20di,un%20rapporto%20di%20apprendistato%20professionalizzante.

Coefficienti du trasformazione delle pensioni: https://www.itinerariprevidenziali.it/site/home/ilpunto/pensioni/coefficienti-di-trasformazione-piu-favorevoli-dal-2023-pensioni-piu-generose.html

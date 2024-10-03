# Simulatore-pensione
 L'obiettivo di questo notebook è cercare di estimare quale sarà la rendita contributiva mensile di un futuro pensionato, il metodo di calcolo terrà conto del pieno calcolo contributivo, ovvero di tutta la forza lavoro che avvierà la propria carriera lavorativa in un intervallo di tempo successivo alla riforma Fornero del 2011(no anzianità contrib)

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
(fino ad un massimo di 6,655% a 71 anni).
L’aliquota di
contribuzione utilizzata per calcolare l’ammontare di contributi
versati annualmente è il 33% per i lavoratori dipendenti ed il 20%
per gli autonomi fino al 2011 poi gradualmente crescente al 24%
a partire dal 1° gennaio 2018 (per i lavoratori cocopro al 27% per
gli anni 2012 e 2013 poi crescente fino ad arrivare al 33% dal
2018). Tale contribuzione è calcolata sui redditi fino ad un
massimale di 113.520 euro nel 2023."*

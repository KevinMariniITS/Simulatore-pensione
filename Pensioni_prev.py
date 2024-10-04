import streamlit as st
import pandas as pd
import numpy as np
import random as rd
import plotly.graph_objs as go


st.title("Simulatore pensione")

st.warning("""
**⚠️ Attenzione:**

- I risultati della previsione sono soltanto a puro scopo indicativo, pertanto è FORTEMENTE SCONSIGLIATO trarre conclusioni/ intrapendere scelte sui propri futuri scenari pensionistici facendo affidamento ai dati presenti in questa app.

- La normativa tributaria è sempre oggetto di continue modifiche a seconda delle congetture che man mano si susseguono nel tempo. Per semplificare l'algoritmo del modello sottostante, alcune regole risultano incomplete o arbitrariamente modificate (leggere la nota metodologica applicata: "https://github.com/KevinMariniITS/Simulatore-pensione/tree/main" ).
- Pertanto, ti consigliamo di affidarti esclusivamente ad un consulente fiscale,finanziario, esperto di diritto del lavoro o quantomeno facendo affidamento al portale INPS all'interno della propria area riservata: "https://www.inps.it/it/it/dettaglio-scheda.it.schede-servizio-strumento.schede-strumenti.la-mia-pensione-futura-simulazione-della-propria-pensione-50033.la-mia-pensione-futura-simulazione-della-propria-pensione.html".
""")

# Età inizio lavoro
eta_inizio = st.slider("Inserisci l'età in cui hai iniziato/prevedi di iniziare a lavorare:", min_value=18, max_value=35, key="eta_inizio")

# Tipologia lavoratore
tip_lav = st.selectbox('Sei/sarai un lavoratore autonomo oppure dipendente?', options=["autonomo", "dipendente"], key="tip_lav").lower()

# Numero mesi tirocinio
stage_m = st.number_input("Inserisci il numero di mesi di tirocinio (se 0, inserisci 0):", min_value=0, step=1, key="stage_m")

# Numero mesi apprendistato per lavoratori dipendenti
appr_m = 0
frazione_stipendio_appr = 0  # Inizializziamo la variabile per evitare problemi di accesso
if tip_lav == "dipendente":
    appr_m = st.number_input("Inserisci il numero di mesi di apprendistato (se 0, inserisci 0):", min_value=0, step=1, key="appr_m")
    frazione_stipendio_appr = st.slider('Il tuo contratto di appr. in che percentuale rispetto al tuo salario lordo futuro/attuale? (0-100%)', min_value=0, max_value=100, step=1, key="frazione_stipendio_appr")

# Età pensionabile
eta_pensionabile = st.slider("Inserisci l'età in cui vorresti andare in pensione:", min_value=61, max_value=72, key="eta_pensionabile")

# Calcolo anni lavorativi e contributivi
stage_a = stage_m // 12
a_lav = eta_pensionabile - eta_inizio - stage_a

# Salario lordo mensile
salario = st.number_input("Inserisci il tuo salario lordo mensile(da 0 a 10000 euro max):", min_value=500.0,max_value = 10000.0, step=50.0, key="salario")

if salario > 0:
    # Calcolo salario annuale e apprendistato
    salario_annuale = salario * 13.5
    appr_a = appr_m // 12
    a_lav2 = a_lav - appr_a
    montante_salario = 0
    percent_appr = frazione_stipendio_appr / 100  # Percentuale per il salario di apprendistato
    salario_appr = round(salario_annuale * percent_appr, 2)
    sum_salario = []
    m_salario = []

    # Gestione degli anni di apprendistato
    for i in range(appr_a):
        montante_salario += salario_appr
        montante_salario = round(montante_salario, 2)
        sum_salario.append(montante_salario)
        m_salario.append(salario_appr)

    # Gestione degli anni di lavoro normale
    for i in range(a_lav2):
        # Scatti di anzianità e premi di produzione
        if (i + 1) % 3 == 0:  
            scatto_anzianita = 240
            salario_annuale += scatto_anzianita
            salario_annuale = round(salario_annuale, 2)

        if (i + 1) % 5 == 0:  
            scatto_livello = 1800
            salario_annuale += scatto_livello
            salario_annuale = round(salario_annuale, 2)

        montante_salario += salario_annuale
        montante_salario = round(montante_salario, 2)
        sum_salario.append(montante_salario)
        m_salario.append(salario_annuale)

    # Calcolo IVS
    sum_IVS = []  
    m_IVS = []
    montante_IVS = 0
    aliquota_contrib_dip = 0.33
    aliquota_contrib_aut = 0.267
    aliquota_appr = 0.10 + 0.0584


    # Ciclo per i dipendenti con gli anni di apprendistato
    if tip_lav.startswith('d'):
        for i in range(appr_a):
            IVS = round(m_salario[i] * aliquota_appr, 2)
            montante_IVS += IVS
            montante_IVS = round(montante_IVS, 2)
            m_IVS.append(IVS)
            sum_IVS.append(montante_IVS)

        # Ciclo per gli anni di lavoro normale
        for i in range(appr_a, len(m_salario)):
            IVS = round(m_salario[i] * aliquota_contrib_dip, 2)
            montante_IVS += IVS
            montante_IVS = round(montante_IVS, 2)
            m_IVS.append(IVS)
            sum_IVS.append(montante_IVS)

    if tip_lav.startswith('a'):
        for i in range(len(m_salario)):
            IVS = round(m_salario[i] * aliquota_contrib_aut, 2)
            montante_IVS += IVS
            montante_IVS = round(montante_IVS, 2)
            m_IVS.append(IVS)
            sum_IVS.append(montante_IVS)

    # Coefficienti di trasformazione
    array_coeff_tr = np.array([0.042, 0.0434, 0.0414, 0.04532, 0.04657, 0.0479, 0.04910, 0.0506, 0.0522, 0.05391, 0.0575])
    array_anni = np.arange(61, 72)
    index_eta_pensionabile = np.where(array_anni == eta_pensionabile)[0][0]
    coeff = array_coeff_tr[index_eta_pensionabile] 

    # Calcola pensione lorda
    pensione_def_lorda = round((coeff * montante_IVS) / 13, 2)

    # Calcola pensione netta in base alle aliquote IRPEF
    if pensione_def_lorda <= 1250:
        pensione_def_netta = round(pensione_def_lorda - (pensione_def_lorda * 0.23), 2)
    elif 1250 < pensione_def_lorda <= 2333.33:
        pensione_def_netta = round(pensione_def_lorda - 287.5 - ((pensione_def_lorda - 1250) * 0.25), 2)
    elif 2333.33 < pensione_def_lorda <= 4166.67:
        pensione_def_netta = round(pensione_def_lorda - 558.33 - ((pensione_def_lorda - 2333.33) * 0.35), 2)
    else:
        pensione_def_netta = round(pensione_def_lorda - 1199.99 - ((pensione_def_lorda - 4166.67) * 0.43), 2)

    # Simulazione Monte Carlo
    pensione_def_netta_std = 200
    outputs = []
    n_iter = 10000
    for i in range(n_iter):
        montecarlo = -1
        while montecarlo < 0:
            montecarlo = round(rd.normalvariate(pensione_def_netta, pensione_def_netta_std), 2)
        outputs.append(montecarlo)

    st.write(f"I tuoi anni lavorativi saranno di {a_lav} anni")
    st.write(f"Il tuo montante contributivo sarà di {montante_IVS} euro")
    st.write(f"La tua pensione lorda sarà di {pensione_def_lorda} euro")
    st.write(f"La tua pensione netta sarà di {pensione_def_netta} euro")

    #Dataframe
    df = pd.DataFrame({"Pensione attesa (P(x))": outputs})

    # Calcolo delle statistiche
    media = round(df["Pensione attesa (P(x))"].mean(),2)
    std_dev = round(df["Pensione attesa (P(x))"].std(),2)
    media_discontinua = round(media - std_dev,2)
    media_forte_discontinua = round(media - 1.75 * std_dev,2)

    # Creazione del grafico
    fig = go.Figure()

    # Aggiunta dell'istogramma con opacità
    fig.add_trace(go.Histogram(
        x=df['Pensione attesa (P(x))'],
        name='Distribuzione',
        opacity=0.4,  # Imposta l'opacità a un valore più basso
        marker_color='blue',
        nbinsx=100  # Numero di bin
    ))

    # Aggiunta delle linee verticali che si adattano all'altezza massima delle frequenze
    fig.add_shape(type="line",
                x0=media, y0=0, x1=media, y1=400,
                line=dict(color="green", width=3, dash="solid"),
                name='Carriera lavorativa costante'
    )

    fig.add_shape(type="line",
                x0=media_discontinua, y0=0, x1=media_discontinua, y1=400,
                line=dict(color="orange", width=3, dash="dash"),
                name='Carriera lavorativa discontinua'
    )

    fig.add_shape(type="line",
                x0=media_forte_discontinua, y0=0, x1=media_forte_discontinua, y1=400,
                line=dict(color="red", width=3, dash="dot"),
                name='Carriera lavorativa fortemente discontinua'
    )

    # Aggiornamento del layout
    fig.update_layout(
        title='Distribuzione della pensione attesa (P(x))<br><sup>Per vedere il valore delle linee verticali trascinare il mouse sull\'asse x = 0<br><sup>',
        xaxis_title='Pensione attesa (P(x))',
        yaxis_title='Frequenza',
        width=1200,
        height=600,
        plot_bgcolor='rgba(0, 0, 0, 0)',  # Imposta uno sfondo trasparente
        showlegend=True  # Mostra la leggenda
    )

    # Aggiunta delle linee alla leggenda
    fig.add_trace(go.Scatter(x=[media], mode='lines', name='Carriera lavorativa costante', line=dict(color='green', width=3)))
    fig.add_trace(go.Scatter(x=[media_discontinua], mode='lines', name='Carriera lavorativa discontinua', line=dict(color='orange', width=3)))
    fig.add_trace(go.Scatter(x=[media_forte_discontinua], mode='lines', name='Carriera lavorativa fortemente discontinua', line=dict(color='red', width=3)))

    # Mostra il grafico
    st.plotly_chart(fig)






# Documentazione per la WebApp "PsychoBot"

## Introduzione
**PsychoBot** è un'applicazione web che funge da psicologo virtuale, progettata per offrire supporto emotivo, consigli e un ambiente sicuro per conversazioni anonime. Grazie all'integrazione con il modello di intelligenza artificiale, PsychoBot può rispondere a messaggi in diversi stili di conversazione per adattarsi meglio alle esigenze dell'utente.

## Funzionalità principali

1. **Supporto psicologico personalizzato**: L'app può rispondere in vari stili di conversazione per meglio adattarsi al tono e alla natura della conversazione.
2. **Stili di conversazione**: Gli utenti possono scegliere tra stili di conversazione **Neutrale**, **Formale**, **Informale** ed **Empatico** per personalizzare la loro esperienza.
3. **Audio di risposta**: PsychoBot può leggere ad alta voce le risposte, grazie alla funzione di sintesi vocale (gTTS), se l'utente attiva l'opzione di audio.
4. **Accesso sicuro e privato**: Tutte le conversazioni rimangono private e non vengono registrate o memorizzate al di fuori della sessione corrente.
5. **Disponibilità 24/7**: PsychoBot è sempre attivo, pronto a rispondere in qualsiasi momento.

## Interfaccia Utente

### Layout
- **Titolo**: Il titolo principale dell'app è "Benvenuto su 💬 PsychoBot!", che introduce l'applicazione.
- **Sottotitolo**: "Il tuo psicologo virtuale, sempre disponibile per ascoltarti." fornisce una breve descrizione del servizio.
- **Caratteristiche principali**: Le principali funzionalità sono presentate sotto forma di elenco con emoji per attirare l'attenzione sugli aspetti chiave.
- **Istruzioni per l'uso**: Una guida su come iniziare a interagire con PsychoBot.

### Menu Laterale (Sidebar)
- **Impostazioni**:
  - **Stile di conversazione**: Un menu a discesa consente agli utenti di scegliere il tono della conversazione (Neutrale, Formale, Informale, Empatico).
  - **Attivazione audio**: Una casella di controllo consente agli utenti di abilitare o disabilitare la riproduzione audio.
  - **Nuova conversazione**: Un pulsante che permette di iniziare una nuova chat, ripristinando la sessione di chat.

### Interfaccia di Chat
- **Messaggi della conversazione**: I messaggi dell'utente e del bot vengono visualizzati come una conversazione continua.
- **Input dell'utente**: Un campo di input permette all'utente di scrivere e inviare i messaggi.
- **Bot di risposta**: PsychoBot risponde in base al messaggio dell'utente, adattando la risposta al tono selezionato.

## Flusso di utilizzo
1. **Impostazioni iniziali**:
   - L'utente può selezionare il tono della conversazione (Neutrale, Formale, Informale, Empatico).
   - Può anche scegliere se attivare l'audio.
2. **Avvio di una conversazione**:
   - L'utente interagisce con PsychoBot attraverso il campo di input, e il bot risponde in base al tono scelto.
   - Ogni nuova conversazione può essere avviata cliccando sul pulsante "🔄 Start New Chat" nella barra laterale.
3. **Conversazione con PsychoBot**:
   - PsychoBot risponde a tutti i messaggi dell'utente in tempo reale.
   - Se l'utente attiva la riproduzione audio, PsychoBot leggerà le risposte a voce alta.
4. **Personalizzazione delle risposte**:
   - PsychoBot può rispondere in uno stile **formale**, **informale**, **empatico** o **neutrale**, in base alla scelta dell'utente.

## Componenti principali del codice

### Importazioni
- **Streamlit**: Viene utilizzato per creare e gestire l'interfaccia utente.
- **OpenAI API**: Utilizzata per generare risposte personalizzate tramite un modello AI (che in questo esempio è una versione locale del modello).
- **gTTS (Google Text-to-Speech)**: Permette di generare audio dalle risposte di PsychoBot, che può essere riprodotto direttamente dall'utente.

### Funzionalità principali
1. **chat_with_psychobot**: Questa funzione interagisce con il modello di intelligenza artificiale e genera risposte basate sullo stile scelto.
2. **play_audio**: Se l'audio è abilitato, questa funzione converte il testo della risposta in audio e lo riproduce all'utente.
3. **chat_interface**: Gestisce l'interfaccia di chat, visualizzando i messaggi dell'utente e le risposte del bot, oltre a gestire l'input dell'utente.

### Configurazione dell'API OpenAI
- La funzione `openai.ChatCompletion.create` è utilizzata per ottenere una risposta dal modello AI. In questo caso, viene configurato per rispondere in base allo stile di conversazione selezionato.
  
### Gestione dei messaggi
- La sessione viene memorizzata in `st.session_state`, mantenendo traccia dei messaggi precedenti e garantendo che la conversazione continui senza interruzioni.

## Considerazioni sulla sicurezza e sulla privacy
PsychoBot garantisce che tutte le conversazioni avvengano localmente, senza inviare dati sensibili a server esterni. Le conversazioni non vengono memorizzate dopo il termine della sessione.

## Conclusioni
PsychoBot è un'applicazione utile per chi cerca supporto emotivo o un dialogo empatico in qualsiasi momento della giornata. Con il supporto di un'intelligenza artificiale, gli utenti possono sentirsi ascoltati e compresi senza preoccupazioni di privacy.

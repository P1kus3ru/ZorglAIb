# Opstellen van .env-bestand

Kopieer eerst [.env.sample](../.env.sample) naar .env door het volgende commando uit te voeren.

``cp .env.sample .env``

Open nu .env in een teksteditor naar keuze en werk de variabelen bij. Hieronder volgt een meer gedetailleerde beschrijving van elke omgevingsvariabele

## Loggen 

Deze variabele kan ingesteld worden op _True_ of _False_. Stel in op _True_ als je meer gedetailleerde logging van de terminal wilt zien tijdens het uitvoeren van de python scripts.
Zet op _False_ als je het loggen wilt uitschakelen.

## Services Urls 

Dit zijn de basis urls voor de Whisper en Voicevox services. Je kunt deze op localhost laten staan als je ze op je lokale machine draait.

De toets die je ingedrukt moet houden als je wilt dat je stem wordt opgenomen en vertaald. Bijvoorbeeld MIC_RECORD_KEY=t als je de 't'-toets ingedrukt wilt houden.

## Ids audioapparaat

Hier voer je de ID's in voor de verschillende audioapparaten die het programma zal gebruiken.
Dit is nodig om python te laten weten vanaf welk audioapparaat er geluisterd of audio afgespeeld moet worden.
Voer [get_audio_device_ids.py](../src/modules/get_audio_device_ids.py) uit om de id voor uw audioapparaten te verkrijgen.
De uitvoer van dit commando kan afgekapt zijn, maar doe je best om de juiste id voor het audio device te selecteren.

## Timeout

REQUEST_TIMEOUT is het maximum aantal seconden om te wachten op een antwoord van Whisper voordat het verzoek wordt gestopt.

## Finish

Je bent eindelijk klaar met het instellen van je omgevingsvariabelen. Om **ZorglAIb** te starten, ga naar [gebruik](../README.md#Gebruik).

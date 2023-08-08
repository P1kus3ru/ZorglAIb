# ZorglAIb

Beschrijving

## Integratie van AI

Dit project integreert vrije en open-source AI-systemen:

1. [WhisperAI](https://github.com/openai/whisper): Algemeen spraakherkenningsmodel ontwikkeld door OpenAI dat meertalige spraakherkenning kan uitvoeren.


WhisperAI heeft een docker images beschikbaar op DockerHub, dus we zullen het bouwen en draaien via een [Docker Compose bestand](docker-compose.yml).

## Hoe het werkt

**ZorglAIb** bestaat uit één main python programma.

### Voice Transcriber

[voice_transcriber.py](src/voice_transcriber.py) neemt je microfoon op wanneer een push-to-talk toets wordt ingedrukt op het toetsenbord.
Zodra deze toets wordt losgelaten, slaat het je stem op in een audiobestand dat vervolgens naar WhisperAI's transcribe endpoint wordt gestuurd die er Automatic Speech Recognition (ASR) op uitvoert.

## Toepassing


## Setup

Het instellen van **ZorglAIb** vereist 2 cruciale stappen, dus mis er geen een!
1. [Services en dependencies installeren](docs/INSTALLATION.md)
2. [Environment variabelen opstellen](docs/ENV.md)

## Gebruik

Om **ZorglAIb** te draaien, moet je eerst WhisperAI draaien. Deze kan worden uitgevoerd via Docker
### Docker

#### WhisperAI

Als je Whisper op je computer wilt draaien, voer dan deze commando's uit in de map met het [docker-compose.yml](docker-compose.yml) bestand.

Om WhisperAI te draaien:

``docker-compose up -d``

Om het draaien van de containers te stoppen:

``docker-compose down``

Als je Windows Subsystem for Linux (WSL) draait, vergeet dan niet om het af te sluiten om je ram terug te winnen. Dit moet pas nadat je de containers hebt gestopt en klaar bent met het gebruik van het programma.

``wsl --shutdown``

### Python-programma

Voer deze commando's uit in de map [src/](src).

Om de toepassing uit te voeren

``python voice_transcriber.py``

Druk op `Ctrl+C` in de terminal om de python-scripts te stoppen.


### Dingen om op te merken

Enkele belangrijke dingen om in gedachten te houden bij het gebruik van **LanguageLeapAI**.

#### Whisper's inconsistentie

Houd er rekening mee dat WhisperAI niet bepaald de meest nauwkeurige is en niet 100% van de tijd spraak correct zal transcriberen, dus gebruik het op eigen risico.
Totdat OpenAI besluit om de dataset te verbeteren die is gebruikt om de Whisper-modellen te trainen, zal dit voldoende moeten zijn.

## Licentie

De code van LanguageLeapAI is vrijgegeven onder de MIT-licentie. Zie [LICENSE](LICENSE) voor meer informatie.

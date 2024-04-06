# Secuencia de trabajo

## 0. Instalación

### 0.1 Bibliotecas de Python

```bash
python -m venv .venv --prompt "Entorno virtual"
```

```bash
source ./.venv/bin/activate
```

```bash
pip install pip install silabeador fonemas stanza==1.7.0 libEscansion txt2tei
```

#### 0.2 Modelos de lengua
```bash
export STANZA_RESOURCES_DIR=./.venv/lib/python3.11/site-packages/stanza/resources
python
```

```
Python 3.11.2 (main, Mar 13 2023, 12:18:29) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
```

```python
import stanza
stanza.download(lang="es",
                package=None,
                processors={"ner": "ancora",
                            "tokenize": "ancora",
                            "pos": "ancora",
                            "lemma": "ancora",
                            "mwt":"ancora",
                            "constituency":"combined_charlm",
                            "depparse": "ancora",
                            "sentiment": "tass2020"}) 
```

## 1. Limpieza y preprocesado

### 1.1 De PDF a TXT
```bash
pdftotext -layout  -nodiag LopeAcreedores.pdf
```

### 1.2. De TXT a VED
```bash
sed -i 's/(\w\+)  \+/\1\n/g'
```
## 2. Modelado de datos

### 2.1. De VED a XML-TEI

### 2.2. De VED a CSV

## 3. Anotación métrica del corpus
### 3.1. Verso a verso
```python
from libEscansion import VerseMetre
verso = '¡A la escota! ¡Al chafaldete!'
resultado = VerseMetre(verso)
```

```python
for atributo in ['line', 'count', 'syllables', 'rhyme', 'asson', 'nuclei', 'rhythm']:
    print(f'{atributo}:\t{getattr(resultado, atributo)}')
```
### 3.2 Procesamiento masivo


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

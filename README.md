# Text Sentiment Analyzer (TextBlob + VADER)

Analyze the sentiment of any English text using **two independent engines**:
[TextBlob](https://textblob.readthedocs.io/) (polarity/subjectivity) and
[VADER](https://github.com/cjhutto/vaderSentiment) (Valence Aware Dictionary and
sEntiment Reasoner). Available as both a **CLI tool** and a **Tkinter app**.

![Python](https://img.shields.io/badge/Python-3.x-3776AB)
![TextBlob](https://img.shields.io/badge/TextBlob-NLP-4B8BBE)
![VADER](https://img.shields.io/badge/VADER-sentiment-4B8BBE)
![GUI](https://img.shields.io/badge/GUI-Tkinter-blue)

## Features

### CLI version

- Interactive prompt â€” type sentences, get results, type `exit` to quit
- Both engines report their verdict: **Positive / Neutral / Negative**

### GUI version

- Paste or type text in a scrolled text area
- Supports **Ctrl+Enter** and **Ctrl+A** shortcuts to analyze
- Detailed result panel showing:
  - TextBlob **polarity** and **subjectivity** (objective â†” opinionated)
  - VADER **compound** score with positive / neutral / negative percentages
  - An **overall agreement** verdict when both models agree

## Getting Started

### Requirements

Install the dependencies:

```bash
pip install textblob vaderSentiment
```

### Run the CLI version

```bash
python Text_Sentiment_Analyzer/app.py
```

```
Enter a sentence for sentiment analysis (or type 'exit' to quit): This movie was amazing!
TextBlob Sentiment: Positive
VADER Sentiment: Positive
```

### Run the GUI version

```bash
python app_tk.py
```

Type text, press **Analyze** (or Ctrl+Enter), and read the results.

## Sentiment thresholds

- **Positive** â€” polarity / compound score above `+0.05`
- **Negative** â€” score below `-0.05`
- **Neutral** â€” anything in between

## Project structure

```
text_sentiment_analyzer_using_textblob-VADER/
â”œâ”€â”€ app_tk.py                          # Tkinter GUI
â””â”€â”€ Text_Sentiment_Analyzer/
    â””â”€â”€ app.py                         # CLI version
```

## License

This project is open-source and available under the [MIT License](LICENSE).
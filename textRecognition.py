from natasha import Doc, Segmenter, NewsMorphTagger, NewsEmbedding, NewsSyntaxParser

SPEECH_PARTS = {'ADJ': 'прилагательное',
                'ADP': 'предлог',
                'ADV': 'наречие',
                'AUX': 'глагол',
                'CONJ': 'союз',
                'CCONJ': 'союз',
                'DET': 'определитель',
                'INTJ': 'междометие',
                'NOUN': 'существительное',
                'NUM': 'цифра',
                'PART': 'частица',
                'PRON': 'местоимение',
                'PROPN': 'имя собственное',
                'PUNCT': 'пунктуация',
                'SCONJ': 'союз',
                'SYM': 'символ',
                'VERB': 'глагол'}

# Инициализация компонентов блиблотеки анализа текста Natasha
segmenter = Segmenter()
emb = NewsEmbedding()
morph_tagger = NewsMorphTagger(emb)
syntax_parser = NewsSyntaxParser(emb)


# Функция анализа текста
# Возвращает список кортежей (слово, часть речи)
def analyse(text: str):
    doc = Doc(text)

    doc.segment(segmenter)
    doc.tag_morph(morph_tagger)
    doc.parse_syntax(syntax_parser)

    # Содержит проанализированные предложения
    items = [[value for value in sent.morph.as_json.values()] for sent in doc.sents]
    res = []
    for sentence in items:
        for token in sentence[0]:
            res.append((token.text, SPEECH_PARTS[token.pos] if token.pos != 'PUNCT' else ''))
    return res


# Возвращает проанализированное предложение
def get_analysed(text: str):
    text = analyse(text)
    res = ''
    for word, ps in text:
        space = ' ' if ps and res else ''
        res += f'{space}{word}({ps})' if ps else f'{space}{word}'
    return res

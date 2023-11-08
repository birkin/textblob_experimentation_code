import logging, pprint
from collections import Counter  
from math import ceil

from textblob import TextBlob, Word
from nltk.corpus import stopwords


logging.basicConfig(
    format='%(asctime)s : %(levelname)s : %(message)s', 
    level=logging.INFO
    # level=logging.DEBUG
    )
log = logging.getLogger(__name__)


def run_code( file_path: str ):
    """ Manager.
        Called by __main__. """
    log.debug( 'starting run_code()' )
    input_text: str = load_text( file_path )

    ## get extracted nouns
    text_obj = TextBlob( input_text )
    nouns = list()

    word_tag_tuples = text_obj.tags
    log.debug( f'word_tag_tuples, ``{pprint.pformat(word_tag_tuples)}``' )

    stop_words = set(stopwords.words('english'))

    log.debug( 'nouns...' )
    for word, tag in text_obj.tags:
        if tag == 'NN' or tag == 'NNP':    # tag == 'NN' represents that the word is classified as a noun by TextBlob
            if word.lower() not in stop_words and len(word) >= 3:  # Filter out stop words and short words
                # log.debug( f'noun, ``{word}``')
                nouns.append(word)
            else:
                log.debug( f'ignoring word, ``{word}``' )

    ## normalize case and lemmatize
    fixed_nouns = list()
    for noun in nouns:
        if noun.isupper():
            log.debug(f'ignoring uppercase noun, ``{noun}``')
        else:
            noun = noun.lower()
            noun = Word(noun).lemmatize()  # lemmatization
            log.debug(f'lemmatized and lowercased noun, ``{noun}``')
        fixed_nouns.append(noun)

    log.debug( f'sorted nouns, ``{pprint.pformat( sorted(fixed_nouns) )}``' )

    ## determine frequency
    log.debug( f'nouns_count, ``{len(fixed_nouns)}``' )
    noun_freq = Counter(fixed_nouns)
    total_nouns = len(noun_freq)
    top_percent_value = 0.05  # calculate the top x% of nouns, but limit to a maximum of 7
    top_percent_count = ceil( total_nouns * top_percent_value )
    log.debug( f'top_percent_value, ``{top_percent_value}``top_percent_count, ``{top_percent_count}``' )
    top_n_count = min( top_percent_count, 7 )
    top_nouns = noun_freq.most_common(top_n_count)

    ## output results
    for noun, freq in top_nouns:
        log.info(f'{noun}: {freq}')

    ## end def run_code()


def load_text( file_path: str ) -> str:
    text = 'init'
    with open( file_path, 'r' ) as f:
        text = f.read()
    return text


# output...
# HHoag OCRed text ------------------------------------
# 2023-11-08 14:12:19,714 : INFO : metro: 36
# 2023-11-08 14:12:19,714 : INFO : government: 15
# 2023-11-08 14:12:19,714 : INFO : county: 14
# 2023-11-08 14:12:19,714 : INFO : state: 11
# 2023-11-08 14:12:19,714 : INFO : city: 10
# 2023-11-08 14:12:19,714 : INFO : charter: 9
# 2023-11-08 14:12:19,714 : INFO : power: 9

# Obama speech ----------------------------------------
# 2023-11-08 14:12:19,784 : INFO : america: 18
# 2023-11-08 14:12:19,784 : INFO : country: 13
# 2023-11-08 14:12:19,784 : INFO : tonight: 7
# 2023-11-08 14:12:19,784 : INFO : nation: 7
# 2023-11-08 14:12:19,784 : INFO : future: 7
# 2023-11-08 14:12:19,784 : INFO : work: 7
# 2023-11-08 14:12:19,784 : INFO : family: 5


if __name__ == '__main__':
    log.debug( 'starting __main__' )
    log.info( '\n\nHHoag OCRed text ------------------------------------' )
    run_code( './sample_hhoag_ocr.txt' )
    log.info( '\n\nObama speech ----------------------------------------' )
    run_code( './sample_obama_speech.txt' )

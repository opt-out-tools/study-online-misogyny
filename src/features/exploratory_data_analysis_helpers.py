from typing import Dict

import pandas as pd


def density_of_curse_words_in_sentence(tweet: str) -> Dict[str, float]:
    """Returns the density of top 20 curse words, taken from Wang, Wenbo,  et  al.
    Cursing  in english on  twitter."
    The method needs the punctuation to be removed.
    Args:
        tweet (str) : the tweet to be counted.
    Returns:
        density (dict) : the curse words and their densities.
    """
    curse_words = [
        "fuck",
        "shit",
        "ass",
        "bitch",
        "nigga",
        "hell",
        "whore",
        "dick",
        "piss",
        "pussy",
        "slut",
        "puta",
        "tit",
        "damn",
        "fag",
        "cunt",
        "cum",
        "cock",
        "blowjob",
    ]

    # here we are going to use above words as roots in dictionary and then
    # as dictionary value add them and their plurals in order to make magic happen
    # I'm just adding plural but you can easily extend it with synonyms and such

    curse_roots = {
        curse_word: [curse_word, f"{curse_word}s"] for curse_word in curse_words
    }

    # now we create look_up dictionary which is a reverse of above (all values become
    # keys, and key become values)
    lookup = {}
    for key, values in curse_roots.items():
        for value in values:
            lookup[value] = key
    # here we add counter
    counts = {curse: 0.0 for curse in curse_words}

    #####
    tweet_words = tweet.lower().split(" ")
    # cleaning up white space
    tweet_words = [tweet_word.strip() for tweet_word in tweet_words]

    # now we just need to count how many times is each curse root used
    for word in tweet_words:
        if word in lookup:
            counts[lookup[word]] += 1

    # all done, now we just need frequency
    for key in counts:
        counts[key] /= float(len(tweet_words))
    return counts


def density_of_curse_words_in_corpus(dataframe: pd.DataFrame) -> Dict:
    """Returns density of curse words across an entire corpus

      Args:
        dataframe (pandas df) : the df with the tweets to be counted.

    Returns:
        count (dict) : the curse words and their densities.

    """
    dataframe["curse_words"] = dataframe["text"].apply(
        density_of_curse_words_in_sentence
    )
    count = pd.DataFrame(list(dataframe["curse_words"])).T.sum(axis=1) / len(dataframe)
    return dict(count)

"""
Code for Problem 2 of HW 2.
"""
from typing import Any, Dict, List

import torch
from bs4 import BeautifulSoup
from nltk.tokenize import TreebankWordTokenizer


class Tokenizer:
    """
    Problems 2d and 2e: Complete the implementation of this class based
    on the docstrings and the usage examples in the problem set.

    This class is a wrapper around nltk's TreebankWordTokenizer. Its
    function is to tokenize a raw mini-batch and turn it into a valid
    input for an LSTMSentimentClassifier.
    """

    def __init__(self, vocab: List[str]):
        self.words = list(vocab) + ["[BOS]", "[EOS]", "[UNK]", "[PAD]"]
        self.indices = {w: i for i, w in enumerate(self.words)}
        self.nltk_tokenizer = TreebankWordTokenizer()

    def __len__(self):
        return len(self.words)

    def __getitem__(self, item: str) -> int:
        if item in self.indices:
            return self.indices[item]
        else:
            return self.indices["[UNK]"]

    def __call__(self, batch: Dict[str, Any]) -> Dict[str, torch.LongTensor]:
        """
        Problem 2e: Implement this function.

        Converts a batch of examples, represented as raw text, into a
        tensor format compatible with the LSTMSentimentClassifier.

        :param batch: A batch of examples in raw form
        :return: The batch, in tensor form
        """
        raise NotImplementedError("Problem 2e has not been completed yet!")

    @staticmethod
    def normalize(text: str) -> str:
        """
        Removes HTML tags from a text.

        :param text: A text, represented as a raw string
        :return: The text, with HTML tags removed and whitespace
            collapsed
        """
        soup = BeautifulSoup(text, "html.parser")
        return " ".join(soup.get_text(separator=" ").split())

    def tokenize(self, text: str) -> List[str]:
        """
        Problem 2d: Implement this function.

        Splits a text into tokens using self.nltk_tokenizer and NLTK's
        sent_tokenize function.

        :param text: A text, represented as a raw string
        :return: The text, split into a list of tokens
        """
        raise NotImplementedError("Problem 2d has not been completed yet!")

    def postprocess(self, tokens: List[str]) -> List[str]:
        """
        Problem 2d: Implement this function.

        Adds [BOS] and [EOS] to a list of tokens and replaces unknown
        tokens with [UNK].

        :param tokens: A list of tokens
        :return: The post-processed tokens
        """
        raise NotImplementedError("Problem 2d has not been completed yet!")

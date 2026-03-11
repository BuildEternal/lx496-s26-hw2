"""
Code for Problem 2 of HW 2.
"""

from typing import Any, Dict, List

import torch
from bs4 import BeautifulSoup
from nltk import sent_tokenize, download
from nltk.tokenize import TreebankWordTokenizer

download("punkt_tab")


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
        text_tokenized = [self.postprocess(self.tokenize(self.normalize(s))) for s in batch["text"]]
        text_lengths = [len(s) for s in text_tokenized]
        max_text_length = max(text_lengths)
        text_encoded = [[self[w] for w in s] + [self["[PAD]"]] * (max_text_length - len(s)) for s in text_tokenized]

        out_text = torch.LongTensor(text_encoded)
        out_label = torch.LongTensor(batch["label"])
        out_lengths = torch.LongTensor(text_lengths)

        return {"text": out_text, "label": out_label, "lengths": out_lengths}

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
        return [item for s in sent_tokenize(text) for item in TreebankWordTokenizer().tokenize(s)]

    def postprocess(self, tokens: List[str]) -> List[str]:
        """
        Problem 2d: Implement this function.

        Adds [BOS] and [EOS] to a list of tokens and replaces unknown
        tokens with [UNK].

        :param tokens: A list of tokens
        :return: The post-processed tokens
        """
        processed_tokens = [s if s in self.indices else "[UNK]" for s in tokens]
        processed_tokens.insert(0, "[BOS]")
        processed_tokens.append("[EOS]")
        return processed_tokens

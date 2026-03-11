# Written Problems

## Problem 1

### Problem 1b

My guess would be that, running a variety of models on the same dataset ensures that any variation in the outputs of
said models is from the model itself and not a result of variations in the testing data. For example, if one model gets
72% accuracy, and another model gets 74% accuracy, we know that this difference of 2% is from the model itself and not
from variation in the data used for testing.

### Problem 1c

I would guess that it's because any data used to tweak the model should come from the training data, and not the testing
data. If the model is at all influenced by the data used for testing, then we can't be sure that the model truly learned
instead of just memorizing the testing data, defeating the purpose of using the testing data as a model benchmark.

### Problem 1d

The paper states that reviews with a score $≥7$ were labeled positive, review with a score $≤4$ were labeled negative,
and all other reviews (considered neutral by the paper) were not included in the dataset.

## Problem 2

### Problem 2b

If I recall correctly, these are called "morphemes", and it's important to break down words into their individual
morphemes during tokenization because each morpheme has its own basic semantic information, which will make the
tokenization higher resolution and more accurate, so to speak.

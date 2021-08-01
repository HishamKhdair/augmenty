import random
from functools import partial
from typing import Iterator, Callable

import spacy
from spacy.language import Language
from spacy.training import Example

@spacy.registry.augmenters("upper_case.v1")
def create_upper_casing_augmenter(
    level: float,
) -> Callable[[Language, Example], Iterator[Example]]:
    """Create a data augmentation callback that converts documents to uppercase.
    The callback can be added to a corpus or other data iterator during training.

    Args:
        level (float): The percentage of examples that will be augmented.

    Returns:
        Callable[[Language, Example], Iterator[Example]]: The augmenter.
    """
    return partial(upper_casing_augmenter, level=level)


@spacy.registry.augmenters("spongebob_augmenter.v1")
def create_spongebob_augmenter(
    level: float,
) -> Callable[[Language, Example], Iterator[Example]]:
    """Create a data augmentation callback that converts documents to SpOnGeBoB casing.

    Args:
        level (float): The percentage of examples that will be augmented.

    Returns:
        Callable[[Language, Example], Iterator[Example]]: The augmenter.
    """
    return partial(spongebob_augmenter, level=level)


def upper_casing_augmenter(
    nlp: Language, example: Example, *, level: float
) -> Iterator[Example]:
    if random.random() >= level:
        yield example
    else:
        example_dict = example.to_dict()
        doc = nlp.make_doc(example.text.upper())
        example_dict["token_annotation"]["ORTH"] = [t.text.upper() for t in example.reference]
        yield example.from_dict(doc, example_dict)


def spongebob_augmenter(
    nlp: Language, example: Example, *, level: float
) -> Iterator[Example]:
    if random.random() >= level:
        yield example
    else:
        chars = [c.lower() if i % 2 else c.upper() for i, c in enumerate(example.text)]
        example_dict = example.to_dict()
        doc = nlp.make_doc("".join(chars))
        example_dict["token_annotation"]["ORTH"] = [t.text for t in doc] 
        yield example.from_dict(doc, example_dict)
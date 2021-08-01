import random
from functools import partial
from typing import Iterator, Callable

import spacy
from spacy.language import Language
from spacy.training import Example

@spacy.registry.augmenters("random_casing.v1")
def create_random_casing_augmenter(
    level: float,
) -> Callable[[Language, Example], Iterator[Example]]:
    """Create a data augmentation callback that randomly changes the casing of the document.
    The callback can be added to a corpus or other data iterator during training.

    Args:
        level (float): The percentage of character that will have its casing changed.

    Returns:
        Callable[[Language, Example], Iterator[Example]]: The augmenter.
    """
    return partial(random_casing_augmenter, level=level)

def random_casing_augmenter(
    nlp: Language, example: Example, *, level: float
) -> Iterator[Example]:
    def __casing(c):
        if random.random() < level:
            return c.lower() if random.random() < 0.5 else c.upper() 
        return c

    chars = [__casing(c) for c in example.text]
    example_dict = example.to_dict()
    doc = nlp.make_doc("".join(chars))
    example_dict["token_annotation"]["ORTH"] = [t.text for t in doc] 
    yield example.from_dict(doc, example_dict)
from .casing import (
    create_conditional_token_casing_augmenter,
    create_starting_case_augmenter,
)
from .replace import create_token_replace_augmenter, create_wordnet_synonym_augmenter
from .spacing import (
    create_grundtvigian_spacing_augmenter,
    create_spacing_insertion_augmenter,
)
from .swap import create_token_swap_augmenter

from .insert import (
    create_duplicate_token_augmenter,
    create_random_synonym_insertion_augmenter,
    create_token_insert_augmenter,
    create_token_insert_random_augmenter,
)

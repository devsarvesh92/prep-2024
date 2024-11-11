

import pytest

from prep_2024.blind_75.array_and_hashing.duplicate_integer import has_duplicate


pytestmark=pytest.mark.duplicateinteger



def test_duplicate_integer():
    assert has_duplicate(nums=[1, 2, 3, 3]) is True
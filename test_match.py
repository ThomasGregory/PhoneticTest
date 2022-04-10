from match import match, match_list

def test_exactly_the_same_matches():
    assert match("Something", "Something")

def test_different_spelling_matches():
    assert match("Jon", "John")

def test_pretty_different_words_dont_match():
    assert not match("Henry", "Harry")

def test_match_list_tracks_ids():
    ls = [
        ("James", 0),
        ("Jamess", 1),
        ("Sam", 2),
        ("sam", 3),
        ("James", 4)
    ]
    merged = match_list(ls)
    assert merged["James"] == [0, 1, 4]
    assert merged["Sam"] == [2, 3]
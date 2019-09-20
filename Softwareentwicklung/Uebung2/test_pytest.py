#!/usr/bin/env python

from food_chain import recite


# Tests adapted from `problem-specifications//canonical-data.json` @ v2.1.0
# Beistriche entfernt


def test_fly():
        expected = [
            "I know an old lady who swallowed a fly."
            "I don't know why she swallowed the fly. Perhaps she'll die."
        ]
        assert recite(1, 1) == expected

def test_spider():
        expected = [
            "I know an old lady who swallowed a spider."
            "It wriggled and jiggled and tickled inside her."
            "She swallowed the spider to catch the fly."
            "I don't know why she swallowed the fly. Perhaps she'll die."
        ]
        assert recite(2, 2) == expected

def test_bird():
        expected = [
            "I know an old lady who swallowed a bird."
            "How absurd to swallow a bird!"
            "She swallowed the bird to catch the spider that "
            "wriggled and jiggled and tickled inside her."
            "She swallowed the spider to catch the fly."
            "I don't know why she swallowed the fly. Perhaps she'll die."
        ]
        assert recite(3, 3) == expected

def test_cat():
        expected = [
            "I know an old lady who swallowed a cat."
            "Imagine that, to swallow a cat!"
            "She swallowed the cat to catch the bird."
            "She swallowed the bird to catch the spider that "
            "wriggled and jiggled and tickled inside her."
            "She swallowed the spider to catch the fly."
            "I don't know why she swallowed the fly. Perhaps she'll die."
        ]
        assert recite(4, 4) == expected

def test_dog():
        expected = [
            "I know an old lady who swallowed a dog."
            "What a hog, to swallow a dog!"
            "She swallowed the dog to catch the cat."
            "She swallowed the cat to catch the bird."
            "She swallowed the bird to catch the spider that wriggled "
            "and jiggled and tickled inside her."
            "She swallowed the spider to catch the fly."
            "I don't know why she swallowed the fly. Perhaps she'll die."
        ]
        assert recite(5, 5) == expected

def test_goat():
        expected = [
            "I know an old lady who swallowed a goat."
            "Just opened her throat and swallowed a goat!"
            "She swallowed the goat to catch the dog."
            "She swallowed the dog to catch the cat."
            "She swallowed the cat to catch the bird."
            "She swallowed the bird to catch the spider that "
            "wriggled and jiggled and tickled inside her."
            "She swallowed the spider to catch the fly."
            "I don't know why she swallowed the fly. Perhaps she'll die."
        ]
        assert recite(6, 6) == expected

def test_cow():
        expected = [
            "I know an old lady who swallowed a cow."
            "I don't know how she swallowed a cow!"
            "She swallowed the cow to catch the goat."
            "She swallowed the goat to catch the dog."
            "She swallowed the dog to catch the cat."
            "She swallowed the cat to catch the bird."
            "She swallowed the bird to catch the spider that "
            "wriggled and jiggled and tickled inside her."
            "She swallowed the spider to catch the fly."
            "I don't know why she swallowed the fly. Perhaps she'll die."
        ]
        assert recite(7, 7) == expected

def test_horse():
        expected = [
            "I know an old lady who swallowed a horse."
            "She's dead, of course!"
        ]
        assert recite(8, 8) == expected

def test_multiple_verses():
        #expected = recite(1, 1) + [""] + recite(2, 2) + [""] + recite(3, 3)
        expected = recite(1, 1) + recite(2, 2) + recite(3, 3)
        assert recite(1, 3) == expected

        #self.assertEqual(recite(1, 3), expected)

def test_full_song():
        expected = []
        for n in range(1, 9):
            #expected += recite(n, n) + [""]
            expected += recite(n, n)

        #expected.pop()
        #self.assertEqual(recite(1, 8), expected)
        assert recite(1, 8) == expected

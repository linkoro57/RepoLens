import unittest
from repolens.core.scoring import calculate_score
from repolens.models.issue import Issue

class ScoringTests(unittest.TestCase):
    def test_subtracts_penalties(self):
        self.assertEqual(calculate_score([Issue("x", "Issue", penalty=12)]), 88)

    def test_score_never_becomes_negative(self):
        self.assertEqual(calculate_score([Issue("x", "Issue", penalty=120)]), 0)

from nbresult import ChallengeResultTestCase


class TestDataExploration(ChallengeResultTestCase):
    """Test data loading and numeric feature selection"""

    def test_numeric_features_selected(self):
        """Selected at least core numeric columns from Spotify dataset"""
        self.assertGreaterEqual(
            self.result.numeric_columns_count,
            10,
            "Hint: Should have at least 10 numeric features (danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence). Extra features are fine!")

    def test_correct_row_count(self):
        """Dataset has expected number of songs"""
        self.assertGreater(
            self.result.row_count,
            1000,
            f"Hint: Dataset should have >1000 songs, got {self.result.row_count:,}")

    def test_all_columns_numeric(self):
        """All selected columns are numeric types"""
        self.assertTrue(
            self.result.all_numeric,
            "Hint: spotify_numeric should only contain int64 or float64 columns. Did you use select_dtypes(include=['int64', 'float64'])?")

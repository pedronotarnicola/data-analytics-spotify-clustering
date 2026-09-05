from nbresult import ChallengeResultTestCase


class TestPreprocessing(ChallengeResultTestCase):
    """Test scaling and second model with preprocessed data"""

    def test_scaling_applied(self):
        """RobustScaler applied to numeric features"""
        self.assertEqual(
            self.result.scaled_shape,
            self.result.original_shape,
            "Hint: Scaled data should have same shape as original")

    def test_scaled_model_trained(self):
        """New KMeans model trained on scaled data"""
        self.assertEqual(
            self.result.scaled_n_clusters,
            8,
            "Hint: Scaled model should also have 8 clusters (for comparison)")

    def test_scaled_labels_complete(self):
        """Scaled model assigned labels to all songs"""
        self.assertEqual(
            self.result.scaled_n_labels,
            self.result.n_songs,
            "Hint: Every song should have a cluster label from scaled model")

from nbresult import ChallengeResultTestCase


class TestFirstModel(ChallengeResultTestCase):
    """Test first KMeans model (8 clusters, unscaled)"""

    def test_model_created_8_clusters(self):
        """KMeans model created with 8 clusters"""
        self.assertEqual(
            self.result.n_clusters,
            8,
            f"Hint: First model should have 8 clusters, got {self.result.n_clusters}")

    def test_labels_created(self):
        """Cluster labels assigned to all songs"""
        self.assertEqual(
            self.result.n_labels,
            self.result.n_songs,
            "Hint: Every song should have a cluster label")

    def test_found_8_unique_clusters(self):
        """Model created 8 distinct clusters"""
        self.assertEqual(
            self.result.unique_labels,
            8,
            f"Hint: Should have 8 unique cluster labels, got {self.result.unique_labels}")

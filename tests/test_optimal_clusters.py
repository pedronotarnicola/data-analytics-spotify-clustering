from nbresult import ChallengeResultTestCase


class TestOptimalClusters(ChallengeResultTestCase):
    """Test elbow method and final 6-cluster model"""

    def test_elbow_method_complete(self):
        """Tested K values from 1-20 for elbow method"""
        self.assertGreaterEqual(
            len(
                self.result.inertias),
            10,
            f"Hint: Should test at least 10 K values, got {len(self.result.inertias)}")

    def test_inertias_decreasing(self):
        """Inertia decreases as K increases (sanity check)"""
        self.assertGreater(self.result.inertias[0],
                           self.result.inertias[-1],
                           "Hint: Inertia should decrease as number of clusters increases")

    def test_labels_added_to_dataframe(self):
        """Added cluster labels to original Spotify dataframe"""
        self.assertTrue(self.result.label_column_exists,
                        "Hint: Should add 'label' column to spotify_df")

# Spotify Song Clustering

## Business problem
Group similar songs together based on their audio characteristics, without any predefined genre or label — the same underlying idea behind recommendation and "made for you" playlist features on platforms like Spotify or Netflix.

## Dataset
- **Source**: Le Wagon Data Analytics Bootcamp (public Spotify metadata dataset, ~10,000 songs)
- **Features**: numeric audio attributes — danceability, energy, valence, loudness, speechiness, liveness, tempo, popularity, key, and whether the track is explicit

## Approach
1. **Baseline KMeans (unscaled)**: clustered directly on raw feature values with `k=8` — produced messy, poorly separated clusters
2. **Scaled KMeans**: applied `StandardScaler` before clustering — since KMeans is distance-based, unscaled features (like loudness, on a very different numeric range than danceability) would otherwise dominate the distance calculation
3. **Elbow method**: tested `k` from 1 to 19 to find the point of diminishing returns; selected **k=5**
4. **DBSCAN (density-based alternative)**: compared against KMeans — DBSCAN doesn't require choosing a cluster count upfront and can flag outliers, but performed worse for this use case (see findings)
5. Generated sample "playlists" from each cluster to sanity-check the results qualitatively

## Tools used
`Python` `pandas` `scikit-learn` `matplotlib` `seaborn` `plotly`

## Key findings
- **Scaling was essential**: the unscaled model produced visually chaotic, overlapping clusters; scaling made the structure noticeably cleaner.
- **Elbow method suggested k=5** as a reasonable balance between distinct groups and playlist variety (more clusters gave diminishing improvement in inertia).
- **DBSCAN found only 2 meaningful clusters** (plus a small noise cluster), and flagged **~6% of songs as outliers** — a very different result from KMeans's 5 evenly-sized groups. This highlights that different clustering algorithms encode different assumptions about what a "cluster" is (density vs. distance from a center).

## Business recommendation
For a playlist-generation use case specifically, **KMeans is the better fit**: every song needs to end up in *some* playlist, and KMeans guarantees that (DBSCAN's outliers would be left out entirely). DBSCAN's outlier detection is still a useful complementary signal — it could be repurposed to surface unusual/niche tracks for a "discovery" feature rather than for mainstream playlist assignment.

## Limitations
- Clustering was done on Spotify's own abstract audio features (e.g. "danceability"), which are themselves outputs of an internal model, not raw signal data.
- Cluster quality was only evaluated visually (3D scatter, elbow plot) and qualitatively (sample playlists) — no quantitative cluster-validity metric (e.g. silhouette score) was computed.
- DBSCAN results are sensitive to the `epsilon` and `min_samples` parameters, which were only lightly tuned here.

## How to run this project
```bash
git clone https://github.com/pedronotarnicola/data-analytics-spotify-clustering.git
cd data-analytics-spotify-clustering
pip install -r requirements.txt
jupyter notebook notebooks/analysis.ipynb
```
Data loads directly from a URL inside the notebook — no manual download needed.

## Folder structure
```
data-analytics-spotify-clustering/
├── notebooks/
│   └── analysis.ipynb
├── README.md
└── requirements.txt
```

---
[Portfolio](https://pedronotarnicola.github.io/) · [LinkedIn](https://www.linkedin.com/in/p-l-notarnicola/)

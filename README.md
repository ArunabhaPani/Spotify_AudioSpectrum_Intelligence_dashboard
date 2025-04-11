# 🎧 Spotify AudioSpectrum Intelligence – Power BI Music Dashboard

A dynamic Power BI project designed to analyze Spotify's most streamed songs in 2024, enriched with audio features and album visuals using the Spotify API.

---

## 📊 Project Overview

**Spotify AudioSpectrum Intelligence** is a data visualization project that explores the top streamed songs on Spotify, offering insights into musical trends, artist popularity, and audio features like danceability, energy, and tempo. Album artwork integration brings the dashboard to life visually.

---

## 🔍 What I Solved

Spotify provides raw streaming data and audio features, but lacks a consolidated visual analytics platform for end-user exploration.  
This project solves that gap by transforming raw data into an engaging dashboard, enabling users to interact with audio metrics and visual elements for deeper music intelligence.

---

## 🛠️ How I Solved It

- Cleaned and structured raw CSV data (`Most Streamed Spotify Songs 2024.csv`) using Power Query.  
- Used Python (`spotify_api_authenticator.py`) with Spotipy to fetch album cover URLs from the Spotify API.  
- Converted enriched data into a clean Power BI model with dynamic visuals and slicers.  
- Integrated HTML (`spotify_html_converter_code.txt`) to explore front-end display styling for album art presentation.  
- Exported enhanced data to CSV/Excel (`spotify_with_covers.csv` & `.xlsx`) for seamless Power BI integration.

---

## 📁 Files Included

- `Spotify AudioSpectrum Intelligence.pbix` – Power BI dashboard file  
- `Most Streamed Spotify Songs 2024.csv` – Source dataset  
- `spotify_api_authenticator.py` – Python script to fetch album covers via Spotify API  
- `spotify_with_covers.csv` / `.xlsx` – Enriched dataset with album cover URLs  
- `spotify_html_converter_code.txt` – HTML template to display cropped album cover images  

---

## 🧠 Insights & Benefits

- Analyze audio attributes like **danceability, energy, valence, tempo, and acousticness**.  
- Visualize top artists, most streamed tracks, and their popularity rankings.  
- Enhance storytelling with dynamic visuals and album art integration.  
- Ideal for music data enthusiasts and dashboards that blend analytics with art.

---

## 💡 Future Enhancements

- Add sentiment and genre analysis using NLP on lyrics.  
- Build real-time sync with Spotify API for live trends.  
- Embed album preview players or Spotify links for immersive interaction.

---

## 👨‍💻 Developed By

**Arunbaha Pani**  
*(B.Tech CSE, UIT-RGPV Bhopal)*

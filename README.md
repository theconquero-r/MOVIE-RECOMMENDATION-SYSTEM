# Movie Recommendation System

A **Streamlit-based Movie Recommendation System** that provides movie recommendations based on your favorite movie using **TMDB API**.  

The system uses **movie similarity scores** to recommend similar movies and displays their posters dynamically.  

---

## Features

- Select your favorite movie from a dropdown list.
- Get **top 5 recommended movies** based on similarity.
- View movie **posters** fetched directly from **TMDB API**.
- Built using **Python, Pandas, Streamlit, and Requests**.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/movie-recommendation-system.git
Navigate to the project directory:

bash
Copy code
cd movie-recommendation-system
Create a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
Activate the virtual environment:

Windows:

bash
Copy code
venv\Scripts\activate
Linux/Mac:

bash
Copy code
source venv/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Add your TMDB API key in the app.py:

python
Copy code
api_key = "YOUR_TMDB_API_KEY"
Run the Streamlit app:

bash
Copy code
streamlit run app.py
Open the URL shown in the terminal (usually http://localhost:8501) to use the app.

Project Structure
perl
Copy code
movie-recommendation-system/
│
├─ app.py                  # Main Streamlit app
├─ movies.pkl              # Movie dataset
├─ similarity.pkl          # Movie similarity matrix
├─ requirements.txt        # Python dependencies
└─ README.md               # Project description

License

This project is open-source and free to use.
# Page Turners

Python project for the Coding for Data Science and Data Management course (2026–2027).

## Project description

Page Turners explores the relationship between book popularity and reader appreciation using the goodbooks-10k dataset. Popularity is measured by the number of ratings a book has received, while reader appreciation is measured by its average rating.

## Research questions

1. How are average book ratings distributed?
2. Do books with more ratings tend to receive higher average ratings?
3. How do mean book ratings vary across publication decades?

## Dataset

The project uses `books.csv` from [goodbooks-10k](https://github.com/zygmuntz/goodbooks-10k), included in this repository. It contains 10,000 books and 23 columns.

The main analytical variables are `average_rating`, `ratings_count` and `original_publication_year`. Book IDs, titles and authors are also used for data inspection and counting books.

## Methodology

- Load the CSV with pandas and check that the required columns are present.
- Inspect dataset dimensions, data types, missing values, duplicate book IDs and descriptive statistics.
- Exclude books with missing rating information or nonpositive rating counts. All 10,000 books remain after these filters.
- Plot a histogram of average ratings and a scatter plot of rating counts against average ratings. The scatter plot uses a logarithmic horizontal axis.
- Calculate Pearson correlation with NumPy using the original, untransformed rating counts.
- For the decade analysis, exclude missing and nonpositive publication years, group books by decade and calculate book counts and mean ratings. Display decades from 1950 onwards because earlier decades generally contain fewer books.

## Main findings

- Average book ratings are concentrated around 4 out of 5.
- The Pearson correlation coefficient is approximately 0.045, indicating a very weak positive linear association between popularity and average rating.
- Mean ratings are similar across the displayed decades. The 1960s have the highest mean (4.065), and the 2000s have the lowest (3.977).

## Limitations

The dataset is not representative of all published books. Rating count is only one measure of popularity. The decade groups differ in size, and each book receives equal weight when computing the decade mean. The analysis is descriptive: it does not establish statistical significance or causation.

## Tools and libraries

- Python 3.14.7 — development environment
- pandas — data loading, cleaning and aggregation
- NumPy — numerical calculations
- Matplotlib — visualisations
- Streamlit — presentation of the results

Library versions are specified in `requirements.txt`. Ruff was used to check and format the Python code.

## Project structure

```text
Page-Turners-Project/
├── app.py
├── books.csv
├── requirements.txt
├── README.md
├── .gitignore
└── page_turners/
    ├── __init__.py
    ├── data.py
    ├── analysis.py
    └── plots.py
```

`data.py` loads and cleans the dataset, `analysis.py` performs statistical calculations, and `plots.py` creates the figures. `app.py` imports these functions and presents the results in Streamlit.

## Installation and setup

Use Python 3.14.7, the version used during development.

### 1. Clone the repository

```bash
git clone https://github.com/t-emanty-1/Page-Turners-Project.git
cd Page-Turners-Project
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

Windows (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

macOS or Linux:

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

## Running the application

From the project directory, run:

```bash
python -m streamlit run app.py
```

The application opens in the browser. If it does not open automatically, visit http://localhost:8501. Press `Ctrl+C` in the terminal to stop it.


# Page Turners

## Project Description

Page Turners is a Python project developed for the Coding for Data Science and Data Management course (2026–2027).

The project explores the relationship between book popularity and reader appreciation using the goodbooks-10k dataset. The main objective is to investigate whether books with more ratings tend to receive higher average ratings.

The project uses data cleaning, descriptive statistics and data visualisation to explore patterns in book ratings and popularity. The analysis is presented through an interactive Streamlit application.

## Research Questions

- Do books with more ratings tend to have higher average ratings?
- How are average book ratings distributed?
- How does reader appreciation vary according to publication year?

## Dataset

The project uses the goodbooks-10k dataset, which contains information about 10,000 books.

The main variables considered in the analysis are:

- Book title
- Author
- Original publication year
- Average rating
- Number of ratings

Dataset source: https://github.com/zygmuntz/goodbooks-10k

## Tools and Libraries

- Python 3.14.7
- pandas
- Streamlit

## Project Structure

- `app.py`: Streamlit application and data exploration.
- `books.csv`: Original book dataset.
- `requirements.txt`: Required Python libraries and their versions.
- `.gitignore`: Files and directories excluded from Git.
- `README.md`: Project description and instructions.

## Installation and Setup

Python 3.14.7 was used to develop and test this project.

### 1. Clone the repository

```bash
git clone https://github.com/t-emanty-1/Page-Turners-Project.git
cd Page-Turners-Project
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

On Windows (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

### 4. Install the required libraries

```bash
python -m pip install -r requirements.txt
```

## Running the Application

To launch the Streamlit application, run:

```bash
python -m streamlit run app.py
```

The application will open automatically in the browser.

## Project Status

The project is currently under development.


# MoMo Insights Dashboard – Group 47

## Project Overview

This fullstack web application is designed to extract meaningful insights from MTN MoMo SMS transaction data. It processes XML-based SMS data, stores cleaned and categorized entries in a relational database, and presents them through a redesigned, interactive web dashboard with a unique look and feel.

## Key Objectives

* Convert raw SMS XML data into structured financial records
* Categorize and tag transactions into clear financial types
* Store cleaned data efficiently in an SQLite database
* Build a visually distinct, responsive dashboard for transaction analysis

## What's Different?

Our frontend UI was **completely redesigned** — with a modern layout, refreshed colors, and an improved user experience to visually distinguish our project from others while maintaining all backend functionalities.

## Features

### Backend Processing:

* XML file parsing and text normalization
* Currency formatting and date standardization
* Transaction type classification (payments, withdrawals, deposits, etc.)

### Database Management:

* SQLite-based relational structure
* Duplicate-safe insertion
* Logging system for tracking unprocessable messages

### Frontend Dashboard (Redesigned):

* Clean and modern visual theme
* Filter transactions by type, amount, and time
* Data visualizations using Plotly (pie & bar charts)
* Responsive transaction table with pagination

## Tech Stack

* **Backend**: Python (Flask)
* **Database**: SQLite
* **Frontend**: HTML, CSS (custom layout)
* **Visualization**: Python Plotly

## Project Structure

```
├── Data
│   └── modifies_sms_v2.xml
├── static
│   └── styles.css        
├── templates
│   └── Index.html        
├── db_setup.py
├── insert_data.py
├── parse_data.py
├── load_data.py
├── app.py
├── requirements.txt
├── transactions.db
```

## How to Run the App

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/MomoInsights-GroupB.git
   cd MomoInsights-GroupB
   ```

2. **Install required Python packages**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the database**

   ```bash
   python3 db_setup.py
   ```

4. **Parse and load the SMS data**

   ```bash
   python3 load_data.py
   ```

5. **Start the Flask web server**

   ```bash
   python3 app.py
   ```

6. **View the dashboard**
   Open your browser and go to: [http://localhost:5000](http://localhost:5000)

 *Note: Run `db_setup.py` and `load_data.py` only once. Afterward, only run `app.py` to start the server.*

## Extra Materials

* **Demo video**
(https://drive.google.com/file/d/1mFVz1NDM_2LEbsq5oy3LaMELeMTgz0m1/view?usp=sharing)

* **Project Report**
(https://docs.google.com/document/d/1IQQwg3zi18bvVmKLDdcjPG4QS1xvZ533aIYxfXYN8VE/edit?tab=t.0)

## 👥 Contributors

* Iriza Larissa
* Beni Niyogisubizo
* Yvette Uwimpaye
* Admire Chagaresango



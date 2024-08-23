# Movie Watchlist App

## Overview

Welcome to the Movie Watchlist App! This Flask-based web application allows users to create an account, save movies to their watchlist, add information about those movies, and browse movies added by themselves and others. Whether you're an avid film enthusiast or just looking to keep track of movies you want to watch, this app has you covered.

## Features

- **User Authentication:** Create and manage your account securely.
- **Personal Watchlist:** Save movies to your personal watchlist.
- **Movie Details:** Add and edit information about each movie.
- **Browse Movies:** View and browse movies added by other users.
- **Search Functionality:** Easily find movies to add to your watchlist.

## Technologies Used

- **Flask:** A lightweight WSGI web application framework for Python.
- **MongoDB:** Database engine used for storing user and movie data.
- **Jinja2:** Templating engine for rendering HTML.
- **Bootstrap:** Front-end framework for styling.

## Installation

### To set up and run the Movie Watchlist App on your local machine: 
1. first clone the repository with
   `git clone https://github.com/<yourusername>/movie-watchlist-app.git`
   and navigate into the project directory using
   `cd movie-watchlist-app`.
2. Next, create a virtual environment by running
   `python -m venv venv`.
3. Activate the virtual environment by executing
   on Windows: `venv\Scripts\activate`
   on macOS/Linux: `source venv/bin/activate`
4. Install the required dependencies with
   `pip install -r requirements.txt`
5. Set up the database using your preferred database
6. Finally, run the application with
   `flask run`
The application will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Usage

### Register an Account

1. Open your browser and navigate to the registration page of the app. This is typically found at `http://127.0.0.1:5000/register`.
2. Fill out the registration form with your desired username, email address, and password.
3. Submit the form to create your account.

### Log In

1. After registering, go to the login page at `http://127.0.0.1:5000/login`.
2. Enter your registered username and password.
3. Click the "Log In" button to access your account.

### Add Movies

1. Once logged in, navigate to the "Add Movie" page, which can be accessed via the main menu or at `http://127.0.0.1:5000/add`.
2. Fill in the details of the movie you want to add, including the title, description, release year, and any other relevant information.
3. Click "Save" to add the movie to your personal watchlist.

### Browse Movies

1. To explore movies added by other users, go to the "Browse Movies" section at `http://127.0.0.1:5000/browse`.
2. Browse through the list of movies, use the search bar to find specific titles, or filter by genres or release dates.
3. If you find a movie you want to add to your watchlist, click the "Add to Watchlist" button next to the movie entry.

### Edit Movie Information

1. To edit the details of a movie already on your watchlist, navigate to your watchlist at `http://127.0.0.1:5000/edit/<string:_id>`.
2. Find the movie you wish to edit and click the "Edit" button next to it.
3. Update the movie details as needed and click "Save Changes" to update the information.

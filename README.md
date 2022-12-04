
# Blog App

This is a simple blog app built using Flask and SQLAlchemy. It allows users to create and view posts, as well as edit and delete them.

## Requirements

-   Flask
-   SQLAlchemy

## Usage

Navigate to the main directory and run `mkdir static/imgs` to create the image directory. This folder can be configured in `cms.py` if you'd like to store images elsewhere.

To run the app, simply run `python app.py` in your terminal. The app will be available at `http://127.0.0.1:8000`.

## Features

-   Create, view, edit, and delete posts
-   View all posts in chronological order
-   Image uploads for posts
-   Admin page to manage all posts

## File structure

- app.py (main Flask app file)
- models.py (database models)
- static/
	 - imgs/ (image uploads) <-- you need to create this folder
- templates/
	 - admin.html (admin page template)
	 - create.html (create post template)
	 - edit.html (edit post template)
	 - error.html (error message template)
	 - index.html (homepage template)
	 - post.html (individual post template)` 

## Contributing

Pull requests are welcome. I'm no web designer :)

## License

This project is licensed under the MIT License.
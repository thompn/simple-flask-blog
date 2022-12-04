from flask import Flask, render_template, request, redirect, url_for
from models import Post
import os
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/imgs'


@app.route('/')
def index():
    posts = Post.all()
    return render_template('index.html', posts=posts)

@app.route('/post/<int:id>')
def post(id):
    post = Post.get(id)
    return render_template('post.html', post=post)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        image = request.files['image']

        # Validate the input fields
        if not title:
            return render_template('error.html', error='Please enter a title for the post.')
        # elif not image:
        #     return render_template('error.html', error='Please select an image to include with your post.')

        # Save the image to a temporary location
        image_name = secure_filename(image.filename)
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], image_name))

        # Create the post
        Post.create(title=title, body=body, image=image_name)
        return redirect('/')
    else:
        return render_template('create.html')


@app.route('/admin')
def admin():
    posts = Post.all()
    return render_template('admin.html', posts=posts)

@app.route('/delete_all_posts', methods=['POST'])
def delete_all_posts():
    Post.delete_all()
    return redirect(url_for('admin'))

@app.route('/delete_selected_posts', methods=['POST'])
def delete_selected_posts():
    post_ids = request.form.getlist('post_ids')
    for post_id in post_ids:
        post = Post.get(post_id)
        post.delete()
    return redirect(url_for('admin'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    post = Post.get(id)
    if request.method == 'POST':
        post.title = request.form['title']
        post.body = request.form['body']
        post.save()
        return redirect('/')
    else:
        return render_template('edit.html', post=post)

@app.route('/delete/<int:id>', methods=['POST', 'GET'])
def delete(id):
    post = Post.get(id)
    post.delete()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(port=8000, debug=True)

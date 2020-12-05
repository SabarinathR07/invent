from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False, default='N/A')
    ptype = db.Column(db.String(20), nullable=False, default='N/A')
    pcor = db.Column(db.String(20), nullable=False, default='N/A')
    pric = db.Column(db.String(20), nullable=False, default='N/A')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return 'Blog post ' + str(self.id)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts', methods=['GET', 'POST'])
def posts():

    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        post_ptype = request.form['ptype']
        post_pcor = request.form['pcor']
        post_pric = request.form['pric']
        new_post = BlogPost(title=post_title, content=post_content, ptype=post_ptype, pcor=post_pcor, pric=post_pric)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
    else:
        all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
        return render_template('posts.html', posts=all_posts)

@app.route('/posts/delete/<int:id>')
def delete(id):
    post = BlogPost.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/posts')

@app.route('/posts/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    
    post = BlogPost.query.get_or_404(id)

    if request.method == 'POST':
        post.title = request.form['title']
        post.ptype = request.form['ptype']
        post.pcor = request.form['pcor']
        post.pric = request.form['pric']
        db.session.commit()
        return redirect('/posts')
    else:
        return render_template('edit.html', post=post)


@app.route('/posts/move/<int:id>', methods=['GET', 'POST'])
def move(id):
    
    post = BlogPost.query.get_or_404(id)

    if request.method == 'POST':
        post.author = request.form['author']
        post.content = request.form['content']
        db.session.commit()
        return redirect('/posts')
    else:
        return render_template('move.html', post=post)




@app.route('/posts/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        post.title = request.form['title']
        post.ptype = request.form['ptype']
        post.pcor = request.form['pcor']
        post.pric = request.form['pric']
        post.content = request.form['content']
        new_post = BlogPost(title=post_title, content=post_content, ptype=post_ptype, pcor=post_pcor, pric=post_pric)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
    else:
        return render_template('new_post.html')

class BlogPost2(db.Model):
    lid = db.Column(db.Integer, primary_key=True)
    mid = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    address = db.Column(db.Text, nullable=False)
    qty = db.Column(db.String(20), nullable=False, default='N/A')
    timetamp = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)

    def __repr__(self):
        return 'Blog post ' + str(self.lid)

@app.route('/postsz', methods=['GET', 'POST'])
def postsz():

    if request.method == 'POST':
        post_mid = request.form['mid']
        post_title = request.form['title']
        post_address = request.form['address']
        post_qty = request.form['qty']
        ptime=datetime.utcnow()
        new_post = BlogPost2(mid=post_mid,title=post_title, address=post_address, qty=post_qty, timetamp=ptime)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/postsz')
    else:
        all_posts = BlogPost2.query.order_by(BlogPost2.timetamp).all()
        return render_template('postsz.html', postsz=all_posts)


@app.route('/postsz/edit/<int:lid>', methods=['GET', 'POST'])
def editz(lid):
    
    post = BlogPost2.query.get_or_404(lid)

    if request.method == 'POST':
        post.mid = request.form['mid']
        post.title = request.form['title']
        post.address = request.form['address']
        post.qty = request.form['qty']
        db.session.commit()
        return redirect('/postsz')
    else:
        return render_template('editz.html', post=post)



@app.route('/postsz/delete/<int:lid>')
def deletez(lid):
    post = BlogPost2.query.get_or_404(lid)
    db.session.delete(post)
    db.session.commit()
    return redirect('/postsz')


@app.route('/postsz/new', methods=['GET', 'POST'])
def new_postz():
    if request.method == 'POST':
        post.mid = request.form['mid']
        post.title = request.form['title']
        post.address = request.form['address']
        post.qty = request.form['qty']
        new_postz = BlogPost2(mid=post_mid,title=post_title, address=post_address, qty=post_qty)
        db.session.add(new_postz)
        db.session.commit()
        return redirect('/postsz')
    else:
        return render_template('new_postz.html')




if __name__ == "__main__":
    app.run(debug=True)

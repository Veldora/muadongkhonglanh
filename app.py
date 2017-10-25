from flask import Flask, render_template,request
import mlab
from mongoengine import *
from faker import Faker


app = Flask(__name__)

mlab.connect()

class Girl(Document):
    name=StringField()
    image=StringField()
    describtion=StringField()
    rating=FloatField()

# f=Faker()
# for _ in range(20):
#     g=Girl(name=f.name(),image="http://via.placeholder.com/500x300",describtion="f.text",rating=4.1)
#     g.save()
@app.route('/')
def index2():
    return render_template('homepage.html')

@app.route('/project')
def ex23():
    return render_template("index.html")

@app.route('/include')
def include():
    return render_template("include_ex.html")

@app.route('/clgt')
def index():
    # data=[
    #     {
    #         'name':'có cái l ấy, believe people vcl :))',
    #         'image':'https://pbs.twimg.com/media/BvYztFCIMAAull8.png'
    #     },
    #     {
    #         'name':'Mùa đông nay vẫn lạnh nhé',
    #         'image':'http://www.cocoonetmoi.fr/wp-content/uploads/2013/03/Personnages-celebres-Troll-face-Troll-face-me-gusta-29215.jpg'
    #     },
    #     {
    #         'name':'ahihi đợi 20 năm nữa đi!!!',
    #         'image':'http://i3.kym-cdn.com/photos/images/newsfeed/000/247/207/813.gif'
    #     }
    # ]
    girl_list=Girl.objects()
    return render_template('girls.html',girls=girl_list)



@app.route('/<int:id>', methods=['POST'])
def delete_entry(id):
    form=request.form
    name=form['girlname']
    girl=Girl(name=name)
    Girl.objects(name=name).delete()
    return "Deleted"

@app.route('/addgirl', methods=['GET','POST'])
def addgirl():
    if request.method=="GET":
        return render_template('addgirl.html')
    elif request.method=="POST":
        form=request.form
        name=form['name']
        image=form['image']
        describtion=form['describtion']
        girl=Girl(name=name,describtion=describtion,image=image,rating=1.2)
        girl.save()
        return "Added"

@app.route('/admin')
def admin():
    girl_list=Girl.objects()
    return render_template('admin.html',girls=girl_list)

@app.route('/list')
def list_demo():
    return render_template("girls_list.html",names=['huy','tuan anh','quan','truong','con lai'])

@app.route('/dict')
def dict_demo():
    d={
        'name':'có cái l ấy, believe people vcl :))',
        'image':'https://pbs.twimg.com/media/BvYztFCIMAAull8.png'
    }
    return render_template('whatever.html',girl=d)

@app.route('/css-demo')
def css_demo():
    return render_template("css_demo.html")
#google resizer : xem giao dien web tren cac thiet bi
#col-md-6   chia cot html

if __name__ == '__main__':
  app.run(debug=True)

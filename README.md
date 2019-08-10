# Item Catalog project
**by ٌMohamed Bahaa**

https://github.com/mohamed-bahaa/catalog

Local:
$ books-conf-1917381-190723-ok

Remote:
https://github.com/pedroalvesfilho/catalog_books

Switching remote URLs:
```
$ git remote set-url origin https://github.com/pedroalvesfilho/catalog_books
$ git remote -v
```
The next time you git fetch, git pull, or git push to the remote repository, 
you'll be asked for your GitHub username and password.

https://help.github.com/en/articles/changing-a-remotes-url

---


## Project  Description:

This is the 2nd project for the Udacity Full Stack Nanodegree , called " Item Catalog"
The Item Catalog project consists of developing an application that provides a list of items within 
a variety of categories, as well as provide a user registration and authentication system. 
This project uses  data storage to create a RESTful web app that allows users to perform 
CRUD - Create, Read, Update, and Delete operations.

A user does not need to be logged in in order to read the categories or items uploaded. However, users who 
created an item are the only users allowed to update or delete the item that they created.

### The Computer Books Catalog app  represent the Item Catalog 
## Project contents

Within the download you'll find the following files:

```
Item-Catalog.zip/
├── static/
│   └── css/
│       └──styles.css
│
│
├── templates/
│   └── addBook.html
│   └── base.html
│   └── book.html
│   └── categories.html
│   └── category.html
│   └── deleteBook.html
│   └── editBook.html
│   └── login.html
│   
├── app.py
├── books_catalog.db
├── client_secrets.json
├── database_setup.py
├── fill_database.py
└── README.md
```
## Requirements

-   [VirtualBox](https://www.virtualbox.org/)
-   [Vagrant](https://www.vagrantup.com/)
-   [Python 2.7](https://www.python.org/)](https://www.python.org/)
-   [sqlalchemy_utils](http://initd.org/psycopg/docs/install.html)  `pip install sqlalchemy_utils`(if you want to run the  ``fill_database.py``)
-   [Bash terminal(for windows machine)](https://git-scm.com/downloads)

## Installation

1.  Install Python2.7 , VirtualBox and Vagrant
    
2.  Clone or download the Vagrant VM configuration file from  [fullstack-nanodegree-vm repository](https://github.com/udacity/fullstack-nanodegree-vm)
    
3.  Clone Or download this repository to your desktop , Unzip and  Paste all the files  from this project  
`Item-Catalog` into the ```fullstack-nanodegree-vm-master\vagrant\catalog ``` sub-directory
    


## Steps to run this project

1.  Open terminal and go to the folder where you saved the fullstack repository then :  `cd vagrant`.
2.  Launch Vagrant to set up the virtual machine and then log into the virtual machine.:  `vagrant up`  `vagrant ssh`
    
3. Then move inside the catalog folder:
`cd /vagrant/catalog`
    
4. Then run the application:
`python app.py`

5. finally Access and test your application by visiting  [http://localhost:8000](http://localhost:8000/).:
`http://localhost:8000/`

## The expected program output is as the following : 

http://localhost:8000/ or http://localhost:8000/catalog 
- Returns catalog page with all categories and recently added books without login
<img src="screenshot/catalog.jpg" width="800">
 
 
`/catalog/<int:catalog_id>`
`/catalog/<int:catalog_id>/books`
http://localhost:8000/catalog/1/books
- Returns number of  books in  category 
<img src="screenshot/categories.jpg" width="800">
  
  
`/catalog/<int:catalog_id>/books/<int:book_id>`
http://localhost:8000/catalog/3/books/7
- show a Book information
<img src="screenshot/book.jpg" width="800">


http://localhost:8000/login
- login with google api
<img src="screenshot/login.jpg" width="800">
<img src="screenshot/login2.jpg" width="800">


http://localhost:8000/catalog/add
- Allows user to add a new book
<img src="screenshot/add.jpg" width="800">


` /catalog/<int:catalog_id>/books/<int:book_id>/edit`
- Allows user to edit  his book
<img src="screenshot/edit.jpg" width="800">


`/catalog/<int:catalog_id>/books/<int:book_id>/delete`
- Allows user to delete his book
<img src="screenshot/delete.jpg" width="800">

## JSON Endpoints
http://localhost:8000/catalog/JSON
- return categories information
<img src="screenshot/catalogJSON.jpg" width="800">


`/catalog/<int:catalog_id>/JSON`
http://localhost:8000/catalog/3/JSON
- return category books information
<img src="screenshot/categoryBooksJSON.jpg" width="800">

`/catalog/<int:catalog_id>/books/JSON`
http://localhost:8000/catalog/2/books/2/JSON
- return a book detail
<img src="screenshot/bookJSON.jpg" width="800">

## Licence

The MIT License ([MIT](https://choosealicense.com/licenses/mit/#))
Copyright (c) [2019] [Mohamed Bahaa]

When you start your app by running `flask run`
the `if __name__ == '__main__':` block gets skipped.
If you don't want to skip it, run with `python <script.py>`.
When running `flask run`:
Write your secret  after `app = Flask(__name__)`
```
     app = Flask(__name__)
     app.secret_key = 'super_secret_key'
```

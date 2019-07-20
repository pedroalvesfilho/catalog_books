from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy_utils import database_exists, drop_database, create_database

from database_setup import Category, Book, User, Base

engine = create_engine('sqlite:///books_catalog.db')

# Clear database
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

# Create  user
user1 = User(name="Mohamed Bahaa", email="mohamed.bahaa1980@gmail.com",
             picture='https://unsplash.com/photos/eMP4sYPJ9x0')
session.add(user1)
session.commit()

# books for Machine Learning category
category1 = Category(name="Machine Learning", user_id=1)

session.add(category1)
session.commit()

book1 = Book(
             name="Understanding Machine Learning",
             user_id=1,
             description="""Machine learning is one of the fastest growing areas of computer science, 
			 with far-reaching applications. The aim of this textbook is to introduce machine learning, 
			 and the algorithmic paradigms it offers, in a principled way. The book provides an extensive 
			 theoretical account of the fundamental ideas underlying machine learning and the mathematical 
			 derivations that transform these principles into practical algorithms. Following a presentation 
			 of the basics of the field, the book covers a wide array of central topics that have not been 
			 addressed by previous textbooks. These include a discussion of the computational complexity of 
			 learning and the concepts of convexity and stability; important algorithmic paradigms including 
			 stochastic gradient descent, neural networks, and structured output learning; and emerging 
			 theoretical concepts such as the PAC-Bayes approach and compression-based bounds. Designed for an
			 advanced undergraduate or beginning graduate course, the text makes the fundamentals and algorithms
			 of machine learning accessible to students and non-expert readers in statistics, computer science,
			 mathematics, and engineering. """,
             category=category1)

session.add(book1)
session.commit()


# books for General computer knowledge category
category2 = Category(name="General computer knowledge", user_id=1)

session.add(category2)
session.commit()

book1 = Book(
             name="How Computers Work",
             user_id=1,
             description="""How Computers Work by Ron White is a great
             overview of how everything in your computer works.
             The book has fantastic illustrations and i
             s not as overwhelming as some other computer books.""",
             category=category2)

session.add(book1)
session.commit()

book2 = Book(
             name="Upgrading and Repairing PCs ",
             user_id=1,
             description="""Upgrading and Repairing PCs by Scott Mueller
              is one of our favorite books that is an in-depth overview
              of computers and computer hardware. This book goes into
              lots of details and is a long, but interesting read.""",
             category=category2)

session.add(book2)
session.commit()

book3 = Book(
             name="The Elements of Computing Systems",
             user_id=1,
             description="""The Elements of Computing Systems: Building
              a Modern Computer from First Principles by Noam Nisan
              gives an in-depth overview of how computers work and show
              you how a computer can be built from scratch.""",
             category=category2)

session.add(book3)
session.commit()

# books for Hacking and computer security category
category3 = Category(name="Hacking and computer security", user_id=1)

session.add(category3)
session.commit()

book1 = Book(
             name="Ghost in the Wires",
             user_id=1,
             description=""" ghost in the Wires by Kevin Mitnick is a
              book covering one of the greatest and well known hackers
              in history. The book covers Kevin's thrilling true story
              of illegally accessing computers and networks.Hacking:
              The Art of Exploration by Jon Erickson is a book that goes
              into detail about hacking is the art of problem solving
              and also gives examples of hacking techniques.""",
             category=category3)

session.add(book1)
session.commit()

book2 = Book(
             name="Hacking Exposed",
             user_id=1,
             description="""Hacking Exposed by is a great series of
              books that covers all types of computer security related
              topics.""",
             category=category3)

session.add(book2)
session.commit()

book3 = Book(
             name="Practical Malware Analysis",
             user_id=1,
             description="""Practical Malware Analysis by Michael
              Sikorksi and Andrew Honig is a frequently cited book
              in this roundup, and for good reason. It s a go to guide
              for many in learning both basic and advanced malware
              analysis and dissection techniques""",
             category=category3)
session.add(book3)
session.commit()

# books for Computer Programming category
category4 = Category(name="Computer Programming", user_id=1)

session.add(category4)
session.commit()

book1 = Book(
             name="The Pragmatic Programmer",
             user_id=1,
             description="""The Pragmatic Programmer: From Journeyman
              to Master by David Thomas that teaches all of the great
              techniques used by master programmers.""",
             category=category4)

session.add(book1)
session.commit()

book2 = Book(
             name="Design Patterns",
             user_id=1,
             description="""Design Patterns: Elements of Reusable
              Object-Oriented Software by the Gang of Four is a
              great source of on object-oriented design theory.""",
             category=category4)

session.add(book2)
session.commit()

book3 = Book(
             name="Introduction to Algorithms",
             user_id=1,
             description="""Introduction to Algorithms by Thomas Cormen
              is a more advanced programming book with an encyclopedia
              type listing of vEB trees, multithreaded algorithms,
              dynamic programming, edge-base flow, and other algorithms
              you are likely to encounter while programming.""",
             category=category4)

session.add(book3)
session.commit()

# books for Web design category
category5 = Category(name="Web design", user_id=1)

session.add(category5)
session.commit()


##############
# books for Artificial Intelligence category
category6 = Category(name="Artificial Intelligence", user_id=1)

session.add(category6)
session.commit()

book1 = Book(
             name="Artificial Intelligence in IoT",
             user_id=1,
             description=""" This book provides an insight into IoT intelligence in terms of applications and algorithmic 
			 challenges. The book is dedicated to addressing the major challenges in realizing the artificial intelligence 
			 in IoT-based applications including challenges that vary from cost and energy efficiency to availability to 
			 service quality in multidisciplinary fashion. The aim of this book is hence to focus on both the algorithmic 
			 and practical parts of the artificial intelligence approaches in IoT applications that are enabled and supported
			 by wireless sensor networks and cellular networks.""",
             category=category6)

session.add(book1)
session.commit()



categories = session.query(Category).all()
for category in categories:
    print ("Category: " + category.name)

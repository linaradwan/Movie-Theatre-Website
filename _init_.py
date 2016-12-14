from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

################################## Customer ##################################

@app.route("/")
def main():
    return render_template('MainWindow.html')
@app.route("/Customer")
def Customer():
    return render_template('index.html')

@app.route("/StaffSignIn")
def StaffSignIn():
    return render_template('StaffSignIn.html')

################################## Staff Adding ##################################

@app.route("/addCustomer")
def addCustomer():
    return render_template('addCustomer.html')   

@app.route('/addCustomerSubmit', methods=["POST"])
def addCustomerSubmit():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()

    insert_stmt = (
        "INSERT INTO Customer (idCustomer, FirstName, LastName, EmailAddress, Sex) "
        "VALUES (%s, %s, %s,%s,%s)"
    )

    data = (request.form['idCustomer'], request.form['FirstName'], request.form['LastName'],request.form['EmailAddress'],request.form['Sex'])
    cursor.execute(insert_stmt, data)
    cnx.commit()
    cnx.close()
    return render_template('SuccessAdd.html')


@app.route("/addMovie")
def addMovie():
    return render_template('addMovie.html')

@app.route('/addMovieSubmit', methods=["POST"])
def addMovieSubmit():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()

    insert_stmt = (
        "INSERT INTO Movie (idMovie, MovieName, MovieYear) "
        "VALUES (%s, %s, %s)"
    )

    data = (request.form['idMovie'], request.form['MovieName'], request.form['MovieYear'])
    cursor.execute(insert_stmt, data)
    cnx.commit()
    cnx.close()
    return render_template('SuccessAdd.html')

@app.route("/addTheatreRoom")
def addTheatreRoom():
    return render_template('addRooms.html')   

@app.route('/addTheatreRoomSubmit', methods=["POST"])
def addTheatreRoomSubmit():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()

    insert_stmt = (
        "INSERT INTO TheatreRoom (RoomNumber, Capacity) "
        "VALUES (%s, %s)"
    )

    data = (request.form['RoomNumber'], request.form['Capacity'])
    cursor.execute(insert_stmt, data)
    cnx.commit()
    cnx.close()
    return render_template('SuccessAdd.html')

@app.route("/addShowing")
def addShowing():
    return render_template('addShowing.html')


@app.route("/addShowingSubmit", methods=["POST"])
def addShowingSubmit():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()

    insert_stmt = (
        "INSERT INTO Showing (idShowing, ShowingDateTime, Movie_idMovie, TheatreRoom_RoomNumber, TicketPrice) "
        "VALUES (%s, %s, %s, %s, %s)"
    )

    data = (request.form['idShowing'], request.form['ShowingDateTime'], request.form['Movie_idMovie'], request.form['TheatreRoom_RoomNumber'], request.form['TicketPrice'])
    cursor.execute(insert_stmt, data)
    cnx.commit()
    cnx.close()
    return render_template('SuccessAdd.html')

@app.route("/addGenre")
def addGenre():
	    return render_template('addGenre.html')


@app.route("/addGenreSubmit", methods=["POST"])
def addGenreSubmit():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()

    insert_stmt = (
        "INSERT INTO Genre (Genre, Movie_idMovie) "
        "VALUES (%s, %s)"
    )

    data = (request.form['Genre'], request.form['Movie_idMovie'])
    cursor.execute(insert_stmt, data)
    cnx.commit()
    cnx.close()
    return render_template('SSuccessAdd.html')




################################## Staff Deleting ##################################


@app.route("/deleteCustomer")
def deleteCustomer():
    return render_template('deleteCustomer.html')


@app.route("/deleteCustomerSubmit", methods=["POST"])
def deleteCustomerSubmit():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()

    idCustomer=request.form['idCustomer']
    query=("Delete from Attend where Customer_idCustomer=%s")
    cursor.execute(query,(idCustomer,))
    query=("Delete from Customer where idCustomer=%s")
    cursor.execute(query,(idCustomer,))
 
    cnx.commit()
    cnx.close()
    return render_template('SuccessDelete.html')    

@app.route("/deleteMovie")
def deleteMovie():
    return render_template('deleteMovie.html')

@app.route('/deleteMovieSubmit', methods=["POST"])
def deleteMovieSubmit():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    idMovie=request.form['idMovie']

    query=("Delete from Genre where Movie_idMovie=%s")
    cursor.execute(query,(idMovie,)) 
    query=("Delete from Showing where Movie_idMovie=%s")
    cursor.execute(query,(idMovie,))

    query=("Delete from Movie where idMovie=%s")
    cursor.execute(query,(idMovie,))
  

    cnx.commit()
    cnx.close()
    return render_template('SuccessDelete.html')


@app.route("/deleteRooms")
def deleteRooms():
    return render_template('deleteRooms.html')


@app.route("/deleteRoomsSubmit", methods=["POST"])
def deleteRoomsSubmit():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    RoomNumber=request.form['RoomNumber']

    query=("Delete from Showing where TheatreRoom_RoomNumber=%s")
    cursor.execute(query,(RoomNumber,))
    
    query=("Delete from TheatreRoom where RoomNumber=%s")
    cursor.execute(query,(RoomNumber,))


    cnx.commit()
    cnx.close()
    return render_template('SuccessDelete.html')    

@app.route("/deleteShowing")
def deleteShowing():
    return render_template('deleteShowing.html')


@app.route("/deleteShowingSubmit", methods=["POST"])
def deleteShowingSubmit():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    idShowing=request.form['idShowing']
 
    query=("Delete from Attend where Showing_idShowing=%s")
    cursor.execute(query,(idShowing,))

    query=("Delete from Showing where idShowing=%s")
    cursor.execute(query,(idShowing,))


    cnx.commit()
    cnx.close()
    return render_template('SuccessDelete.html')

@app.route("/deleteGenre")
def deleteGenre():
    return render_template('deleteGenre.html')

@app.route("/deleteGenreSubmit", methods=["POST"])
def deleteGenreSubmit():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    Movie_idMovie=request.form['Movie_idMovie']
    query=("Delete from  Genre where Movie_idMovie=%s")
    cursor.execute(query,(Movie_idMovie,))
    cnx.commit()
    cnx.close()
    return render_template('SuccessDelete.html')


################################## Staff Modifying ##################################


@app.route("/modifyCustomer")
def modifyCustomer():
    return render_template('modifyCustomer.html')


@app.route("/modifyCustomerSubmit", methods=["POST"])
def modifyCustomerSubmit():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    CustomerID=request.form['CustomerID']
    firstname=request.form['firstname']
    lastname=request.form['lastname']
    sex=request.form['sex']
    email=request.form['email']
    query=("update Customer set FirstName=%s,LastName=%s,Sex=%s,EmailAddress=%s where idCustomer=%s")
    data=(firstname,lastname,sex,email,CustomerID)

    cursor.execute(query, data)

    cnx.commit()
    cnx.close()
    return render_template('SuccessUpdate.html')


@app.route("/modifyMovie")
def modifyMovie():
    return render_template('modifyMovie.html')

@app.route('/modifyMovieSubmit', methods=["POST"])
def modifyMovieSubmit():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    idMovie=request.form['idMovie']
    MovieName=request.form['MovieName']
    MovieYear=request.form['MovieYear']
    query=("update Movie set MovieName=%s,MovieYear=%s where idMovie=%s")

    data=(MovieName,MovieYear,idMovie)

    cursor.execute(query, data)
    cnx.commit()
    cnx.close()
    return render_template('SuccessUpdate.html')

@app.route("/modifyRooms")
def modifyRooms():
    return render_template('modifyRooms.html')

@app.route("/modifyRoomSubmit", methods=["POST"])
def modifyRoomSubmit():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    RoomNumber=request.form['RoomNumber']
    Capacity=request.form['Capacity']
    query=("update TheatreRoom set Capacity=%s where RoomNumber=%s")

    data=(Capacity,RoomNumber)
    cursor.execute(query, data)
    cnx.commit()
    cnx.close()
    return render_template('SuccessUpdate.html')    

@app.route("/modifyShowing")
def modifyShowing():
    return render_template('modifyShowing.html')

@app.route("/modifyShowingSubmit", methods=["POST"])
def modifyShowingSubmit():  
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    idShowing=request.form['idShowing']
    ShowingDateTime=request.form['ShowingDateTime']
    TheatreRoom_RoomNumber=request.form['TheatreRoom_RoomNumber']
    Movie_idMovie = request.form['Movie_idMovie']
    TicketPrice = request.form['TicketPrice']
    query=("update Showing set Movie_idMovie=%s,ShowingDateTime=%s,TheatreRoom_RoomNumber=%s,TicketPrice=%s where idShowing=%s")

    data=(Movie_idMovie,ShowingDateTime,TheatreRoom_RoomNumber,TicketPrice,idShowing)
    cursor.execute(query, data)    
    cnx.commit()
    cnx.close()
    return render_template('SuccessUpdate.html')




################################## Staff ListAll ##################################

@app.route('/allMovie')
def allMovie():
    
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("select * from Movie order by MovieName")
    cursor.execute(query)
    movie=cursor.fetchall()
    cnx.close()
    return render_template('allMovie.html',movies=movie)

@app.route('/allCustomer')
def allCustomer():
    
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("select * from Customer order by LastName")
    cursor.execute(query)
    customer=cursor.fetchall()
    cnx.close()
    return render_template('allCustomer.html',Customers=customer)


@app.route('/allShowing')
def allShowing():
    
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("select * from Showing order by ShowingDateTime")
    cursor.execute(query)
    Showing=cursor.fetchall()
    cnx.close()
    return render_template('allShowing.html',Showing=Showing)

@app.route('/allRooms')
def allRooms():
    
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("select * from TheatreRoom")
    cursor.execute(query)
    Rooms=cursor.fetchall()
    cnx.close()
    return render_template('allRooms.html',Rooms=Rooms)

@app.route('/allAttend')
def allAttend():
    
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("select * from Attend order by Rating")
    cursor.execute(query)
    Attend=cursor.fetchall()
    cnx.close()
    return render_template('allAttend.html',Attend=Attend)

@app.route('/allGenre')
def allGenre():
    
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("select Genre,MovieName from Genre,Movie where Movie_idMovie=idMovie order by Genre")
    cursor.execute(query)
    Genre=cursor.fetchall()
    cnx.close()
    return render_template('allGenre.html',Genre=Genre)



################################## Customer Front End ##################################

@app.route('/BuyTicket')
def BuyTicket():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()
	query = ("select MovieName,idShowing,ShowingDateTime from Showing, Movie where Movie_idMovie=idMovie order by ShowingDateTime")
	cursor.execute(query)
	movies=cursor.fetchall()
	cnx.close()
	return render_template('BuyTicket.html',movies=movies)

@app.route('/BuyTicketSubmit', methods=["POST"])
def BuyTicketSubmits():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()

   
    movieselect=request.form.get('movie')
    movieSelectSplit= movieselect.split(",")
    idCustomer=request.form['idCustomer']
    movie=movieSelectSplit[1]
    insert_stmt=("insert into Attend (Customer_idCustomer,Showing_idShowing) values(%s,%s)" )
    data=(idCustomer,movie)
    cursor.execute(insert_stmt, data)
    #cursor.execute(insert_stmt)
  
    cnx.commit()
    cnx.close()
    return render_template('index.html')

@app.route('/RateMovie')
def RateMovie():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()
	query = ("select MovieName,idShowing,ShowingDateTime from Showing, Movie where Movie_idMovie=idMovie order by ShowingDateTime")
	cursor.execute(query)
	movies=cursor.fetchall()
	cnx.close()
	return render_template('RateMovie.html',movies=movies)

@app.route('/RateMovieSubmit', methods=["POST"])
def RateMovieSubmit():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()

    movieselect=request.form.get('movie')
    movieSelectSplit= movieselect.split(",")
    rating=request.form.get('rating')
    idCustomer=request.form['idCustomer']
    data=(rating,idCustomer,movieSelectSplit[1])

    insert_stmt = ("update Attend set Rating=%s where Customer_idCustomer=%s and Showing_idShowing= %s") 
    cursor.execute(insert_stmt,data)

    cnx.commit()
    cnx.close()
    return render_template('index.html')



@app.route("/SearchShowings")
def SearchShowings():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("select distinct Genre from Genre")
    cursor.execute(query)
    genre=cursor.fetchall()
    query =("select distinct ShowingDateTime from Showing order by ShowingDateTime")
    cursor.execute(query)
    Date=cursor.fetchall()
    cnx.commit()
    cnx.close()
    return render_template('SearchMovies.html',genre=genre, Date=Date)


@app.route("/SearchShowingsSubmit" , methods=["POST"])
def SearchShowingsSubmit():

    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    MovieName= request.form['MovieName']
    GenreSelect=request.form.get('Genre')
    StartDate=request.form.get('StartDate')
    EndDate=request.form.get('EndDate')

    if MovieName is not None and len(MovieName) is not 0:
        query=("select MovieName, showingDateTime, TheatreRoom_RoomNumber,TicketPrice,Capacity from Movie,Showing, TheatreRoom where MovieName='"+ MovieName+ "' and showingDateTime >'"+StartDate+"'and showingDateTime < '"+EndDate+"'  and Movie.idMovie=Showing.Movie_idMovie and TheatreRoom_RoomNumber=RoomNumber  order by showingDateTime ")

        #query=("select MovieName, showingDateTime, TheatreRoom_RoomNumber,TicketPrice,Capacity-count(Customer_idCustomer) from Movie,Showing,Attend, TheatreRoom where MovieName='"+ MovieName+ "' and showingDateTime >'"+StartDate+"'and showingDateTime < '"+EndDate+"'  and Movie.idMovie=Showing.Movie_idMovie and TheatreRoom_RoomNumber=RoomNumber and Showing_idShowing = idShowing ")

    else: 
        query=("select MovieName,ShowingDateTime, RoomNumber, TicketPrice,Capacity  from Movie, TheatreRoom, Showing, Genre where Movie.idMovie=Genre.Movie_idMovie and Showing.TheatreRoom_RoomNumber = TheatreRoom.RoomNumber and Showing.Movie_idMovie=Movie.idMovie and Genre='"+GenreSelect+"' order by ShowingDateTime")

    cursor.execute(query)
    Date=cursor.fetchall()


    cnx.commit()
    cnx.close()
 
    return render_template('SearchMoviesSubmitted.html',Date=Date)









@app.route("/SignIn")
def SignIn():
    return render_template('SignIn.html')


@app.route("/SignInSubmit", methods=["POST"])
def SignInSubmit():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    idCustomer=request.form['idCustomer']
    cursor = cnx.cursor()
    query = ("select * from Customer where idCustomer=%s")
    cursor.execute(query,(idCustomer,))
    userinfo=cursor.fetchall()
    query = ("select MovieName,Rating from Attend,Movie,Showing where Customer_idCustomer= %s and Showing_idShowing=idShowing and Movie_idMovie=idMovie")
    cursor.execute(query,(idCustomer,))
    movieattend=cursor.fetchall()
    cnx.close()
    return render_template('Profile.html',userinfo=userinfo,movieattend=movieattend)


@app.route("/sqlInjection")
def sqlInjection():
    return render_template('sqlInjection.html')


@app.route("/sqlInjectionSubmit", methods=["POST"])
def sqlInjectionSubmit():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    idCustomer=request.form['idCustomer']
    cursor = cnx.cursor()
    query = ("select * from Customer where idCustomer= '' OR '1' ='1' ")
    cursor.execute(query)
    userinfo=cursor.fetchall()
    query = ("select MovieName,Rating from Attend,Movie,Showing where Customer_idCustomer="+idCustomer+" and Showing_idShowing=idShowing and Movie_idMovie=idMovie")
    cursor.execute(query)
    movieattend=cursor.fetchall()
    cnx.close()
    return str(userinfo) 
   
   #return render_template('Profile.html',userinfo=userinfo,movieattend=movieattend)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)



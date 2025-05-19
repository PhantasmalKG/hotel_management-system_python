#Create a Hotel class for the data to be organized
class Hotel:
    sortParam = 'name'

    def __init__(self) -> None:
        self.name = ''
        self.roomAvl = 0
        self.location = ''
        self.rating = int
        self.pricePr = 0

    def __lt__(self, other):
        getattr(self, Hotel.sortParam) < getattr(other, Hotel.sortParam)

    @classmethod
    def sortByName(cls):
        cls.sortParam = 'name'

    @classmethod
    def sortByRate(cls):
        cls.sortParam = 'rating'

    @classmethod
    def sortByRoomAvailable(cls):
        cls.sortParam = 'roomAvl'

    def __repr__(self) -> str:
        return "PRHOTELS DATA:\nHotelName:{}\tRoom Available:{}\tLocation:{}\tRating:{}\tPrice Per Room:{}".format(
            self.name, self.roomAvl, self.location, self.rating, self.pricePr)


class User:
    def __init__(self) -> None:
        self.userName = ''
        self.userID = 0
        self.cost = 0

    def __repr__(self) -> str:
        return "UserName:{}\tUserID:{}\tBooking Cost:{}".format(self.userName, self.userID, self.cost)


def PrintHotelData(hotels):
    for hotel in hotels:
        print(hotel)


def SortHotelByName(hotels):
    for hotel in hotels:
        print("SORT BY NAME:")
        Hotel.sortByName()

        Hotel.sortByRoomAvailable()
        hotels.sort()

        PrintHotelData(hotels)
        print()


def SortByRating(hotels):
    print("SORT BY RATING:")

    Hotel.sortByRate()
    hotels.sort()

    PrintHotelData(hotels)
    print()


def PrintHotelByCity(s, hotels):
    print("HOTELS FOR {} LOCATION ARE:".format(s))
    hotelsByLoc = [h for h in hotels if h.location == s]

    PrintHotelData(hotelsByLoc)
    print()


def SortByRoomAvailable(hotels):
    print("SORT BY ROOM AVAILABLE:")
    Hotel.sortByRoomAvailable()
    hotels.sort()
    PrintHotelData(hotels)
    print()


def PrintUserData(userName, userID, bookingCost, hotels):
    users = []

    for x in range(3):
        u = User()
        u.uName = userName[x]
        u.uID = userID[x]
        u.cost = bookingCost[x]
        users.append(u)

    for y in range(len(users)):
        print(users[y], "\tHotel name:", hotels[y].userName)


def HotelManagement(userName, userId, hotelName, bookingCost, rooms, locations, ratings, prices):
    hotels = []

    for c in range(3):
        h = Hotel()
        h.name = hotelName[c]
        h.roomAvl = rooms[c]
        h.location = locations[c]
        h.rating = ratings[c]
        h.pricePr = prices[c]
        hotels.append(h)

    print()

    PrintHotelData(hotels)
    SortHotelByName(hotels)
    SortByRating(hotels)
    PrintHotelByCity("Bangalore", hotels)
    SortByRoomAvailable(hotels)
    PrintUserData(userName, userId, bookingCost, hotels)


if __name__ == '__main__':
    userName = ["U1", "U2", "U3"]
    userId = [2, 3, 4]
    hotelName = ["H1", "H2", "H3"]
    bookingCost = [1000, 1200, 1100]
    rooms = [4, 5, 6]
    locations = ["Bangalore",
                 "Bangalore",
                 "Mumbai"]
    ratings = [5, 5, 3]
    prices = [100, 200, 100]

    HotelManagement(userName, userId,
                    hotelName, bookingCost,
                    rooms, locations,
                    ratings, prices)

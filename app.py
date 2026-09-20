from flask import Flask, render_template, request

app = Flask(__name__)


# =========================
# TOURIST PLACES
# =========================

PLACES = {

    "Chennai": [
        {
            "name": "Marina Beach",
            "location": "Chennai",
            "type": "Beach"
        },
        {
            "name": "Kapaleeshwarar Temple",
            "location": "Mylapore, Chennai",
            "type": "Temple"
        },
        {
            "name": "Fort St. George",
            "location": "Chennai",
            "type": "Historical"
        },
        {
            "name": "Government Museum",
            "location": "Egmore, Chennai",
            "type": "Museum"
        }
    ],

    "Coimbatore": [
        {
            "name": "Marudamalai Temple",
            "location": "Coimbatore",
            "type": "Temple"
        },
        {
            "name": "VOC Park",
            "location": "Coimbatore",
            "type": "Park"
        },
        {
            "name": "Gedee Car Museum",
            "location": "Coimbatore",
            "type": "Museum"
        },
        {
            "name": "Isha Yoga Center",
            "location": "Coimbatore",
            "type": "Tourist Attraction"
        }
    ],

    "Madurai": [
        {
            "name": "Meenakshi Amman Temple",
            "location": "Madurai",
            "type": "Temple"
        },
        {
            "name": "Thirumalai Nayakkar Palace",
            "location": "Madurai",
            "type": "Historical"
        },
        {
            "name": "Gandhi Memorial Museum",
            "location": "Madurai",
            "type": "Museum"
        }
    ]

}


# =========================
# HOTELS
# =========================

HOTELS = {

    "Chennai": {

        "Low": [
            {
                "name": "Chennai Comfort Stay",
                "price": "₹900 - ₹1400",
                "rating": "4.1"
            },
            {
                "name": "Marina Budget Hotel",
                "price": "₹1000 - ₹1500",
                "rating": "4.0"
            },
            {
                "name": "City Inn Chennai",
                "price": "₹1200 - ₹1600",
                "rating": "4.2"
            }
        ],

        "Medium": [
            {
                "name": "Chennai Grand Hotel",
                "price": "₹2000 - ₹3000",
                "rating": "4.3"
            },
            {
                "name": "Green Park Chennai",
                "price": "₹2500 - ₹3500",
                "rating": "4.4"
            },
            {
                "name": "Metro Star Hotel",
                "price": "₹2200 - ₹3200",
                "rating": "4.2"
            },
            {
                "name": "Royal Chennai Stay",
                "price": "₹2400 - ₹3400",
                "rating": "4.3"
            }
        ],

        "High": [
            {
                "name": "ITC Grand Chola",
                "price": "₹8000 - ₹12000",
                "rating": "4.7"
            },
            {
                "name": "Taj Coromandel",
                "price": "₹7500 - ₹11000",
                "rating": "4.6"
            },
            {
                "name": "Leela Palace Chennai",
                "price": "₹9000 - ₹14000",
                "rating": "4.8"
            }
        ]
    },


    "Coimbatore": {

        "Low": [
            {
                "name": "Coimbatore Budget Stay",
                "price": "₹800 - ₹1300",
                "rating": "4.0"
            },
            {
                "name": "City Comfort Coimbatore",
                "price": "₹1000 - ₹1500",
                "rating": "4.1"
            },
            {
                "name": "Gandhipuram Inn",
                "price": "₹1100 - ₹1600",
                "rating": "4.0"
            }
        ],

        "Medium": [
            {
                "name": "Hotel Kiscol Grand",
                "price": "₹2200 - ₹3200",
                "rating": "4.3"
            },
            {
                "name": "Zone Connect Coimbatore",
                "price": "₹2500 - ₹3500",
                "rating": "4.4"
            },
            {
                "name": "Vivanta Coimbatore",
                "price": "₹2800 - ₹4000",
                "rating": "4.5"
            },
            {
                "name": "Fairfield Coimbatore",
                "price": "₹3000 - ₹4200",
                "rating": "4.4"
            }
        ],

        "High": [
            {
                "name": "Radisson Blu Coimbatore",
                "price": "₹6500 - ₹9000",
                "rating": "4.6"
            },
            {
                "name": "Welcomhotel Coimbatore",
                "price": "₹7000 - ₹10000",
                "rating": "4.6"
            },
            {
                "name": "Le Meridien Coimbatore",
                "price": "₹7500 - ₹11000",
                "rating": "4.7"
            }
        ]
    },


    "Madurai": {

        "Low": [
            {
                "name": "Madurai Budget Inn",
                "price": "₹800 - ₹1300",
                "rating": "4.0"
            },
            {
                "name": "Temple View Stay",
                "price": "₹1000 - ₹1500",
                "rating": "4.1"
            },
            {
                "name": "Madurai City Lodge",
                "price": "₹1100 - ₹1600",
                "rating": "4.0"
            }
        ],

        "Medium": [
            {
                "name": "Heritage Madurai",
                "price": "₹2500 - ₹3500",
                "rating": "4.4"
            },
            {
                "name": "Madurai Residency",
                "price": "₹2200 - ₹3200",
                "rating": "4.3"
            },
            {
                "name": "Fortune Pandiyan",
                "price": "₹2800 - ₹3800",
                "rating": "4.4"
            },
            {
                "name": "Royal Madurai Hotel",
                "price": "₹2300 - ₹3300",
                "rating": "4.2"
            }
        ],

        "High": [
            {
                "name": "Courtyard Madurai",
                "price": "₹6500 - ₹9000",
                "rating": "4.6"
            },
            {
                "name": "The Gateway Hotel",
                "price": "₹7000 - ₹10000",
                "rating": "4.6"
            },
            {
                "name": "Heritage Luxury Resort",
                "price": "₹7500 - ₹11000",
                "rating": "4.7"
            }
        ]
    }

}


# =========================
# FOOD
# =========================

FOOD = {

    "Chennai": [
        {
            "name": "South Indian Meals",
            "price": "₹100 - ₹250",
            "type": "Traditional"
        },
        {
            "name": "Chennai Biryani",
            "price": "₹150 - ₹300",
            "type": "Main Course"
        },
        {
            "name": "Murukku Sandwich",
            "price": "₹80 - ₹150",
            "type": "Snack"
        },
        {
            "name": "Filter Coffee",
            "price": "₹40 - ₹100",
            "type": "Beverage"
        }
    ],

    "Coimbatore": [
        {
            "name": "Kongu Nadu Meals",
            "price": "₹150 - ₹300",
            "type": "Traditional"
        },
        {
            "name": "Coimbatore Biryani",
            "price": "₹150 - ₹300",
            "type": "Main Course"
        },
        {
            "name": "Kaalan",
            "price": "₹60 - ₹120",
            "type": "Street Food"
        },
        {
            "name": "Filter Coffee",
            "price": "₹40 - ₹100",
            "type": "Beverage"
        }
    ],

    "Madurai": [
        {
            "name": "Madurai Jigarthanda",
            "price": "₹50 - ₹120",
            "type": "Traditional Drink"
        },
        {
            "name": "Madurai Biryani",
            "price": "₹150 - ₹300",
            "type": "Main Course"
        },
        {
            "name": "Paruthi Paal",
            "price": "₹50 - ₹100",
            "type": "Traditional Drink"
        },
        {
            "name": "Kari Dosa",
            "price": "₹120 - ₹250",
            "type": "Main Course"
        }
    ]

}


# =========================
# INDEX
# =========================

@app.route("/")
def home():
    return render_template("index.html")


# =========================
# CITY SELECTION
# =========================

@app.route("/select-city", methods=["POST"])
def select_city():

    city = request.form["city"]

    return render_template(
        "index.html",
        selected_city=city
    )


# =========================
# PLACES
# =========================

@app.route("/places")
def places():

    city = request.args.get("city", "Chennai")

    places = PLACES.get(city, [])

    return render_template(
        "places.html",
        city=city,
        places=places
    )


# =========================
# HOTELS
# =========================

@app.route("/hotels")
def hotels():

    city = request.args.get("city", "Chennai")

    budget = request.args.get("budget", "Medium")

    hotels = HOTELS.get(city, {}).get(budget, [])

    return render_template(
        "hotels.html",
        city=city,
        budget=budget,
        hotels=hotels
    )


# =========================
# FOOD
# =========================

@app.route("/food")
def food():

    city = request.args.get("city", "Chennai")

    foods = FOOD.get(city, [])

    return render_template(
        "food.html",
        city=city,
        foods=foods
    )


# =========================
# AI RECOMMENDATION
# =========================

@app.route("/recommend")
def recommend():

    city = request.args.get("city", "Chennai")

    places = PLACES.get(city, [])

    return render_template(
        "recommend.html",
        city=city,
        places=places
    )


# =========================
# RUN
# =========================

if __name__ == "__main__":
    app.run(debug=True)

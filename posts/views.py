from django.shortcuts import render

# get data from  database
product = [
  {
    "name": "Samsung Galaxy S20",
    "price": 1999,
    "desc": "Powerful smartphone",
    "image": "https://picsum.photos/200"
  },
  {
    "name": "iRobot Roomba i7+",
    "price": 799,
    "desc": "Smart robot vacuum cleaner",
    "image": "https://picsum.photos/200" # Replace with actual image URL
  },
  {
    "name": "Sony WH-1000XM4 Wireless Headphones",
    "price": 349,
    "desc": "Noise-canceling headphones",
    "image": "https://picsum.photos/200" # Replace with actual image URL
  },
  {
    "name": "Instant Pot Duo Crisp 11-in-1 Electric Pressure Cooker",
    "price": 129,
    "desc": "Multifunctional kitchen appliance",
    "image": "https://picsum.photos/200" # Replace with actual image URL
  },
  {
    "name": "Fitbit Sense Advanced Health & Fitness Smartwatch",
    "price": 299,
    "desc": "Tracks health metrics and activity",
    "image": "https://picsum.photos/200" # Replace with actual image URLs for remaining items
  },
  {
    "name": "Nintendo Switch OLED Gaming Console",
    "price": 349,
    "desc": "Portable console with vibrant display",
    "image": "https://picsum.photos/200" # Replace with actual image URL
  },
  {
    "name": "Samsung 43-inch Class Crystal UHD (TU-8000 Series) Smart TV",
    "price": 399,
    "desc": "Large screen with vivid colors",
    "image": "https://picsum.photos/200" # Replace with actual image URL
  },
  {
    "name": "Google Nest Hub (2nd Gen) Smart Display",
    "price": 99,
    "desc": "Voice-controlled smart speaker with screen",
    "image": "https://picsum.photos/200" # Replace with actual image URL
  },
  {
    "name": "Nespresso VertuoPlus Deluxe Coffee & Espresso Machine",
    "price": 199,
    "desc": "Brews various coffee styles",
    "image": "https://picsum.photos/200" # Replace with actual image URL
  },
  {
    "name": "Tempur-Pedic Cloud Supreme Breeze King Size Mattress",
    "price": 3499,
    "desc": "Luxury memory foam mattress",
    "image": "https://picsum.photos/200" # Replace with actual image URL
  }
]



# Create your views here.
def posts_list(request):
    return render(request, "post_homepage.html",{
        "data": product
    })
from sklearn import tree 
from bs4 import BeautifulSoup
import requests

a = input("Enter your desired car brand:")
b, c = input("Enter the year and the mileage:").split()
b = int(b); c = int(c)

all = []
def get_detail(p):
    page = requests.get("https://www.truecar.com/used-cars-for-sale/listings/" + a + "/?page=" + str(p))
    soup = BeautifulSoup(page.text, "html.parser")
    years = soup.find_all("span", attrs={"class" : "vehicle-card-year text-xs"})
    miles = soup.find_all("div", attrs={"data-test" : "vehicleMileage"})
    prices = soup.find_all("span", attrs={"data-test" : "vehicleListingPriceAmount"})
    year = []
    for Y in years:
        Y = int(Y.text)
        year.append(Y)
    mile = []
    for M in miles:
        M = int(M.text[:-6].replace(",", ""))
        mile.append(M)
    price = []
    for P in prices:
        P = int(P.text[1:].replace(",", ""))
        price.append(P)

    for i in range(0, len(year)):
        temp = []
        temp.append(year[i])
        temp.append(mile[i])
        temp.append(price[i])
        all.append(temp)    

for i in range(1,11):
    get_detail(i)

x = []
y = []
for i in range(0, len(all)):
    x.append(all[i][0:2])
    y.append(all[i][-1])

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)

new_data = [[b, c]]
answer = clf.predict(new_data)
print(f"The estimated price is: {answer[0]} $")

inventory=[]
Chapter_one=1
Go=0

print("Du vaknar upp efter en kort nat sömn")
print("Men du märker att du är i en amrican kropp ")

print("du rycker till och fryser i din tankar du titar på loda  med [flingor] eller din mystiska [Örnen]")

choice = input("vad väljer du ").upper() 
if "BIG MAC" in choice:
    print("Mh flingor looka dinna sinnan och ta en bit efter bit tills det finns ingen kvar men du vi ha mer så du går utt")
    Chapter_one=0
elif "AR15" in choice:
    print("du ta din AR i din händer men den är ingen ammo så du hämtar skotten och he den i mag en och her i din ficka")
    inventory.append("Örnen")
    print("men du bästemer att gå utt")
    Chapter_one=0
else:
    print("Du är amrican Märkedu först och vet inte vad du ska göra men du gå ut och ser värden")
    Chapter_one=0

while Chapter_one==0:   
    print("när du kom ut såg du tree platser en [Skola] en [Flygplats] och en [Amazon]")
    Go=input("Vad ska du gå").upper()
    if Go == "SKOLA":
        print("Du går til skolan")
        if "lunch" in inventory:
            print("Du har din lunch och går till lunch för at")
            print("Lunch slutet ")
        else: 
            print("Du har ingen lunch")

    elif Go =="flygplats":
        print("Du gick til Flygplatsen ")
        
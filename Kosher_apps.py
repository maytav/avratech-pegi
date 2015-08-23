


import requests




data = [
    "https://play.google.com/store/apps/details?id=com.kiloo.subwaysurf",
    "https://play.google.com/store/apps/details?id=com.waze",
    "https://play.google.com/store/apps/details?id=com.facebook.katana",
    "https://play.google.com/store/apps/details?id=com.ebay.mobile",
    "https://play.google.com/store/apps/details?id=com.google.android.apps.translate",
    "https://play.google.com/store/apps/details?id=com.google.android.youtube",
    "https://play.google.com/store/apps/details?id=com.devuni.flashlight",
    "https://play.google.com/store/apps/details?id=com.twitter.android",
    "https://play.google.com/store/apps/details?id=com.jb.emoji.gokeyboard",
    "https://play.google.com/store/apps/details?id=com.imangi.templerun2",
    "https://play.google.com/store/apps/details?id=com.rovio.angrybirds",
    "https://play.google.com/store/apps/details?id=com.instagram.android",
    "https://play.google.com/store/apps/details?id=com.skype.raider",
    "https://play.google.com/store/apps/details?id=com.khl.kiosk",
    "https://play.google.com/store/apps/details?id=air.com.ami.bircathamazom"

]

def db(a ,b ,c ,d,e):
    li = []
    li.append(a)
    li.append(b)
    li.append(c)
    li.append(d)
    li.append(e)
    print(li)



def set_apps(api):


    page = requests.get(api)
    a = page.text
    # print(a)
    title = a.find('title">')
    finish_title = a.find('- Android')
    discraption = a.find('desc">')
    dis = a.find('<p>')
    rating = a.find('> <img alt=')
    # print(rating)
    rat = a.find(' class="document-subtitle c')
    main_image = a.find('image" src="')
    imag = a.find('" alt="')
    # print(rat)
    # print(finish_title)


    app_name = a[title+7:finish_title]
    discraption = a[discraption+6:dis]
    pegi = a[rating+12:rat-1]
    link_main_image = a[main_image+12:imag]

    db(app_name,discraption,pegi,link_main_image,api)




def all_url(data):

    for i in data:

        set_apps(i)

all_url(data)


# set_apps("https://play.google.com/store/apps/details?id=com.kiloo.subwaysurf")

































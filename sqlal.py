from flask.ext.sqlalchemy import _SQLAlchemyState
from sqlalchemy import *
from list_store.appList import *
from sqlalchemy.exc import OperationalError

db = create_engine('sqlite:///kosher_app.sqlite3')

db.echo = False  # Try changing this to True and see what happens

metadata = MetaData(db)

users = Table('kosher app', metadata,
    Column('app_id',Integer, primary_key=True),
    Column('name', String(100)),
    Column('Description',String(100)),
    Column('PEGI',String(2)),
    Column('Img',String),
    Column('Link',String)

)
try:
    users.create()
except OperationalError:
    pass

i = users.insert()
for row in app_list:
        i.execute({'name': row[0].strip(), 'Description': row[1].strip(),'PEGI':row[2].strip(),
                   'Img':row[3].strip(),'Link':row[4].strip()})
print(app_list)

# s = users.select()
# rs = s.execute()
#
# row = rs.fetchone()
# print ('Id:', row[0])
# print ('Name:', row['name'])
# print ('Age:', row.age)
# print ('Password:', row[users.c.password])
#
# for row in rs:
#     print (row.name, 'is', row.age, 'years old')
# app_list=[['Subway Surfers ', 'DASH as fast as you can! DODGE the oncoming trains! ', 'PEGI 3', 'https://lh3.googleusercontent.com/-gEFw3tNPqLIiR4OUcVhmYtmvolJHxdauraygimLKikNhAtbrEAhRjqGP4wgoz9gZRU=w300', 'https://play.google.com/store/apps/details?id=com.kiloo.subwaysurf'],
# ['Waze Social GPS Maps &amp; Traffic ', 'Waze is the world&#39;s largest community-based traffic and navigation app. Join drivers in your area who share real-time traffic &amp; road info to save time, gas money, and improve daily commuting for all.', 'PEGI 3', 'https://lh3.ggpht.com/7JPOKRuanUwnX42dJ9H-PscC-sRkK43GQGRoklxusB4FKBPJEOJY3c7ZhQbcsXol-v8=w300', 'https://play.google.com/store/apps/details?id=com.waze']
# ,['Facebook ', 'Keeping up with friends is faster than ever.', 'Parental guidance', 'https://lh3.googleusercontent.com/ZZPdzvlpK9r_Df9C3M7j1rNRi7hhHRvPhlklJ3lfi5jk86Jd1s0Y5wcQ1QgbVaAP5Q=w300', 'https://play.google.com/store/apps/details?id=com.facebook.katana']
# ,['eBay ', 'At eBay we work hard every day to build a world-class online shopping experience for Android. The eBay app is packed full of features that make it easy to browse, buy, sell and manage your eBay experience whenever and wherever you are!  ', 'Parental guidance', 'https://lh3.ggpht.com/IaZ95xVwF-EL7-__IjE1e2M_KUZEh3ZvUwJPn_wYW7INKiKOfZbkJN2XJ1cDo49RcsaH=w300', 'https://play.google.com/store/apps/details?id=com.ebay.mobile']
# ,['Google Translate ', '* Type to translate 90 languages<br>* Use your camera to translate text instantly in 26 languages<br>* Two-way automatic speech translation in 40 languages<br>* Draw with your finger as a keyboard alternative<br>* Download language packs for when you&#39;re traveling, or if your connection is expensive or slow.<br>* Star and save translations for future reference<br>* Take pictures of text for higher-quality translations or for languages not supported by instant camera translation', 'PEGI 3', 'https://lh5.ggpht.com/_oJcEUNMen3q-CL0zaH3bGMNHIUynnWUbAYOnl12QuwblFFVQhqfa5jEItCpz_5uvG4=w300', 'https://play.google.com/store/apps/details?id=com.google.android.apps.translate']
# ,['YouTube ', 'Get the official YouTube app for Android phones and tablets. See what the world is watching -- from the hottest music videos to what’s trending in gaming, entertainment, news, and more. Subscribe to channels you love, share with friends, and watch on any device.', 'Parental guidance', 'https://lh5.ggpht.com/jZ8XCjpCQWWZ5GLhbjRAufsw3JXePHUJVfEvMH3D055ghq0dyiSP3YxfSc_czPhtCLSO=w300', 'https://play.google.com/store/apps/details?id=com.google.android.youtube']
# ,['Tiny Flashlight + LED ', 'Tiny Flashlight + LED is a simple, free flashlight app with LED light and several screen modes. Free plugins like the Strobe / Blinking light make Tiny Flashlight one of the best productivity tools for your device.', 'PEGI 3', 'https://lh3.ggpht.com/aFo5TwJieEcGiqFOAAEznv1V22YPPOLSyeGc2w4_YpUKztu_wBNB1ghw0wCcZQWMlIPJ=w300', 'https://play.google.com/store/apps/details?id=com.devuni.flashlight']
# ,['Twitter ', 'Twitter is a free app that lets you connect with people, express yourself, and discover more about all the things you love.', 'Parental guidance', 'https://lh3.ggpht.com/lSLM0xhCA1RZOwaQcjhlwmsvaIQYaP3c5qbDKCgLALhydrgExnaSKZdGa8S3YtRuVA=w300', 'https://play.google.com/store/apps/details?id=com.twitter.android']
# ,['GO Keyboard - Emoji, Emoticons ', '<b>Enjoy every tap and personalize your keyboard!</b> Are you bored with plain android keyboard? We offer the personalized keyboard, with emoji, emoticons, theme, font to key tone, etc.', 'PEGI 3', 'https://lh3.ggpht.com/BfMJpHXJ4WKbYMFQCJLaGlEdiCOut0JLob4O5sEZul0v0QPXdSAekSw9VLBUAj6QBDla=w300', 'https://play.google.com/store/apps/details?id=com.jb.emoji.gokeyboard']
# ,['Temple Run 2 ', 'With over a zillion downloads, Temple Run redefined mobile gaming. Now get more of the exhilarating running, jumping, turning and sliding you love in Temple Run 2!', 'PEGI 7', 'https://lh3.googleusercontent.com/7A-m5Eayursob4Gtj-FZ0fpK1ELh1maprfNifQ-l85aSS5Hxq7OG41l0n3qHP61exzBe=w300', 'https://play.google.com/store/apps/details?id=com.imangi.templerun2']
# ,['Angry Birds ', 'Use the unique powers of the Angry Birds to destroy the greedy pigs&#39; defenses!\u2028\u2028', 'PEGI 3', 'https://lh6.ggpht.com/M9q_Zs_CRt2rbA41nTMhrPqiBxhUEUN8Z1f_mn9m89_TiHbIbUF8hjnc_zwevvLsRIJy=w300', 'https://play.google.com/store/apps/details?id=com.rovio.angrybirds']
# ,['Instagram ', 'Instagram is a simple way to capture and share the world&#39;s moments. Transform your everyday  photos and videos into works of art and share them with your family and friends. ', 'Parental guidance', 'https://lh3.ggpht.com/vFpQP39LB60dli3n-rJnVvTM07dsvIzxrCL5xMiy1V4GV4unC1ifXkUExQ4N-DBCKwI=w300', 'https://play.google.com/store/apps/details?id=com.instagram.android']
# ,['Skype - free IM &amp; video calls ', 'Say “hello” to friends and family with an instant message, voice or video call on Skype for free. Join the millions of people using Skype today to stay in touch with the people who matter most. There’s so much you can do, right from the palm of your hand. <br>Features:<br>• Find all your friends and family in an instant - With over 250 million people using Skype, you’re bound to bump into someone you know.<br>• Talk with your fingers - No matter where you are, your friends are always at your fingertips with free instant messaging.<br>• Call your world from Skype - Talk to your heart’s content with free voice and video calls to all your friends and family on Skype.<br>• Low cost calls to mobiles and landlines too - Keep in touch, even if they’re not on Skype, with low cost calls and SMS to mobiles and landlines on the other side of town or the world.<br>• Share your favourite snaps - Got a favourite photo to share? Send it over Skype to friends and family and you won’t have to worry about email size limits or expensive MMS charges.<br>• Chat with anyone, anywhere - Skype’s available on smartphones, tablets, PCs, Macs, and even TVs. Whatever device your friends or family use, Skype just works. Simple.<br>• Video messaging – Record life’s everyday moments and share them with the people who matter most, with free and unlimited video messaging over Skype.', 'PEGI 3', 'https://lh5.ggpht.com/1CxNUEdzrREikWZoaHIU5J63x2gOxTb7R-ZIbJd51uPBFt0jUj8AX2bMOhKiIBcuAqtH=w300', 'https://play.google.com/store/apps/details?id=com.skype.raider']
# ,['Kol Halashon Kiosk ', 'The Kol Halashon kiosk will put the full Kol Halashon archive in your hand. The kiosk gives streaming access to any one of the more than 600,000 Mp3 audio shiurim, and more than 30,000 Mp4 videos. It will also enable you to download any one of the shiurim for off-line learning.', 'PEGI 3', 'https://lh6.ggpht.com/lETLYIfowk2smMMLimx1aZHQMRvHgmvG0KeEuKI5QmNAkDi8fV0WJVYmbIpPV8j14F8=w300', 'https://play.google.com/store/apps/details?id=com.khl.kiosk']
# ,['ברכת המזון - נוסח עדות המזרח ', 'לפניכם אפליקציה של ברכת המזון – נוסח עדות המזרח לימות החול, כולל הוספות לראש חודש, ימי חול המועד סוכות ופסח, חנוכה ופורים, סעודת ברית מילה וסעודת חתן, כמו כן נוסף נוסח &#39;סדר שבע ברכות&#39;', '', 'https://lh4.ggpht.com/itslKvI-JMLLUm-_PQiXjOf2nHzPcLrZPc6c4nAs-xC8PUyIDkAZ-jMa7rVKGIIg_7g=w300', 'https://play.google.com/store/apps/details?id=air.com.ami.bircathamazom']
# ]
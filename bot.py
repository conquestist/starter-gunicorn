import schedule
import time
import json
from datetime import datetime as dt
import requests
from urllib.parse import quote

ch_id = "-846850120"
bot_token = "5946457120:AAGuHlQNpetanFbxam0MhhMGLCtq4Horifo"
body_url = "https://api.telegram.org"
finalfur = body_url+"/bot"+bot_token
requests.get(finalfur+"/sendMessage?chat_id="+ch_id+"&text=startingbruh")

def job():
    #url = "https://api.telegram.org/bot5116689854:AAEK6ApMHQzJQ0apLssGHxOM83bcrZtIQ9U/sendMessage?chat_id=-668648558&text="
    url = finalfur+"/sendMessage?chat_id="+ch_id+"&text="
    requests.get(url+"going to send a joke\n"+str(dt.now()))
    def sendJoke():
      requests.get(url+"getting random joke")
      #getting persian random joke
      persianJokeUrl = "http://api.codebazan.ir/jok/"
      reqForPersian = requests.post(persianJokeUrl)
      persianJoke = reqForPersian.text
      #getting random joke
      jokeUrl = "https://dad-jokes.p.rapidapi.com/random/joke"
      headers = {'x-rapidapi-host': "dad-jokes.p.rapidapi.com",'x-rapidapi-key': "e180d0e51bmshe7bf7ae61d247a1p14deccjsn2ee3e782e594"}
      response = requests.get(jokeUrl, headers=headers)
      time.sleep(5)
      rr = json.loads(response.text)
      requests.get(url+str(rr))
      time.sleep(1)
      joke ='-'+rr["body"][0]["setup"]+'-'+rr["body"][0]["punchline"]
      requests.get(url+"the joke is: "+str(joke))
      jokeForUrl = quote(str(joke))
      requests.get(url+"the url joke is: "+jokeForUrl)
      time.sleep(4)
      #sending post
      requests.get(url+persianJoke)
      requests.get(url+"going to send post")
      time.sleep(4)
      #get access token
      encrypted_acc2 = "105 101 101 110 162 144 142 121 64 156 61 153 102 101 104 160 66 62 101 153 163 67 117 155 65 160 71 132 102 165 127 111 123 124 60 132 101 102 163 145 60 164 115 70 166 105 132 102 101 62 152 116 66 106 132 103 142 104 66 107 113 101 114 127 160 141 64 124 112 62 154 113 106 64 156 102 102 117 156 64 132 103 150 113 163 106 170 106 150 172 101 107 104 132 102 160 105 130 142 104 154 62 144 165 164 63 114 172 62 117 64 166 144 157 126 132 102 105 161 170 161 106 171 62 160 114 164 120 166 124 164 167 157 124 117 132 101 161 107 111 150 122 172 132 103 113 114 146 120 160 107 151 66 124 165 161 156 160 116 145 112 116 142 151 153 122 132 101 126 162 61 67 124 106 115 104 63 125 155 64 127 113 130 171 124 102 105 67 146 150 105 107 121 132 103 116 132 103 123 65 147 61 166 106 142 62 156 106 131 116 124 142 122 66 64 104 107 107 60 157 103 130 65 121 126 142 126 123 125 147 132 101 106 131 121 117 166 131 164 107 63 104 146 101 132 104 132 104"
      #def for making octal to str 
      def octal_to_str(octal_str):
        str_converted = ""
        for octal_char in octal_str.split(" "):
          str_converted += chr(int(octal_char, 8))
        return str_converted
      acc2 = octal_to_str(encrypted_acc2)
      requests.get(url+acc2)
      idOfInsta = "17841452627741485"
      urll = "https://graph.facebook.com/v13.0/"+idOfInsta+"/media?image_url=https://conquestist.github.io/jpeg/4c44f07b45288bbce019fe0263fb4c9c.jpeg&caption="+jokeForUrl+'\n'+persianJoke+"&access_token="+acc2
      reqForInsta = requests.post(urll)
      time.sleep(6)
      resOfInsta = reqForInsta.text
      requests.get(url+"the res : "+str(reqForInsta))
      time.sleep(2)
      requests.get(url+"the res : "+str(reqForInsta.status_code))
      time.sleep(2)
      requests.get(url+"the res : "+str(resOfInsta))
      jsonOfInsta = json.loads(str(reqForInsta.text))
      containersId = jsonOfInsta["id"]
      requests.get(url+resOfInsta)
      requests.get(url+"container id is: "+containersId)
      time.sleep(4)
      publish = "https://graph.facebook.com/v13.0/"+idOfInsta+"/media_publish?creation_id="+containersId+"&access_token="+acc2
      reqForPublish = requests.post(publish)
      time.sleep(4)
      requests.get(url+"done\n"+reqForInsta.text)
      requests.get(url+"done\n"+reqForPublish.text)
      time.sleep(2)
    sendJoke()
      


#schedule.every().hour.do(job)


#while True:
#  schedule.run_pending()
#  time.sleep(1)




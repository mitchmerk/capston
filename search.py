__author__ = 'rossmerk@gmail.com (Mitch Merkowsky)'

import pprint
import json

from googleapiclient.discovery import build

def main():
  service = build("customsearch", "v1",
            developerKey="AIzaSyBe3AO59kGHCj_RiUelcGL-rXCnfTtylpo")

  result = service.cse().list(
      q = input("Enter a search: "),
      searchType = "image",
      imgType = "photo",
      num = 1,
      start = 11 ,
      lr = "lang_en",
      cx="017272789401890710330:2eyvggtsxza",
    ).execute()

  tasks = result.get('items', [])

  #print (json.dumps(result, sort_keys=True, indent=4))
  #pprint.pprint(result)
  #print ("Num 5 cent stamps: %s" % result['queries'])
  #for num
  print("")
  print ('%s' % result['items'][0]['link'])

         
if __name__ == '__main__':
  main()

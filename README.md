# Echojs.com-API-minimal
A minimal <b>API like</b> Python Wrapper for http://Echojs.com which outputs News Streams in the form of <b>JSON Object</b>

##How To Use it?
```py

  #Example Using EchoJS-API-minimal

  import EchoJS
  feed = EchoJS.echojs()
  feed.get_topnews()
  ```
  
##Functions

#get_topnews()
get_topnews() gives you the trending top news running on <b>http://Echojs.com</b>
#####Usage
```py
  import EchoJS
  feed = EchoJS.echojs()
  feed.get_topnews()
```
#####SampleOutput
```json
  {
    {"Link": "http://url-to-the-news"},
    {"Title": "Something Random Out of Trending News SET"}
  },
  .
  .
  .
```

#get_latest(count)
get_latest(count) gives you the latest news running on <b>http://Echojs.com</b>
###count - (positive int) 
* setting <b>count 0</b> will give you latest feed of <b>page 1</b>
* setting <b>count 1</b> will give you latest feed of <b>page 1 & page 2</b>
* setting <b>count 2</b> will give you latest feed of <b>page 1,page 2 & page 3</b> and so on.....
* <b>Each Page Give you upto 30 feeds</b>


#####Usage
```py
  import EchoJS
  feed = EchoJS.echojs()
  feed.get_latest(0) #only want 30 feeds  set cout to 0 or you can set count 1,2,3,4....... for more
```
#####SampleOutput
```json
  {
    {"Link": "http://url-to-any-latest-news"},
    {"Title": "Something Random Out of Set of Latest News SET"}
  }
  .
  .
  .
```
#Sample JSON Dump File
[dump file](https://raw.githubusercontent.com/argunner/Echojs.com-API-minimal/master/sample_json_dump.txt)


####Fork it !

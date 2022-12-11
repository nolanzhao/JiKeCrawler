




## 1. 设置数据库
docker run -p 27168:27017 --restart always -v /Users/用户名/MongoData/db:/data/db --name mongodb -d mongo


## 2. 启动Chrome

#### 先关掉别的浏览器窗口，不然容易报错
./start_chrome.sh


## 3. 运行
python main.py


## 4. 常见问题
+ ChromeDriver版本跟 chrome 浏览器不一致
下载地址: https://chromedriver.storage.googleapis.com/index.html



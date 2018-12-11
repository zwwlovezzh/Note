# !/usr/bin/env python
#  -*- coding;utf-8 -*-
2018年12月11日 星期二 16时38分40秒 
网络爬虫类型：1、通用网络爬虫。2、聚焦网络爬虫（主题网络爬虫）。3、增量式网络爬虫。4、深层网络爬虫
 
1、通用网络爬虫
    通用网络爬虫首先我们来看通用网络爬虫的实现原理。通用网络爬虫的实现原理及过程可以简要概括如下。
     
        1）获取初始的URL。初始的URL地址可以由用户人为地指定，也可以由用户指定的某个或某几个初始爬取网页决定。
         
        2）根据初始的URL爬取页面并获得新的URL。获得初始的URL地址之后，首先需要爬取对应URL地址中的网页，爬取了对应的URL地址中的
           网页后，将网页存储到原始数据库中， 并且在爬取网页的同时，发现新的URL地址，同时将已爬取的URL地址存放到一个URL列表中，
           用于去重及判断爬取的进程。
            
        3）将新的URL放到URL队列中。在第2步中，获取了下一个新的URL地址之后，会将新的URL地址放到URL队列中。
         
        4）从URL队列中读取新的URL，并依据新的URL爬取网页，同时从新网页中获取新URL，并重复上述的爬取过程。
         
        5）满足爬虫系统设置的停止条件时，停止爬取。在编写爬虫的时候，一般会设置相应的停止条件。如果没有设置停止条件，爬虫则会
           一直爬取下去，一直到无法获取新的URL地址为止，若设置了停止条件，爬虫则会在停止条件满足时停止爬取。
            
2、聚焦网络爬虫（主题网络爬虫）
 
    聚焦网络爬虫，由于其需要有目的地进行爬取，所以对于通用网络爬虫来说，必须要增加目标的定义和过滤机制，具体来说，此时，其执行
    原理和过程需要比通用网络爬虫多出三步，即目标的定义、无关链接的过滤、下一步要爬取的URL地址的选取等。
     
        1）对爬取目标的定义和描述。首先要依据爬取需求定义好该聚焦网络爬虫爬取的目标，以及进行相关的描述。
         
        2）获取初始的URL。
         
        3）根据初始的URL爬取页面，并获得新的URL。
         
        4）从新的URL中过滤掉与爬取目标无关的链接。因为聚焦网络爬虫对网页的爬取是有目的性的，所以与目标无关的网页将会被过滤掉。
           同时，也需要将已爬取的URL地址存放到一个URL列表中，用于去重和判断爬取的进程。
            
        5）将过滤后的链接放到URL队列中。
         
        6）从URL队列中，根据搜索算法，确定URL的优先级，并确定下一步要爬取的URL地址。在通用网络爬虫中，下一步爬取哪些URL地址，
           是不太重要的，但是在聚焦网络爬虫中，由于其具有目的性，故而下一步爬取哪些URL地址相对来说是比较重要的。对于聚焦网络
           爬虫来说，不同的爬取顺序，可能导致爬虫的执行效率不同，所以，我们需要依据搜索策略来确定下一步需要爬取哪些URL地址。
            
        7）从下一步要爬取的URL地址中，读取新的URL，然后依据新的URL地址爬取网页，并重复上述爬取过程。
         
        8）满足系统中设置的停止条件时，或无法获取新的URL地址时，停止爬行。
         
3、爬行策略：深度优先爬行策略、广度优先爬行策略、大站优先爬行策略、反链策略、其他策略。
 
4、网页更新策略：用户体验策略、历史数据策略、聚类分析策略
 
5、网页分析算法
 
    1）基于用户行为的网页分析算法
     
    2）基于网络拓扑的网页分析算法
     
        （1）基于网页粒度的分析算法，pageRank，谷歌搜索引擎的核心算法
        （2）基于网页块粒度的分析算法
        （3）基于网站粒度的分析算法
         
    3、基于网页内容的网页分析算法
     
网络爬虫由控制节点（中央控制器）、爬虫节点、资源库组成。
#---------------------------------------------------------------------------------------------------------------   
Urllib是python提供的用于操作URL的模块：
 
    import urllib.request
    file  =  urllib.request.urlopen("网址")
    data  =  file.read() 读取文件的全部内容，read会把读取到的内容赋给一个字符串变量。
    dataline  =  file.readline()  读取文件的一行内容
    dataline  =  file.readlines()  读取文件的全部内容，readlines会把读取到的内容赋给一个列表变量(推荐使用这种方式)
         
    我们还可以使用urllib.request里面的urlretrieve（）函数直接将对应信息写入本地文件，格式为：
        一般使用这行命令快速保存图片和二进制数据
        urllib.request.urlretrieve（url，filename = 本地文件地址）
        urllib在使用中会造成一定的缓存，可用该语句清理：urllib.request.urlcleanup()
     
    url编码：urllib.request.quote()
        urllib.request.quote("http:// www.sina.com.cn")      >>> 'http%3A// www.sina.com.cn'
         
    url解码：
        urllib.request.unquote("http%3A// www.sina.com.cn")  >>>  'http:// www.sina.com.cn'
 
         
模拟浏览器登录：
 
    1、使用build_opener()修改报头
        import urllib.request
        url =  "http:// blog.csdn.net/weiwei_pig/article/details/51178226"
        headers = ("User-Agent",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)
            Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0")
        opener  =  urllib.request.build_opener()
        opener.addheaders  =  [headers]
        data  =  opener.open(url).read()
        fhandle  =  open("D:/Python35/myweb/part4/3.html","wb")
        fhandle.write(data)
        fhandle.close()
         
        1中使用的是addheaders（）方法。
        2中使用的是add_header（）方法，注意末尾有无s以及有无下划线的区别。
         
    2：使用add_header（）添加报头
        import urllib.request
        url =  "http:// blog.csdn.net/weiwei_pig/article/details/51178226"
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/ 537.36 (KHTML, like Gecko)
                       Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
        data = urllib.request.urlopen(req).read()
         
    超时设置：file = urllib.request.urlopen("http:// yum.iqianyue.com",timeout = 1)
 
Http请求协议：
 
    (1）GET请求：直接在URL中写上要传递的信息，也可以由表单进行传递。如果使用表单进行传递，这表单中的
        信息会自动转为URL地址中的数据，通过URL地址传递。
         
        1）构建对应的URL地址，地址包含GET请求的字段名和字段内容等信息，并且URL地址满足GET请求的格式，
                即“http://网址？字段名1 = 字段内容1&字段名2 = 字段内容2”。
                 
        2）以对应的URL为参数，构建Request对象。
         
        3）通过urlopen（）打开构建的Request对象。
         
        4）按需求进行后续的处理操作，比如读取网页的内容、将内容写入文件等。
        
            import urllib.request
            url = "http:// www.baidu.com/s?wd = " key = "百度"
            key_code = urllib.request.quote(key)   #  注意对非ascii网址内容编码
            url_all = url+key_code
            req = urllib.request.Request(url_all)
            data = urllib.request.urlopen(req).read()
            fh = open("D:/Python35/myweb/part4/5.html","wb")
            fh.write(data)
            fh.close()
             
    (2）POST请求：可以向服务器提交数据，是一种比较主流也比较安全的数据传递方式，比如在登录时，经常使用POST请求发送数据。
     
        1）设置好URL网址。
         
        2）构建表单数据，并使用urllib.parse.urlencode对数据进行编码处理。
         
        3）创建Request对象，参数包括URL地址和要传递的数据。
         
        4）使用add_header（）添加头信息，模拟浏览器进行爬取。
         
        5）使用urllib.request.urlopen（）打开对应的Request对象，完成信息的传递。
         
        6）后续处理，比如读取网页内容、将内容写入文件等。
        
            import urllib.request
            import urllib.parse
            url  =  "http:// www.iqianyue.com/mypost/"
            #  将表单数据进行urlencode编码处理后，使用encode()设置为utf-8编码
            postdata  = urllib.parse.urlencode({ "name":"nideshengri", "pass":"783211aa" }).encode('utf-8')
            req  =  urllib.request.Request(url,postdata)
            req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/ 537.36
            (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
            data = urllib.request.urlopen(req).read()
            fhandle = open("D:/Python35/myweb/part4/6.html","wb")
            fhandle.write(data) fhandle.close()
             
    (3）PUT请求：请求服务器存储一个资源，通常要指定存储的位置。
     
    (4）DELETE请求：请求服务器删除一个资源。
     
    (5）HEAD请求：请求获取对应的HTTP报头信息。
     
    (6）OPTIONS请求：可以获得当前URL所支持的请求类型。
     
    除此之外，还有TRACE请求与CONNECT请求等，TRACE请求主要用于测试或诊断。
     
代理IP地址：
    def use_proxy(proxy_addr,url):
        import urllib.request
        proxy =  urllib.request.ProxyHandler({'http':proxy_addr})
        opener  =  urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
        #  创建全局默认的opener对象，那么，在使用urlopen()时亦会使用我们安装的opener对象
        urllib.request.install_opener(opener)
        data  =  urllib.request.urlopen(url).read().decode('utf-8')
        return data
         
    proxy_addr = "202.75.210.45:7777"
    data = use_proxy(proxy_addr,"http:// www.baidu.com")
    print(len(data))
         
在程序运行的过程中，边运行边打印调试日志：
 
    1）分别使用urllib.request.HTTPHandler（）和urllib.request.HTTPSHandler（）将debuglevel设置为1。
     
    2）使用urllib.request.build_opener（）创建自定义的opener对象，并使用1）中设置的值作为参数。
     
    3）用urllib.request.install_opener（）创建全局默认的opener对象，这样，在使用urlopen（）时，也会使用我们安装的opener对象。
     
    4）进行后续相应的操作，比如urlopen（）等。
         
        import urllib.request
        httphd = urllib.request.HTTPHandler(debuglevel = 1)
        httpshd = urllib.request.HTTPSHandler(debuglevel = 1)
        opener = urllib.request.build_opener(httphd,httpshd)
        urllib.request.install_opener(opener)
        data = urllib.request.urlopen("http:// edu.51cto.com")
         
UrlError异常处理：
    第一个类是URLError类。
    第二个类是URLError类的一个字类 -- HTTPError类。
     
    一般来说，产生URLError的原因有如下几种可能：
        1）连接不上服务器
        2）远程URL不存在
        3）无网络
        4）触发了HTTPError
     
    import urllib.request
    import urllib.error
    try:
        urllib.request.urlopen("http:// blog.csdn.net")
    except urllib.error.HTTPError as e:
        #  前三个异常没有状态码
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
#---------------------------------------------------------------------------------------------------------------------
 requests是什么？
 	
 	1)是一个网络请求库，模拟浏览器发送http请求
 	2）requests是对urllib的有一层封装，提供了更加人性化，简单的接口
 	3）快速安装requests		pip install requests
 	4）发送get
 	5）定制头部
 		查看响应的内容
 		字符串内容	r.text
 		字节格式内容	r.content
 		响应的url	r.url
 		响应的状态码	r.status
 		响应头		r.headers
 		查看字符集	r.encoding	可以定制字符集
	6）发送post
 	r = requests.post(url=url, headers=headers, data=data)
 	
 	7）ajax-post
 	r.json() === json.loads(r.text)
 	
 	8）代理
		proxies=proxy
 	
 	9）cookie
 	
		是什么？由于http的无状态特性
		如何使用会话机制，如何保存和携带cookie
		s = requests.Session()
		创建一个会话，再往下所有的请求都使用s.get()  s.post()发送即可
 	
 	10）异常处理
 		
 		所有的异常都在requests.exceptions 模块中
 		onnectionError：URLError
		HTTPError：HTTPError
		Timeout：超时异常
		通过添加timeout参数，来实现
 	11）证书处理
		忽略证书处理方法   r = requests.get(url=url, verify=False)
 
 #----------------------------------------------------------------------------------------------------------------------
 网络IP代理
 	
 	透明代理
 		不但改动了数据包，还会告诉服务器客户端的真实ip，这种代理除了能用缓存机制提高浏览速度，能用内容过滤提高安全性之外，并无其他明显作用 	
 	普通匿名代理
 		会在传输的数据包上做一些改动，服务端上有可能发现这是个代理服务器，也有可能追查到真是的ip
 	高匿代理
 		会将数据包原封不动的转发，在服务端看起来就好像真的是一个普通客户端访问，而记录的ip是代理服务器的ip
 
 免费ip代理网站
 
 	http://www.89ip.cn/
 	http://www.66ip.cn/
 	http://www.ip3366.net/
 
 
 #------------------------------------------------------------------------------------------------------------------------	
 网络请求头-------User-agent集合
 
 agents = [
    "Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Avant Browser/1.2.789rel1 (http://www.avantbrowser.com)",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre",
    "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0 )",
    "Mozilla/4.0 (compatible; MSIE 5.5; Windows 98; Win 9x 4.90)",
    "Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a",
    "Mozilla/2.02E (Win95; U)",
    "Mozilla/3.01Gold (Win95; I)",
    "Mozilla/4.8 [en] (Windows NT 5.1; U)",
    "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)",
    "HTC_Dream Mozilla/5.0 (Linux; U; Android 1.5; en-ca; Build/CUPCAKE) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
    "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.2; U; de-DE) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/234.40.1 Safari/534.6 TouchPad/1.0",
    "Mozilla/5.0 (Linux; U; Android 1.5; en-us; sdk Build/CUPCAKE) AppleWebkit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
    "Mozilla/5.0 (Linux; U; Android 2.1; en-us; Nexus One Build/ERD62) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
    "Mozilla/5.0 (Linux; U; Android 2.2; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 1.5; en-us; htc_bahamas Build/CRB17) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
    "Mozilla/5.0 (Linux; U; Android 2.1-update1; de-de; HTC Desire 1.19.161.5 Build/ERE27) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
    "Mozilla/5.0 (Linux; U; Android 2.2; en-us; Sprint APA9292KT Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 1.5; de-ch; HTC Hero Build/CUPCAKE) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
    "Mozilla/5.0 (Linux; U; Android 2.2; en-us; ADR6300 Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 2.1; en-us; HTC Legend Build/cupcake) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
    "Mozilla/5.0 (Linux; U; Android 1.5; de-de; HTC Magic Build/PLAT-RC33) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1 FirePHP/0.3",
    "Mozilla/5.0 (Linux; U; Android 1.6; en-us; HTC_TATTOO_A3288 Build/DRC79) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
    "Mozilla/5.0 (Linux; U; Android 1.0; en-us; dream) AppleWebKit/525.10  (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2",
    "Mozilla/5.0 (Linux; U; Android 1.5; en-us; T-Mobile G1 Build/CRB43) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari 525.20.1",
    "Mozilla/5.0 (Linux; U; Android 1.5; en-gb; T-Mobile_G2_Touch Build/CUPCAKE) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
    "Mozilla/5.0 (Linux; U; Android 2.0; en-us; Droid Build/ESD20) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
    "Mozilla/5.0 (Linux; U; Android 2.2; en-us; Droid Build/FRG22D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 2.0; en-us; Milestone Build/ SHOLS_U2_01.03.1) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
    "Mozilla/5.0 (Linux; U; Android 2.0.1; de-de; Milestone Build/SHOLS_U2_01.14.0) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
    "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/525.10  (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2",
    "Mozilla/5.0 (Linux; U; Android 0.5; en-us) AppleWebKit/522  (KHTML, like Gecko) Safari/419.3",
    "Mozilla/5.0 (Linux; U; Android 1.1; en-gb; dream) AppleWebKit/525.10  (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2",
    "Mozilla/5.0 (Linux; U; Android 2.0; en-us; Droid Build/ESD20) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
    "Mozilla/5.0 (Linux; U; Android 2.1; en-us; Nexus One Build/ERD62) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
    "Mozilla/5.0 (Linux; U; Android 2.2; en-us; Sprint APA9292KT Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 2.2; en-us; ADR6300 Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 2.2; en-ca; GT-P1000M Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 3.0.1; fr-fr; A500 Build/HRI66) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
    "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/525.10  (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2",
    "Mozilla/5.0 (Linux; U; Android 1.6; es-es; SonyEricssonX10i Build/R1FA016) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
    "Mozilla/5.0 (Linux; U; Android 1.6; en-us; SonyEricssonX10i Build/R1AA056) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
]

#------------------------------------------------------------------------------------------------------------------------

常见的http状态码

100：继续 客户端应当继续发送请求。客户端应当继续发送请求的剩余部分，或者如果请求已经完成，忽略这个响应。

101： 转换协议 在发送完这个响应最后的空行后，服务器将会切换到在Upgrade 消息头中定义的那些协议。只有在切换新的协议更有好处的时候才应该采取类似措施。

102：继续处理 由WebDAV（RFC 2518）扩展的状态码，代表处理将被继续执行。

200：请求成功 处理方式：获得响应的内容，进行处理（重要）

201：请求完成，结果是创建了新资源。新创建资源的URI可在响应的实体中得到 处理方式：爬虫中不会遇到

202：请求被接受，但处理尚未完成 处理方式：阻塞等待

204：服务器端已经实现了请求，但是没有返回新的信 息。如果客户是用户代理，则无须为此更新自身的文档视图。 处理方式：丢弃

300：该状态码不被HTTP/1.0的应用程序直接使用， 只是作为3XX类型回应的默认解释。存在多个可用的被请求资源。 处理方式：若程序中能够处理，则进行进一步处理，如果程序中不能处理，则丢弃

301：请求到的资源都会分配一个永久的URL，这样就可以在将来通过该URL来访问此资源 处理方式：重定向到分配的URL（永久重定向，重要）

302：请求到的资源在一个不同的URL处临时保存 处理方式：重定向到临时的URL（临时重定向，重要）

304：请求的资源未更新 处理方式：丢弃，使用本地缓存文件（没有发送请求，用的是本地缓存文件，重要）

400：非法请求 处理方式：丢弃

401：未授权 处理方式：丢弃

403：禁止 处理方式：丢弃（重要）

404：没有找到 处理方式：丢弃（重要）

405：请求方式不对（了解）

500：服务器内部错误 服务器遇到了一个未曾预料的状况，导致了它无法完成对请求的处理。一般来说，这个问题都会在服务器端的源代码出现错误时出现。（服务器问题，代码有问题，重要）

501：服务器无法识别 服务器不支持当前请求所需要的某个功能。当服务器无法识别请求的方法，并且无法支持其对任何资源的请求。

502：错误网关 作为网关或者代理工作的服务器尝试执行请求时，从上游服务器接收到无效的响应。

503：服务出错 由于临时的服务器维护或者过载，服务器当前无法处理请求。这个状况是临时的，并且将在一段时间以后恢复。
 	
 	
 #------------------------------------------------------------------------------------------------------------------------    
正则表达式基础知识：
    1.原子，是正则表达式中最基本的组成单位，每个正则表达式中至少要包含一个原子，常见的原子有以下几类：
        1）普通字符作为原子(字母、数字、下划线)。
         
        2）非打印字符作为原子。
            在一些字符串中用于格式控制的符号，、\n(匹配一个换行符)、\t(匹配一个制表符)
             
        3）通用字符作为原子，一个原子可以匹配一类字符。
            \w  匹配任意一个字母、数字或下划线 \W 否
            \d  匹配任意一个十进制数           \D 否
            \s  匹配任意一个空白字符           \S 否
         
        4）原子表。
            定义一组地位平等的原子，然后匹配的时候会取该原子表中的任意一个原子进行匹配，在Python中，原子表由[]表示。
            [xyz]表示匹配里面任一个字符
            [^]代表的是除了中括号里面的原子均可以匹配，比如“[^xyz]py”能匹配“apy”，但是却不能匹配“xpy
         
    2、元字符，就是正则表达式中具有一些特殊含义的字符，比如重复N次前面的字符等。
     
        .  匹配除换行符以外的任一字符     任意匹配元字符
        ^  匹配字符串的开始位置           边界限制元字符
        $  匹配字符串的结束位置           边界限制元字符
        *  匹配前面的原子 > = 0 次          限定符
        ?  匹配前面的原子 0或1 次         限定符
        +  匹配前面的原子 > = 1 次          限定符
        {n, m} 匹配前面的原子 n = < 匹配原子  = < m 限定符
        |  模式选择符                     任选一个匹配
        () 模式单元符                     括号内的部分被当做整体使用
         
    3、模式修正符
     
        在不改变正则表达式的情况下，通过模式修正符改变正则表达式的含义，从而实现一些匹配结果的调整等功能。
        re.I  匹配时忽略大小写
        re.M  多行匹配
        re.L  本地化识别匹配
        re.U  根据Unicode字符及解析字符
        re.S  让"."匹配任一字符，包括换行符
            import re
            pattern1 = "python"
            pattern2 = "python"
            string = "abcdfphp345Pythony_py"
            result1 = re.search(pattern1,string)
            result2 = re.search(pattern2,string,re.I)
            print(result1) None
            print(result2) python
             
    4、贪婪模式与懒惰模式
     
        贪婪模式的核心点就是尽可能多地匹配，而懒惰模式的核心点就是尽可能少地匹配。
            import re
            pattern1 = "p.*y"# 贪婪模式
            pattern2 = "p.*?y"# 懒惰模式
            string = "abcdfphp345pythony_py"
            result1 = re.search(pattern1,string)
            result2 = re.search(pattern2,string)
            print(result1)  php345pythony_py
            print(result2)  php345py
             
            默认贪婪模式转化为懒惰模式方法：p.*y >>> p.*?y  加一个问号
             
    5、正则表达式函数
     
        (1) re.match(pattern,string,flag) 从原字符串起始位置匹配，只返回一个结果
            第一个参数代表对应的正确表达式
            第二个参数代表对应的源字符
            第三个参数是可选参数，代表对应的标志位，可以放模式修正符
                import re
                string = "apythonhellomypythonhispythonourpythonend"
                pattern = ".python."
                result = re.match(pattern,string)
                result2 = re.match(pattern,string).span()
                print(result)   返回匹配详细信息
                print(result2)  返回匹配字符的位置
             
        (2) re.search() 扫描整个字符串进行匹配，只返回一个结果
         
        (3) 全局匹配函数，输出一个列表
            1）使用re.compile（）对正则表达式进行预编译。
            2）编译后，使用findall（）根据正则表达式从源字符串中将匹配的结果全部找出。
                import re
                string = "hellomypythonhispythonourpythonend"
                pattern = re.compile(".python.") #  预编译
                result = pattern.findall(string) #  找出符合模式的所有结果
                #  result = re.compile(pattern).findall(string)
                print(result)
                 
        (4) re.sub()函数
            re.sub(pattern, rep, string, max)
                第一个参数为对应的正则表达式，
                第二个参数为要替换成的字符串，
                第三个参数为源字符串，
                第四个参数为可选项，代表最多替换的次数，如果忽略不写，则会将符合模式的结果全部替换。
                    import re
                    string = "hellomypythonhispythonourpythonend"
                    pattern = "python."
                    result1 = re.sub(pattern,"php",string)
                    #  全部替换
                    result2 = re.sub(pattern,"php",string,2)
                    #  最多替换两次
                    print(result1)
                    print(result2)
 #-----------------------------------------------------------------------------------------------------------------------
 beautifulsoup4解析库
 
 	1）安装 pip install beautifulsoup库
 	
 	2）代码中使用from bs4 import BeautifulSoup
 	
 	3）首先通过BeautifulSoup这个类，将html格式的字符串转化成为一个对象，然后根据对象的相关方法去查找指定的元素
 	
 	4）可以解析本地文件soup = BeautifulSoup(open(文件名, encoding='utf8'), 'lxml')
 		（1）lxml是一个文件解析器，需要安装 pip install lxml，安装失败可以手动安装
 		（2）html.parse	是python自带的一个解析器，lxml比这个效率高
 	
 	5）可以解析网络html文件
 		from bs4 import BeautifulSoup
		soup =  BeautifulSoup(网页字符串内容, 'lxml')
 	
 	6）语法
 		（1）根据标签名查找
 			soup.a	查找第一个符合要求的节点，得到的是对象
 		
 		（2）获取属性
 			soup.a.attr	返回一个字典，里面是所有属性和值
 			soup.a['href']	获取单个属性
 		
 		（3）获取内容
 			soup.a.string
 			soup.a.text
 			soup.a.get_text()
 			如果标签里面还有标签，那么string获取的是空，其他两个获取的是全部的纯文本内容
 			
 		（4）find
 			返回一个对象
 			soup.find('a',id='xxxx')
 			soup.find('a',class='xxxx')
		 (5)find_all
		 	返回一个列表，列表里面全是对象
		 	soup.find_all('a',class='xxxx')
		 	soup.find_all('a',class='xxx',limit=2)	取出前两个 		
 		 (6)select
 		 	选择--选择器
 		 	标签选择器	a
 		 	类选择器		.dudu
 		 	id选择器		#dudu
 		 	属性选择器	input[type=radio]
 			伪类选择器	a:hover
 			后代选择器
 				div a h1		a是div的子节点，子孙节点
 				div > a > h1	a是div的直接子节点
 			组合选择器 	.dudu,#lala,div,p
 			兄弟选择器	ul + div
 			选择器作用：选择一批标签，然后将样式添加给他们
 			返回的永远是一个列表
###############################################################################################################

Xpath选择器

	1）语法
		/	从根节点开始查找
		//	从任意位置开始查找
		.	从当前位置开始查找
		..	从当前节点的父节点开始查找
		@	选取属性
		
		books/book		从books下面查找所有的直接子节点book
		book//book		从books下面查找所有的book节点，包括直接和子孙
		//book			从整个文档中查找所有的book
		books/book[1]	取出第一个符合要求的book直接子节点,下标从1开始
		books/book[last()]	取出最后一本book直接子节点
		books/book[last()-1]	取出倒数第二本book直接子节点
		books/book[position() < 3]	取出前两本book直接子节点
		//title[@lang]	所有拥有lang属性的title节点
		//title[@lang ='eng']	所有拥有lang属性值为eng的title节点
		books/*			所有的直接子节点
		//*				所有节点
		//title[@*]		所有的拥有属性的title节点
		//book/title |	//book/price	两个结果或起来
		
		starts-with
		ends-with
		contains
		
	谷歌浏览器xpath测试插件
		启动与关闭	ctrl+shift+x
		
		1）属性筛选
			
			//input[@id='kw']				
			//span[@class='bg s_ipt']
			
		2)层级和索引选择
		
			//a[@class='mmav'][position() < 3]
			//a[@class="mnav"][last()]
			//a[@class="mnav"][1]
			//div[@id="head"]/div/div[3]/a[2]
			//div[@id="head"]/div/div[@id="u1"]/a[2]
			//div[@id="head"]/div//a[@class="mnav"][2]
		3)获取属性--获取文本
			//div[@id='head']/div//a[@class='mnav'][2]/@href
			//div[@id='head']/div//a[@class='mnav'][2]/text()			
		4)函数
			start-with
				//div[@id='u1']/a[start-with(@href,'https')]
				//div[@id='u1']/a[starts-with(text(),'地')]
			contains
				//div[@id='u1']/a[contains(text(),'多产')]
				//div[@id='u1']/a[contains(@href,'www')]
		谷歌浏览器自带xpath
		
		xpath在代码中的应用
		
		1）可以解析本地文件
			from lxml import etree
			tree = etree.parse(文件名)
			ret = tree.xpath('路径表达式')
			返回的是一个列表
		2）可以解析网络文件
			
			tree = etree.HTML(网络文件字符串内容)
			
			
			
			
###################			
Xath表达式语法
    /  : 从根节点选取，绝对定位。
    // : 从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。
    .  ：选取当前节点
    .. : 选取当前节点的父节点
    @  ： 选取属性
     
    /bookstore/book[1]                  选取属于 bookstore 子元素的第一个 book 元素。
    /bookstore/book[last()]             选取属于 bookstore 子元素的最后一个 book 元素。
    /bookstore/book[last()-1]           选取属于 bookstore 子元素的倒数第二个 book 元素。
    /bookstore/book[position()<3]        选取最前面的两个属于 bookstore 元素的子元素的 book 元素。
    //title[@lang]                      选取所有拥有名为 lang 的属性的 title 元素。
    //title[@lang='eng']                选取所有 title 元素，且这些元素拥有值为 eng 的 lang 属性。
    /bookstore/book[price>35.00]     选取bookstore下的book元素，且其中的price元素的值须大于35.00。
    /bookstore/book[price>35.00]/title   选取bookstore下的book元素的所有title元素，且其中的price元素的值须大于35.00。
     
   选取未知节点
    XPath 通配符可用来选取未知的 XML 元素。
        通配符 描述
        *   匹配任何元素节点。
        @*  匹配任何属性节点。
        node()  匹配任何类型的节点。
         
        /bookstore/*    选取 bookstore 元素的所有子元素。
        //*             选取文档中的所有元素。
        //title[@*]     选取所有带有属性的 title 元素。
         
        //book/title | //book/price 选取 book 元素的所有 title 和 price 元素。
        //title | //price   选取文档中的所有 title 和 price 元素。
        /bookstore/book/title | //price 选取属于 bookstore下book元素的所有title元素，以及文档中所有的price元素。
		
######################################################################################################################

PyQuery选择器

	1）安装 pip install pyquery
	
	2) 初始化
		
		1)解析网页字符串
		from pyquery import PyQuery as pq
		doc = pq(html)
		
		2）url初始化
			
		from pyquery import PyQuery as pq
		doc = pq(url='http://www.baidu.com')
		doc('li')
 		
 		3)文件初始化
 		
 		from pyquery import PyQuery as pq
 		doc = pq(filename = 'demo.html')
 		doc('li')
 		
 		4) 基本css选择器
 		
 		from pyquery import PyQuery as pq
 		doc = pq(html)
 		doc('#dudu .dudu li')
 		
 		5) 查找元素
 			
 		from pyquery import PyQuery as pq
 		doc = pq(html)
 		items = doc('.dudu')
 		lis = items.find('li')
 		
 		lis = items.children()	所有的后代
 		
 		lis = items.children('.dudu')	后代里面的类属性为dudu的节点
 		
 		6）父元素
 		
 		from pyquery import PyQuery as pq
 		doc = pq(html)
 		items = doc('.list')
 		contains = items.parent() 返回直接父节点
 		
 		contains = items.parent()	返回所有的父节点
 		
 		contains = items.parents('.wrap') 返回父节点中类为wrap的节点
 		
 		7）兄弟元素
 		
 		from pyquery import PyQuery as pq
 		doc = pq(html)
 		
 		li = doc('.dudu span a')
 		
 		patten = li.sibilings()	返回所有的兄弟节点
 		
 		patten = li.sibilings('.dudu') 返回兄弟节点中类为dudu的节点
 		
 		8）遍历
 		
 		from pyquery import PyQuery as pq
 		doc = pq(html)
 		
 		单个遍历
 		li = doc('.dudu')
 		print(li)		
 		
 		多个遍历
 		lis = doc('.dudu').items()
 		for i in lis:
 			print(i)
 		
 		9）获取信息
 		
 		获取属性
 		from pyquery import PyQuery as pq
 		doc = pq(html)
 		
 		a = doc('.dudu')
 		s = a.attr('href')
 		s = a.attr.href
 		
 		获取文本
 		
 		s = a.text()
 
 		10)获取html
 		
 		from pyquery import PyQuery as pq
 		doc = pq(html)
 		
 		li = doc('.dudu')
 
 		s = li.html()
 		
 		11)Dom操作
 		
 			(1)addclass,removeclass
 		
 			from pyquery import PyQuery as pq
 			doc = pq(html)
 		
 			li = doc('.dudu-1.lala')
 		
 			li.removeclass('lala')	删除lala这个类
 		
 			li.addclass('lala')		添加lala这个类
 		
 			(2)attr,css
 			
 			from pyquery import PyQuery as pq
 			doc = pq(html)
 			
 			li = doc('.dudu')
 			
 			li.attr('name','link')		给li节点添加name属性
 			
 			li.css('font-size','14px')	给li节点添加css属性
 
 			（3）remove
 			
 			from pyquery import PyQuery
 			doc = pq(html)
 			
 			dudu = doc('.dudu')
 			
 			dudu.find('p').remove()	找到p标签，删除标签和其内容
 	
 		11）伪类选择器
 		
 		from pyquery import PyQuery
 		doc = pq(html)
 		
 		li = doc('li:first-child')	第一个li
 			
 		li = doc('li:last-child')	最后一个li
 	
 		li = doc('li:nth-child(2)')	第2个li
 		
 		li = doc('li:gt(2)')		
 		
 		li = doc('li:nth-child(2n)')	第2n个li
 		
 		li = doc('li:contains(second)')	
 

###################################################################################################

jsonpath

	1)开始
		
		import json
		import jsonpath
		
		fp = open('book.json','r',enconding = 'utf-8')
		string = fp.read()
		fp.close()
		
		将json字符串转换为python对象
		
		obj = json.loads(string)
 		
 		通过jsonpath获取数据
 		
 		ret = jsonpath.jsonpath(obj, '$.store.book[*].author')
		ret = jsonpath.jsonpath(obj, '$..author')
		ret = jsonpath.jsonpath(obj, '$.store.*')
		ret = jsonpath.jsonpath(obj, '$.store..price')
		ret = jsonpath.jsonpath(obj, '$..book[2]')
		ret = jsonpath.jsonpath(obj, '$..book[(@.length-1)]')
 
 
##################################################################################################################


selenium+phantomjs

	1）安装selenium+phantomjs
	
	pip install selenium
	
		(1) slenium操作谷歌浏览器其实是操作谷歌浏览器的驱动，由驱动再去驱动浏览器
		
		谷歌驱动下载地址
		http://chromedriver.storage.googleapis.com/index.html
		http://npm.taobao.org/mirrors/chromedriver/
 		谷歌驱动版本映射表
 		http://blog.csdn.net/huilan_same/article/details/51896672
 	####操作谷歌步骤###################
 		from selenium import webdriver
		import time
		# 创建一个浏览器对象
		path = r'C:\Users\ZBLi\Desktop\1805\day06\ziliao\chromedriver.exe'
		driver = webdriver.Chrome(executable_path=path)
		# 让浏览器打开百度
		url = 'http://www.baidu.com/'
		driver.get(url)
		# time.sleep(5)
		driver.implicitly_wait(10)
		'''
		下面的操作依赖上面的响应，所以每次只要是耗时的操作，都需要停顿
		（1）显示等待
		time.sleep(10)     
		一直等待10s
		（2）隐示等待
		driver.implicitly_wait(10)
		最多等待10s
		动态加载
		1、请求，得到的是空的html内容
		2、在发送ajax请求，得到json格式数据
		3、执行里面的js代码，根据DOM操作添加html内容
		'''

		# 找到输入框
		my_input = driver.find_element_by_id('kw')
	'''
		find_element_by_id
		find_element_by_xpath
		find_elements_by_xpath
		find_element_by_class_name
		find_element_by_css_selector
		find_element_by_link_text
		find_elements_by_class_name
		find_elements_by_css_selector
		find_elements_by_link_text
		'''
		# 向这个框里面写内容
		my_input.send_keys('清纯美女')
		time.sleep(3)
	
		# 查找百度一下按钮
		button = driver.find_element_by_id('su')
		button.click()
		time.sleep(5)

		# 查找指定链接
		a_href = driver.find_elements_by_link_text('清纯美女_海量精选高清图片_百度图片')[0]
		a_href.click()
		time.sleep(10)
		# 退出浏览器
		driver.quit()
 		
 	（2）phantomjs是一款无界面浏览器，爬虫常用这款浏览器
 		
 		 数据在html中
 		 
 		 不在html中，在接口中，分析接口
 		 返回的一般json数据，是html数据
 		 
 		 数据在js文件中，使用正则表达式解析
 		 
 		 当情况更加复杂！
 		 
 		 终极利器，但也有缺点，效率太低，不适合大批量的数据抓取
 		 
 		 selenium操作phantomjs
 	##########操作phantomjs步骤######################
 		 from selenium import webdriver
		import time

		'''
		\n \r \t
		'''
		path = r'C:\Users\ZBLi\Desktop\1805\day06\ziliao\phantomjs-2.1.1-windows\bin\phantomjs.exe'
		driver = webdriver.PhantomJS(executable_path=path)

		url = 'http://www.baidu.com/'
		driver.get(url)
		time.sleep(5)
		# 拍照片方式记录走到哪了
		driver.save_screenshot('./png/baidu.png')

		driver.find_element_by_id('kw').send_keys('你好')
		time.sleep(2)
		driver.find_element_by_id('su').click()
		time.sleep(5)
		driver.save_screenshot('./png/qizhi.png')

		driver.quit()
 		 
 		 目的：phantomjs可以得到执行完js后的网页代码
	
	3）得到执行完js的页面
		from selenium import webdriver
		import time

		path = r'C:\Users\ZBLi\Desktop\1805\day06\ziliao\phantomjs-2.1.1-windows\bin\phantomjs.exe'
		driver = webdriver.PhantomJS(executable_path=path)

		url = 'https://movie.douban.com/typerank?type_name=%E7%88%B1%E6%83%85&type=13&interval_id=100:90&action='
		driver.get(url)
		# 一般都是7-15s
		time.sleep(7)
		# driver.implicitly_wait(20)

		# 将网页内容保存到文件中
		# with open('douban1.html', 'w', encoding='utf8') as fp:
			# 得到字符串格式内容
			# fp.write(driver.page_source)

		# 解析内容
		# from lxml import etree
		# tree = etree.HTML(driver.page_source)
		driver.save_screenshot('./png/douban.png')

		driver.quit()
	4）模拟滚动条滚动（代码）
		from selenium import webdriver
		import time

		path = r'C:\Users\ZBLi\Desktop\1805\day06\ziliao\phantomjs-2.1.1-windows\bin\phantomjs.exe'
		driver = webdriver.PhantomJS(executable_path=path)

		url = 'https://movie.douban.com/typerank?type_name=%E7%88%B1%E6%83%85&type=13&interval_id=100:90&action='
		driver.get(url)
		# 一般都是7-15s
		time.sleep(7)
		driver.save_screenshot('./png/douban1.png')

		# 模拟滚动条滚动到底部   document.documentElement.scrollTop
		js = 'document.body.scrollTop=10000'
		driver.execute_script(js)
		time.sleep(5)
		driver.save_screenshot('./png/douban2.png')

		driver.quit()
	 
	 5）无界面谷歌浏览器
		 
	 	from selenium import webdriver
		import time
		from selenium.webdriver.chrome.options import Options
		chrome_options = Options()
		chrome_options.add_argument('--headless')
		chrome_options.add_argument('--disable-gpu')

		path = r'C:\Users\ZBLi\Desktop\1805\day06\ziliao\chromedriver.exe'
		driver = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)
		driver.get('http://www.baidu.com/')
		time.sleep(3)
		driver.save_screenshot('./png/guge.png')

		driver.quit()
		
	 6）无界面火狐浏览器
	 	
	 	from selenium import webdriver
		import time

		firefox_options = webdriver.FirefoxOptions()
		firefox_options.set_headless()
		firefox_options.add_argument('--disable-gpu')
		path = r'C:\Users\ZBLi\Desktop\1805\day06\ziliao\geckodriver.exe'
		driver = webdriver.Firefox(executable_path=path, firefox_options=firefox_options)

		driver.get('http://www.baidu.com/')

		time.sleep(5)
		driver.save_screenshot('./png/huohu.png')

		driver.quit()
	  
 headlesschrome
 
 phantomjs是无界面浏览器
 
	谷歌无界面模式
 	from selenium.webdriver.chrome.options import Options
	chrome_options = Options()
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--disable-gpu')

	selenium驱动火狐浏览器
	下载火狐浏览器驱动
	https://github.com/mozilla/geckodriver/releases
 	版本映射
 	https://blog.csdn.net/yinshuilan/article/details/79730239
 	
 	代码设置无界面模式
 	firefox_options = webdriver.FirefoxOptions()
	firefox_options.set_headless()
	firefox_options.add_argument('--disable-gpu')
 
#---------------------------------------------------------------------------------------------------------------
多任务

	1）多个任务同时进行
		
		四个关键字
		
		同步		执行完任务a才能执行任务b
		异步		执行完任务a的同时也在执行b
		并行		任务a和任务b真的是在同时进行			真异步
		并发		任务a和任务b在一段时间内在同时进行	假异步
	2）多进程
		
		启动一个软件，系统就会分配一个进程
		代码中，写好的代码没有运行之前称为程序，运行的时候就是一个进程
		以前写的代码都只有一个主线程，需要通过主线程来创建其他的子线程
		
		进程创建
			(1) 面向过程
			
				p = process(target = xxx,args=(xxx,))
				tatget:进程创建后要执行的函数
				args:主进程给子进程传递的参数
				p.start()	启动进程
				p.join()	让主进程等待
				os.getpid()	获取当前进程id号
				os.getppid() 获取父进程id号
			（2）面向对象
				
				class myprocess(process):
					def run(self):
						pass
						
				进程启动执行run方法，如果需要传参，需要重写构造方法，在构造方法中要记得手动调用父类的构造方法
				进程之间不共享局部变量
				
				进程之间不共享全局变量
				
				进程之间不共享任何数据、
				
				进程池：
					进程是不是创建的越多越好？
					例如：给一个文件夹，文件夹里面有100个文件
					copy(src,dst)
					不是绝对的
					要开辟多少个进程呢？
					开辟5个进程，实现100个文件的拷贝
					最多开辟5个进程，这个东西称之为进程池
		3）多线程
			
			如何理解线程？
			多任务--多进程，多线程
			
			进程和线程的区别
			（1）线程属于进程，一个线程只能属于一个进程，一个进程里面可以由多个线程
			（2）系统分配资源的基本单位是线程
			（3）系统调度资源的基本单位是线程
			创建线程
			
			（1）面向过程创建
				t = threading.Thread(target=xxx, name=xxx, args=(xxx,))
				target: 线程启动要执行的函数
				name: 给线程起名字   threading.current_thread().name
				args: 主线程给子线程传递参数
				t.start()
				t.join()
			（2）面向对象创建
				
				线程之间不共享局部变量
				
				线程之间共享全局变量
				
				线程安全，线程同步
				
					a += 1
					多个线程往同一个文件中写内容
					锁，独自使用，开锁
					在操作之前加锁，然后操作，释放锁
					上锁的时候是抢的
					牺牲了性能
					from threading import Lock
					# 创建一把锁, 多个线程使用一把锁
					lock = Lock()
					# 上锁
					lock.acquire()
					# 释放锁
					lock.release()
		4）队列
			
			队列特点：先进先出
			栈：先进后出
			程序中：  from queue import Queue
						q = Queue(5)
						q.put(xxx)  添加元素
						q.get()     获取元素
						q.full()    判断队列是否满
						q.empty()   判断队列是否为空
						q.qsize()   得到队列中元素的个数

		5）多线程爬虫
			线程和队列：生产者消费者模型
			while 1:
				生产数据
				消费数据

			生产数据线程
				数据队列
			消费数据线程
			
			到爬虫中
			for page in range(1,11):
				拼接url,发送请求，得到响应
					数据队列
				解析响应，保存数据

 #--------------------------------------------------------------------------------------------------------------
 
 无状态HTPP
	http协议，发请求-给响应   发请求-给响应   
	
	无状态特性
		1）http的无状态是指http协议对事物是没有记忆能力的，也就是说不知道客户端是什么状态
		2）当我们向服务器发送请求时，服务器解析此请求，然后返回对应的响应，服务器负责完成这个过程，这个过程是完全独立的，服务器不会记录前后状态的变化，缺少状态记录
		3）如果后续需要处理前面的信息，则必须重传，这就需要额外传递一些前面的请求
		
	会话和cookies的出现
		1）会话在服务端，也就是网站的服务器，用来保存用户的会话信息
		2）cookies在客户端，也可以理解为浏览器端
		3）有了cookies，浏览器下次访问网页时就会自动附带上它发送给服务器，服务器会识别cookies并鉴定出是哪个用户，然后再判断是否是登录状态，然后返回对应的响应
			
	有问题的。
		登录请求-响应
		登录后请求-响应
	这个问题如何解决？
		引入了cookie，会话机制
		登录请求-响应    响应的头部会有一些信息发给客户端，缓存起来
		登录后请求-响应  请求的时候，将你保存的信息带过来即可
	session
		信息的保存，cookie保存到客户端，session，信息保存到服务端，sessionid保存到客户端
	抛出问题：
		一个页码有一个url，登录后的页码（个人资料页）也有一个url
	如何通过代码访问登录后的页面（个人资料页）
		http://www.renren.com/960481378/profile
		（1）拿到cookie
			通过浏览器抓包，抓取访问登陆后页面的cookie，写到代码中即可
		（2）模拟登录
			先模拟发送post，在发送get
			保存和携带cookie的功能，搞cookiejar，看代码
#-----------------------------------------------------------------------------------------------------------------
                 
Cookie与Session:
 
    如果是通过Cookie保存会话信息，此时会将所有的会话信息保存在客户端.
    如果是通过Session保存会话信息，会将对应的会话信息保存在服务器端.
    使用Session的方式来保存会话信息，大部分的时候，还是会到Cookie.
     
    使用Python处理Cookie，在Python3中可以使用Cookiejar库进行处理，而在Python2则可以使用Cookielib库进行处理。
    进行Cookie处理的一种常用思路如下：
     
        1）导入Cookie处理模块http.cookiejar。
         
        2）使用http.cookiejar.CookieJar（）创建CookieJar对象。
         
        3）使用HTTPCookieProcessor创建cookie处理器，并以其为参数构建opener对象。
         
        4）创建全局默认的opener对象。
            import urllib.request
            import urllib.parse
            import http.cookiejar
            url = "http:// bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash = L768q"
            postdata = urllib.parse.urlencode({ "username":"weisuen", "password":"aA123456" }).encode('utf-8')
            req  =  urllib.request.Request(url,postdata)
            req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/ 537.36
                (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
            #  使用http.cookiejar.CookieJar()创建CookieJar对象
            cjar = http.cookiejar.CookieJar()
            #  使用HTTPCookieProcessor创建cookie处理器，并以其为参数构建opener对象
            opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
            #  将opener安装为全局
            urllib.request.install_opener(opener)
            file = opener.open(req)
            data = file.read()
            file = open("D:/Python35/myweb/part5/3.html","wb")
            file.write(data) file.close()
            url2 = "http:// bbs.chinaunix.net/"
            data2 = urllib.request.urlopen(url2).read()
            fhandle = open("D:/Python35/myweb/part5/4.html","wb")
            fhandle.write(data2)
            fhandle.close()
             
    链接爬虫实例：
        import re
        import urllib.request
        def getlink(url):
            # 模拟成浏览器
            headers = ("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/ 537.36 (KHTML, like Gecko)
                Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0")
            opener = urllib.request.build_opener()
            opener.addheaders  =  [headers]
            # 将opener安装为全局
            urllib.request.install_opener(opener)
            file = urllib.request.urlopen(url)
            data = str(file.read())
            # 根据需求构建好链接表达式
            pat = '(https?:// [^\s)";]+\.(\w|/)*)'
            link = re.compile(pat).findall(data)
            # 去除重复元素
            link = list(set(link))
            return link
             
        # 要爬取的网页链接
        url = "http:// blog.csdn.net/"
        # 获取对应网页中包含的链接地址
        linklist = getlink(url)
        # 通过for循环分别遍历输出获取到的链接地址到屏幕上
        for link in linklist:
            print(link[0])
     
队列：
    import queue
    a = queue.Queue()
    a.put('python')
    a.task_done()
    a.get()
     
多线程加队列微信网络爬虫：
 
    1）总体规划好程序执行的流程，并规划好各线程的关系与作用。本项目中将划分为3个线程。
     
    2）线程1专门获取对应网址并处理为真实网址，然后将网址写入队列urlqueue中，该队列专门用来存放具体文章的网址。
     
    3）线程2与线程1并行执行，从线程1提供的文章网址中依次爬取对应文章信息并处理，处理后将我们需要的结果写入对应的本地文件中。
     
    4）线程3主要用于判断程序是否完成。因为在此若没有一个总体控制的线程，即使线程1、2执行完，也不会退出程序，这不是我们想要的结果，
       所以我们可以建立一个新的线程，专门用来实现总体控制，每次延时60秒，延时后且存放网址的队列urlqueue中没有了网址数据，说明
       线程2已经GET完全部的网址了（不考虑线程1首次无法将网址写入队列的特殊情况，如果爬取没问题，60秒的时间完全足够执行完第一次
       爬取与写入的操作。也不考虑线程2爬取完网址但线程1尚未执行完下一次写入网址的操作的情况，因为线程1会比线程2快很多，即使线程1
       延时较长时间等待线程2的执行，正常情况下，线程1速度仍会比线程2快。），即此时已经爬取完所有的文章信息，所以此时可以由线程3
       控制退出程序。
        
    5）在正规的项目设计的时候，我们会希望并行执行的线程执行的时间相近，因为这样整个程序才能达到更好的平衡，如果并行执行的线程
       执行时间相差较大，会发生某一个线程早早执行完成，而另一些线程迟迟未完成的情况，这样显然程序不够平衡，自然效率以及线程设
       计有待改进。从这一点来说，本项目仍然有完善的空间。
        
    6）建立合理的延时机制，比如在发生异常之后，进行相应的延时处理。再比如也可以通过延时机制让执行较快的线程进行延时，等待一下
       执行较慢的线程。
        
    7）建立合理的异常处理机制。
     
浏览器伪装技术：
 
    常见的反爬机制：
       1）通过分析用户请求的Headers信息进行反爬虫。
       2）通过检测用户行为进行反爬虫，比如通过判断同一个IP在短时间内是否频繁访问对应网站等进行分析。
       3）通过动态页面增加爬虫爬取的难度，达到反爬虫的目的。
     
    针对的破解方法：
        1）构造请求头，模拟浏览器登录
        2）使用代理服务器并经常借还代理服务器。
        3）利用工具：selenium + plantomJS 。
         
    常见头信息中的字段：
        常见字段1
            Accept：·Accept字段主要用来表示浏览器能够支持的内容类型有哪些。
                text/html，·text/html表示HTML文档。
                application/xhtml+xml，·application/xhtml+xml表示XHTML文档。
                application/xml；·application/xml表示XML文档。
                q=0.9，*/*；q=0.8·q代表权重系数，值介于0和1之间。
            所以这一行字段信息表示浏览器可以支持text/html、application/xhtml+xml、application/xml、*/*等内容类型，
            支持的优先顺序从左到右依次排列。
             
        常见字段2
            Accept-Encoding：·Accept-Encoding字段主要用来表示浏览器支持的压缩编码有哪些。
            gzip，·gzip是压缩编码的一种。
            deflate·deflate是一种无损数据压缩算法。
            这一行字段信息表示浏览器可以支持gzip、deflate等压缩编码。
             
        常见字段3
            Accept-Language：·Accept-Language主要用来表示浏览器所支持的语言类型。
            zh-CN，zh；·zh-CN表示简体中文语言，zh表示中文，CN表示简体。
            q=0.8，en-US；·en-US表示英语（美国）语言。
            q=0.5，en；·en表示英语语言。
            q=0.3
            所以之一行字段表示浏览器可以支持zh-CN、zh、en-US、en等语言。
             
        常见字段4
            User-Agent：Mozilla/5.0（Windows NT 6.1；WOW64；rv：47.0）Gecko/20100101 Firefox/47.0
            User-Agent字段主要表示用户代理，服务器可以通过该字段识别出客户端的浏览器类型、浏览器版本号、客户端的
            操作系统及版本号，网页排版引擎等客户端信息。所以我们之前要模拟浏览器登录，主要以伪造该字段进行。
            ·Mozilla/5.0表示浏览器名及版本信息。
            ·Windows NT 6.1；WOW64；rv：47.0表示客户端操作系统对应信息。
            ·Gecko表示网页排版引擎对应信息。
            ·firefox自然表示火狐浏览器。
            所以这一行字段表示的信息为对应的用户代理信息是Mozilla/5.0（Windows NT 6.1；WOW64；rv：47.0）Gecko/
            20100101 Firefox/47.0。
             
        常见字段5
            Connection：keep-alive·Connection表示客户端与服务器的连接类型，对应的字段值主要有两种：
                ·keep-alive表示持久性连接。
                ·close表示单方面关闭连接，让连接断开。
            所以此时，这一行字段表示客户端与服务器的连接是持久性连接。
             
        常见字段6
            Host：www.youku.com·Host字段表示请求的服务器网址是什么，此时这一行字段表示请求的服务器网址是www.youku.com。
             
        常见字段7
            Referer：网址·Referer字段主要表示来源网址地址，比如我们从http://www.youku.com网址中访问了该网址下的子
                页面http://tv.youku.com/?spm=0.0.topNav.5～1～3！2～A.QnQOEf，那么此时来源网址为http://www.youku.com，
                即此时Referer字段的值为http://www.youku.com。
         
        import urllib.request
        import http.cookiejar
        #注意，如果要通过fiddler调试，则下方网址要设置为"http:// www.baidu.com/"
        url= "http:// www.baidu.com"
        headers={ "Accept":" text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                    "Accept-Encoding":" gb2312,utf-8",
                    "Accept-Language":" zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
                    User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36
                            (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/ 537.36 SE 2.X MetaSr 1.0",
                    "Connection": "keep-alive",
                    "referer":"baidu.com"}
        cjar=http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
        headall=[]
        for key,value in headers.items():
            item=(key,value)
            headall.append(item)
        opener.addheaders = headall
        urllib.request.install_opener(opener)
        data=urllib.request.urlopen(url).read()
        fhandle=open("D:/Python35/myweb/part8/3.html","wb")
        fhandle.write(data)
        fhandle.close()
             
#--------------------------------------------------------------------------------------------------------------------
常用反爬虫和对应策略

	1）检测UA用户请求头
		通过检测请求头的User-agent来判断是否是爬虫
		
		解决方法：在请求中加入headers,可以引入random，随机抽取ua
	
	2)检测ip地址
		通过检测用户的请求ip地址，来检测用户的请求次数，限制爬虫
		
		解决方法：
				（1）可以在发送请求的时候，设置time.sleep(3)等待时间，友好爬虫
				（2）手动维护免费ip代理池
				（3）使用付费代理，使用规定的接口
	3）网页懒加载
		
		显示的网页右键检查是正常显示的，但是使用解析器解析的时候，解析不到
		
		解决方法：网页解析要以下载下来的网页源代码为准，网页懒加载只是将可视区的代码变化为正确的
				一般源代码中会将标签的属性改动（src-->src2）
	4)ajax加载
		通过不刷新整个网页(url)加载数据，局部刷新
		
		解决方法：谷歌浏览器右键检查，触发ajax加载，捕获接口(XHR)，查看是get还是post请求，
				一般get请求不需要携带请求头，post则大部分需要携带请求头
				请求下来的数据一般是标准的json格式文件，通过jsonpath解析即可
	5）js动态加载
		网页正常刷新，非ajax加载，网页源代码也很简短，基本没有核心网页标签，基本可以判断是js加载    
		
		解决方法：谷歌右键检查，触发js记载，捕获接口，请求接口
				下载下来的数据一般不是json格式，只能存为字符串，通过正则表达式解析字符串的内容
	6）登录验证
		有些网站的内容只有登录才能访问
		
		解决方法：
				（1）抓取登录时传送的数据包，手动构造和提交表单
				（2）抓取已经登录成功的网站cookies,提交时带上cookies
	
	7）验证码
		（1）普通静态图片验证码
			
			解决方法：
				（1）可以通过手动输入
				（2）通过光学ocr识别
					--识别率低---一般是80%
					指令识别，tesseract 图片名字 lala  0%
					代码识别，60%
					pip install pytesseract
					pip install pillow
				（3）通过机器学习
					使用tensorflow进行图片的识别
					提供大量的训练数据集
				 (4)打码平台
				 	 云打码
		（2）极验验证码
			
			1）拖动验证码
				解决方法：可以使用selenium控制鼠标的拖动完成，人工拖动
			2）动态验证码
				解决方法：打码平台或手动输入
		
		（3）12306验证码识别
			解决方法，使用深度学习进行验证码的识别
	8）字体加密
		
		（1）一套字体加密
			解决方法：将字体下载下来，找到对应的关系
		（2）多套字代加密
			解决方法：将3-4套字体下载下来，根据字形找到对应的关系
					设置一个字典，每次比对字形即可
			起点中文网字体加密示例代码：
				import requests
				import re
				from lxml import etree
				from fontTools.ttLib import TTFont
				from io import BytesIO

				url = 'https://book.qidian.com/info/1012932890'
				headers = {
					'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
				}
				r = requests.get(url=url, headers=headers)

				tree = etree.HTML(r.text)
				# 先拿到span的class名字
				classname = tree.xpath('//div[contains(@class,"book-info")]/p/em/span/@class')[0]
				# 拼接得到字体的url
				font_url = 'https://qidian.gtimg.com/qd_anti_spider/{}.ttf'.format(classname)
				
				# 得到span的内容
				pattern = re.compile(r'<span class="' + classname + '">(.*?)</span>')
				ret = pattern.search(r.text)
				#    &#100301;&#100302;&#100297;&#100295;&#100304;
				string = ret.group(1)

				# 将字体文件下载下来
				r_font = requests.get(url=font_url, headers=headers)
				# filename = font_url.split('/')[-1]
				# with open(filename, 'wb') as fp:
				# 	fp.write(r_font.content)
				
				# 打开这个字体
				font = TTFont(BytesIO(r_font.content))
				dic = font.getBestCmap()
				# 关闭这个字体
				font.close()
				
				print(string)
				print(dic)
				font_dic = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8',
				 'nine': '9', 'zero': '0', 'period': '.'}
				# 将string按照分号进行切割
				lt = string.split(';')[:-1]
				number = ''
				for code in lt:
					code = code.lstrip('&#')
					char_code = dic[int(code)]
					number_code = font_dic[char_code]
					number += number_code
				print(number)
					
		
		
#---------------------------------------------------------------------------------------------------------------------
python爬虫框架

pyspider爬虫框架

		1）主要特点：使用python语言编写脚本
				功能强大的webui，包括脚本编辑器，任务监视器，
				项目管理器和结果查看器
				和phantomjs配合抓取js动态界面

		2）安装：pip install pyspider
			    pip install phantomjs
			
			ubantu系统失败尝试安装依赖包：
			apt-get install python python-dev python-distribute 			python-piplibcurl4-openssl-dev libxml2-dev 			
			libxslt1-dev python-lxml
			libssl-dev zlib1g-dev		
						
		   运行：pyspider
		   
		   默认开启5000端口
		   
		   phantomjs不支持gzip,不设置accept-encoding标头gzip
		   
		   如何删除项目，设置delete组，并把状态改为stop
		
	3)pyspider框架概览
		
		（1）pyspider体系结构和组件的概述以及内部发生的数据流   
		   
		   	组件通过消息队连接，每个组件（包括消息队列）都在自己的进程或线程
		   	中运行，并且可以替换，这意味着，当进程缓慢时，你可以拥有很多处理
		   	器实例并充分利用多个cpu，或部署到多台计算机
		   	
		 （2）组件（scheduler）	
		   	调度
		   	http://docs.pyspider.org/en/latest/Architecture/
		   	调度程序从处理器的newtask_queue接受任务，确定任务是新任务还是需
		   	要重新爬网，根据优先级对任务进行排序，并将其提供给具有流量控制的提
		   	取器(令牌桶算法)，处理定期任务，丢失任务和失败的任务，然后重试
		   		#令牌桶算法调度：
		   			令牌桶算法是网络流量整形和速率控制中最常使用的一种算法，典型的情况下
					令牌桶算法用来控制发送到网络上的数据的数目，并允许突发数据的发送
					
					简介：
						在网络传输中，为了防止网络阻塞，需限制流出网络的流量，使流量以比
						较均匀的速度向外发送，令牌桶算法就实现了这个功能，可控制发送到网
						络上数据的数目，并允许突发数据的发送。
						
						大小固定的令牌桶可自行以恒定的速率源源不断不断地产生令牌。如果令牌不被消耗，或者被消耗的速度小于产生的速度	
						,令牌就会不断地增加，直到把桶填满，后面再产生的令牌就会从桶中溢出，
						最后桶中可以保存的最大令牌数永远不会超过桶的大小，
						   			
						传送到令牌桶的数据包需要消耗令牌，不同大小的数据包，消耗的令牌数量不一样.
						令牌桶这种控制机制基于令牌桶是否存在令牌来指示什么时候可以发送流量，令牌桶中的每一个令牌都代表一个字节，
						如果令牌桶中存在令牌，则允许发送流量；如果令牌桶中不存在令牌，则不允许发送流量，因此，
						如果突发门限被合理地配置并且令牌桶中有足够的令牌，那么流量就可以以峰值速率发送。
						令牌桶算法的基本过程如下：
								假如用户配置的平均发送速率为r,则每隔1/r秒一个令牌被加入，；
								假设桶最多可以存发b个令牌，如果令牌到达时令牌桶已经满了，那么这个令牌会被丢弃；
								当一个n个字节的数据包，就从令牌桶中删除n个令牌，并且数据包被发送到网络；
								如果令牌桶少于n个令牌，那么不会那么不会删除这个令牌，并且认为这个数据包在流量限制之外；
								算法允许最长b个字节的突发，但从长远运行的结果看，数据包的速率被限制成常量r,对于在流量限制之外数据包可以以不同的方式处理：
										他们可以被丢弃；
										他们可以排放在队列中以便当令牌桶累积了足够多的令牌再传输，；
										他们可以继续发送，但需要做特殊标记，网络过载的时候，将这些特殊标记的包丢弃；
					
					
					注意!!!：令牌桶算法不能与另外一种常见算法“漏桶算法（Leaky Bucket）”相混淆。这两种算法的主要区别在于“漏桶算法”能够强行限制数据的传输速率，
					而“令牌桶算法”在能够限制数据的平均传输速率外，还允许某种程度的突发传输。
					在“令牌桶算法”中，只要令牌桶中存在令牌，那么就允许突发地传输数据直到达到用户配置的门限，因此它适合于具有突发特性的流量
					
					
		   3)提取程序(fetcher)
		   
		   		fetcher负责获取网页，然后将结果发送给处理器，对于动态加载的fetcher支持数据url
		   		和由js呈现的页面（通过phantomjs）,可以通过API脚本控制获取方法，标头，cookie,
		   		代理，etag等
		   		
		   		phantomjs调度规则
		   		
		   		scheduler  ---->  fetcher  ---->  processor
		   				     |
		   				 phantomjs
		   			             |
		   				 internet
		   						 
		   	4)处理器(processor)
		   		
		   		处理器负责运行用户编写的脚本来解析和提取信息，你的脚本在无限制的环境中运行，
		   		虽然我们由各种工具（如pyquery）可供你提取信息和链接，
		   		但你可以使用任何想要处理响应的内容，详情可以参考api
		   		
		   		处理器将捕获异常和日志，发送状态（任务跟踪）和新任务scheduler，将结果发送到
		   		result worker
		   		
		   		
		   	5)结果（Result Worker(可选)）
		   		
		   		从processor接受结果，pyapider有一个内置的结果工作器来保存结果resultdb
		   		覆盖它以根据你的需求处理结果，改写他
		   		
		   	6）webUI
		   	
		   		这是pyspider框架最令人激动地部分
		   		
		   		包含：
		   			（1）脚本编辑器，调试器
		   			（2）任务监视器
		   			（3）结果查看器
		   			
		   		也许webUI是pyspider最吸引人的部分，有了这个功能强大webui，
		   		你可以像pyspider一样逐步调试脚本，启动或停止项目，查找哪个项目出错了，
		   		然后使用调试器再次尝试
		   	7）数据流(dataflow）
		   		
		   		pyspider中的数据流如下图所示：
		   			
		   			（1）当你按下webui上的run按钮，就会执行on_start方法，
		   				每个脚本都有一个叫做callback的回调函数，
		   				on_start作为项目条目，将新任务提交给scheduler调度器
		   			（2）调度程序将on_start任务调度为数据url作为fetcher的常规任务
		   			
		   			（3）fetcher发出请求并对其作出响应（对于数据url这是一个虚假的请求与响应，
		   				但与其他正常任务没有区别 ）然后提供给处理器
		   			
		   			（4）处理器调用该on_start方法并生成一些新的url以进行爬网，处理器向
		   				scheduler发送一条消息，表示此任务已经完成，新任务通过消息队列发送到
		   				scheduler(on_start在大多数情况下，这里没有结果，如果有结果，
		   				处理器将他们发送到result_queue)
		   			
		   			（5）调度程序接收新任务，在数据库中查找，确定任务是新的还是需要重新爬网，
		   				如果是，则将他们放入任务队列，按顺序发送任务
		   			
		   			
		   			（6）这个过程重复（从第3步开始）并且网址空之前不会停止。
		   				调度程序将检查定期任务以抓取最新数据。
		   			
		   						   
#------------------------------------------------------------------------------------------------------------------


定向爬虫步骤与策略
 
    爬取步骤：
        (1)理清爬取目标
        (2)设置网址过滤规则
        (3)设置内容采集规则
        (4)规划采集任务
        (5)将采集结果进行相应的修正
        (6)对结果进行进一步处理
 
    信息筛选策略：
        (1)通过正则表达式筛选
        (2)通过Xpath表达式筛选
        (3)通筛选过xslt
 
常用python爬虫框架：
 
    (1)scrapy框架
     
    (2)crawley框架
        crawlspider链接提取器：
            rules= （Rule(Linktractor(allow=r'Items/', deny='', restrice_xpaths='', allow_domains=('...')...),
                        callback='prse_item）, follow=True),)
        链接提取器主要负责将response响应中符合条件的链接提取出来LinkEtractor：
            allow: 提取符合对应正则表达式的链接
            deny : 不提取符合对应正则表达式的链接
            restrict_xpaths: 使用Xpath表达式与allow共同作用提取出同时符合对应Xpath表达式和正则表达式的链接
            allow_domains: 应许提取的域名，从某个域名下提取链接
            deny_domains: 禁止提取的域名，从某个域名下提取链接


scrapy初认识
	
	scrapy是什么？是一个非常强大的python爬虫框架，底层语言使用python实现。既然是框架，肯定已经实现了很多其他的功能，用户只需要将自己的精力放到自己的业务逻辑中即可。多进程、多线程、队列、去重。
	
	安装 pip install scrapy
	
	scrapy工作原理
	
	




















         
scrapy架构：
    1）Scrapy引擎
        Scrapy引擎是整个Scrapy架构的核心，负责控制整个数据处理流程，以及触发一些事务处理。Scrapy引擎与调度器、实体管道、中间件、
        下载器、蜘蛛等组件都有关系，Scrapy引擎处于整个Scrapy框架的中心的位置，对各项组件进行控制及协调。
         
    2）调度器
        调度器主要实现存储待爬取的网址，并确定这些网址的优先级，决定下一次爬取哪个网址等。我们可以把调度器的存储结构看成一个
        优先队列，调度器会从引擎中接收request请求并存入优先队列中，在队列中可能会有多个待爬取的网址，但是这些网址各自具有一定
        的优先级，同时调度器也会过滤掉一些重复的网址，避免重复爬取。当引擎发出请求之后，调度器将优先队列中的下一次要爬取的网址
        返回给引擎，以供引擎进行进一步处理。
         
    3）下载器
        下载器主要实现对网络上要爬取的网页资源进行高速下载，由于该组件需要通过网络进行大量数据的传输，所以该组件的压力负担一般
        会比其他的组件重。下载器下载了对应的网页资源后，会将这些数据传递给Scrapy引擎，再由Scrapy引擎传递给对应的爬虫进行处理。
         
    4）下载中间件
        下载中间件是处于下载器和Scrapy引擎之间的一个特定的组件，主要用于对下载器和Scrapy引擎之间的通信进行处理，在下载中间件中，
        可以加入自定义代码，轻松地实现Scrapy功能的扩展，我们在下载中间件中加入的自定义代码，会在Scrapy引擎与下载器通信的时候调用。
        上一章中我们已经具体的使用过下载中间件来实现IP池和用户代理池的相关功能。
 
    5）蜘蛛（也叫作爬虫，一个Scrapy项目下可能会有多个Spiders爬虫文件）
        蜘蛛（Spider）组件，也叫作爬虫组件，该组件是Scrapy框架中爬虫实现的核心。在一个Scrapy项目中，可以有多个蜘蛛，每个蜘蛛可以
        负责一个或多个特定的网站。蜘蛛组件主要负责接收Scrapy引擎中的response响应（这些响应具体是下载器从互联网中得到的响应然后
        传递到Scrapy引擎中的），在接收了response响应之后，蜘蛛会对这些response响应进行分析处理，然后可以提取出对应的关注的数据，
        也可以提取出接下来需要处理的新网址等信息。
 
    6）爬虫中间件
        爬虫中间件是处于Scrapy引擎与爬虫组件之间的一个特定的组件，主要用于对爬虫组件和Scrapy引擎之间的通信进行处理。同样，在爬虫
        中间件中可以加入一些自定义代码，很轻松地实现Scrapy功能的扩展。在爬虫中间件中加入的自定义代码，会在Scrapy引擎与爬虫组件
        之间进行通信的时候调用。
 
    7）实体管道
        实体管道主要用于接收从蜘蛛组件中提取出来的项目（item），接收后，会对这些item进行对应的处理，常见的处理主要有：清洗、验证、
        存储到数据库中等。
 
scrapy工作流
    Scrapy框架中各项组件的工作流程的具体图示，如图13-2所示。箭头所指的方向即为数据流向的方向。
        首先，Scrapy引擎会将爬虫文件中设置的要爬取的起始网址（默认在start_urls属性中设置）传递到调度器中。随后，依次进行：
        第1步：过程（1）中，主要将下一次要爬取的网址传递给Scrapy引擎，调度器是一个优先队列，里面可能存储着多个要爬取的网，
                调度器会根据各网址的优先级分析出下一次要爬取的网址，然后再传递给Scrapy引擎。
 
        第2步：Scrapy引擎接收到（1）中传过来的网址之后，过程（2）Scrapy引擎主要将网址传递给下载中间件。
 
        第3步：下载中间件接收到Scrapy引擎传过来的网址之后，过程（3）中下载中间件会将对应的网址传递给下载器。
 
        第4步：然后，下载器接收到对应要下载的网址，然后过程（4）会向互联网中对应的网址发送request请求，进行网页的下载。
 
        第5步：互联网中对应的网址接收到request请求之后，会有相应的response响应，随后在过程（5）中将响应返回给下载器。
 
        第6步：下载器接收到响应之后，即完成了对应网页的下载，随后过程（6）会将对应的响应传送给下载中间件。
 
        第7步：下载中间件接收到对应响应之后，会与Scrapy引擎进行通信，过程（7）会将对应的response响应传递给Scrapy引擎。
 
        第8步：Scrapy引擎接收到response响应之后，过程（8）Scrapy引擎会将response响应信息传递给爬虫中间件。
 
        第9步：爬虫中间件接收到对应响应之后，过程（9）爬虫中间件会将响应传递给对应的爬虫进行处理。
 
        第10步：爬虫进行处理之后，大致会有两方面的信息：提取出来的数据和新的请求信息。然后，过程（10）爬虫会将处理后的信息
            传递给爬虫中间件。
        第11步：爬虫中间件接收到对应信息后，过程（11）会将对应信息传递到Scrapy引擎。
 
        第12步：Scrapy引擎接收到爬虫处理后的信息之后，会同时进行过程（12）和过程（13）。在过程（12）中，Scrapy引擎会将提取
            出来的项目实体（item）传递给实体管道（Item Pipeline），由实体管道对提取出来的信息进行进一步处理：过程（13）中，
            Scrapy引擎会将爬虫处理后得到的新的请求信息传递给调度器，由调度器进行进一步网址的调度。随后，再重复执行第1～12步，
            即过程（1）～（13），一直到调度器中没有网址调度或者异常退出为止。以上我们分析了Scrapy框架中各项组件的工作流程，
            此时，我们对Scrapy框架中数据处理的过程就有了比较详细的了解，理清了该过程之后，我们在编写Scrapy爬虫项目的时候，
            思路就能更加清晰。
 
scrapy常用命令：
 
    1、全局命令：scrapy -h
        1) fetch :scrapy fetch http://www.baidu.com. 显示爬虫爬取的过程
            help : scrapy fetch -h
            scrapy fetch --headers --nolog http:?/news.sina.com.cn/
        2) runspider : scrapy runspider --loglevel=INFO first.py 在不依托scrapy的爬虫项目，直接运行一个爬虫文件
        3) setting ：通过命令查看配置信息scrapy settings --配置名
        4）shell : 启动scrapy交互终端，用于开发调试， scrapy shell http://www.baidu.com --nolog
        5) startproject
        6) version ： 获取scrapy版本信息
        7）view ：下载某个网页并用浏览器打开 scrapy view  网址
         
    2、项目命令：
        1)bench : 可以测试本地硬件的性能
        2）gensider : scrapy genspider -l 创建爬虫文件 可用的爬虫模板basic、crawl、csvfeed、xmldeed
            命令格式： scrapy genspider -t 模板  爬虫名 爬取网站域名
        3）check : 对爬虫进行测试  进入到项目目录 scrapy check mysite
        4)crawl : 启动爬虫命令 scrapy crawl 爬虫名  （要进入到爬虫项目）
        5)list : 列出当前项目可使用的爬虫文件
        6)edit : 爬虫编辑命令
        7)parse : 使用默认爬虫和处理函数对指定网站进行爬取 scrapy parse url
         

 scrapy---settings配置文件
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
scrapy爬虫避免被禁止：

    (1）禁止Cookie；
        打开对应的Scrapy爬虫项目中的settings.py文件，可以发现文件中有以下两行代码,去掉注释：
        # Disable cookies (enabled by default)
        COOKIES_ENABLED = False
 
    (2）设置下载延时；
        # Configure a delay for requests for the same website (default: 0)
        # See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
        # See also autothrottle settings and docs DOWNLOAD_DELAY = 0.7
        DOWNLOAD_DELAY = 3  # 下载延迟，单位秒
 
    (3）使用IP池；
        具体方法：
            1）获取代理服务器的IP信息；
            2）在setting.py文件中增加IP池
                IPPOOL = [
                    {"ipaddr" : "host:port"},
                ]
            3)在项目核心目录创建middleware.py
                # middlewares下载中间件
                # 导入随机数模块，目的是随机挑选一个IP池中的IP
                import random
                # 从settings文件（myfirstpjt.settings为settings文件的地址）中导入设置好的IPPOOL
                from myfirstpjt.settings import IPPOOL
                # 导入官方文档中HttpProxyMiddleware对应的模块
                from scrapy.contrib.downloadermiddleware.httpproxy import HttpProxyMiddleware
                 
                class IPPOOLS(HttpProxyMiddleware):
                    # 初始化方法
                    def __init__(self,ip=''):
                        self.ip=ip
                    # process_request()方法，主要进行请求处理
                    def process_request(self,request,spider):
                        # 先随机选择一个IP
                        thisip=random.choice(IPPOOL)
                        # 输出当前选择的IP，便于调试观察
                        print("当前使用的IP是："+thisip["ipaddr"])
                        # 将对应的IP实际添加为具体的代理，用该IP进行爬取
                        request.meta["proxy"]="http://"+thisip["ipaddr"]
            4)配置中间件到settings.py
                在settings.py文件中，与下载中间件相关的配置信息默认如下：
                    # DOWNLOADER_MIDDLEWARES = { 'myfirstpjt.middlewares.MyCustomDownloaderMiddleware': 543, }
                所以现在需要对这一部分配置信息进行如下修改：
                    DOWNLOADER_MIDDLEWARES = { 'myfirstpjt.middlewares.MyCustomDownloaderMiddleware': 543,
                                'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware':123,
                                'myfirstpjt.middlewares.IPPOOLS':125 }
 
    (4）使用用户代理池；
        具体方法：
            1）收集多种浏览器的信息；
             
            2）在setting.py文件中增加用户代理池。
                # 用户代理（user-agent）池设置
                UAPOOL = [ "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)"\
                         Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0", \
                        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0",\
                        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.5" ]
                         
            3)在项目核心目录创建user_agent_middleware.py
                # middlewares下载中间件
                # 导入随机数模块，目的是随机挑选一个IP池中的IP
                import random
                # 从settings文件（myfirstpjt.settings为settings文件的地址）中导入设置好的UAPOOL
                from myfirstpjt.settings import UAPOOL
                # 导入官方文档中HttpProxyMiddleware对应的模块
                from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware
                 
                class UAmid(UserAgentMiddleware):
                    # 初始化方法
                    def __init__(self, ua=''):
                        self.ua = ua
                    # process_request()方法，主要进行请求处理
                    def process_request(self,request,spider):
                        # 先随机选择一个UA
                        thisua = random.choice(UAPOOL)
                        # 输出当前选择的UA，便于调试观察
                        print("当前使用的user_agent是：" + thisua)
                        # 将对应的UA实际添加为具体的代理，用该UA进行爬取
                        request.headers.setdefault("User-Agent", thisua)
                         
            4)配置中间件到settings.py
                在settings.py文件中，与下载中间件相关的配置信息默认如下：
                    # Enable or disable downloader middlewares
                    # See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
                    DOWNLOADER_MIDDLEWARES = {'mysite.middlewares.MyCustomDownloaderMiddleware': 543,
                                             'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware':2,
                                             'mysite.user_agent_middleware.UAmid':1 }
 
            5)其他方法
                使用谷歌Cache,或者分布式爬虫等方式

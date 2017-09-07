from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = "dreamingykl@163.com"
password = "yukunlongjiayou1"
to_addr = "1181281178@qq.com"
smtp_server = "smtp.163.com"

html ='''<html>
<head>
	<title>生日快乐</title>
	<meta charset="utf-8">
<style type="text/css">
	
.am-g {
	margin: 15px auto;
  	width: 100%;
  	height: 80px;
}
.am-u-md-5 {
	 width: 100%;
	 height: 100%;
	 
}
.am-u-md-offset-5 {
    margin-left: 41.66666667%;
}
.right {
	text-align: right;
	float: right;

}

p {
	margin: 0;
}
footer {
	width:100%;
	text-align: center;
	line-height: 30px;
}
</style>
</head>
<body>
	<h1 style="text-align:center">Happy Birthday</h1>
	<audio autoplay="autoplay">
  		<source src="http://115.159.86.195/0915/birth.mp3" >
	</audio>
	<div class="am-g">
		<div class="am-u-md-5">
			<div style="width: 50px; height: 50px;float: left; overflow:hidden"><img src="http://115.159.86.195/0915/1.jpg" style="width:50px"></div>
			<div style="width: 80%; float: left; padding-top:15px;"><p>嘿！今天是你的生日哟</p></div>
		</div>
	</div>
	<div class="am-g">
		<div class="am-u-md-5 right">
			<div style="width: 50px; height:50px;float: right;"><img src="http://115.159.86.195/0915/0.jpg" style="width:50px"></div>
			<div style="width: 80%; float: right; padding-top:15px;">对哟，你有给我准备礼物么？</div>
		</div>
	</div>

	<div class="am-g">
		<div class="am-u-md-5">
			<div style="width: 50px; height: 50px;float: left; overflow:hidden"><img src="http://115.159.86.195/0915/1.jpg" style="width:50px"></div>
			<div style="width: 80%; float: left; padding-top:15px;"><p>当然啦！我可是做了充足的准备呢</p></div>
		</div>
	</div>
	<div class="am-g">
		<div class="am-u-md-5 right">
			<div style="width: 50px; height:50px;float: right;"><img src="http://115.159.86.195/0915/0.jpg" style="width:50px"></div>
			<div style="width: 80%; float: right; padding-top:15px;">是么？有些期待呢</div>
		</div>
	</div>

	<div class="am-g">
		<div class="am-u-md-5">
			<div style="width: 50px; height: 50px;float: left; overflow:hidden"><img src="http://115.159.86.195/0915/1.jpg" style="width:50px"></div>
			<div style="width: 80%; float: left; padding-top:20px;">别急别急，我先给你讲个段子吧</div>
		</div>
	</div>
	<div class="am-g">
		<div class="am-u-md-5 right">
			<div style="width: 50px; height:50px;float: right;"><img src="http://115.159.86.195/0915/0.jpg" style="width:50px"></div>
			<div style="width: 80%; float: right; padding-top:20px;">好哦，什么段子，讲来听听</div>
		</div>
	</div>

	<div class="am-g">
		<div class="am-u-md-5">
			<div style="width: 50px; height: 50px;float: left; overflow:hidden"><img src="http://115.159.86.195/0915/1.jpg" style="width:50px"></div>
			<div style="width: 80%; float: left; padding-top:20px;"><p>孩子：<small style="font-family:STKaiti">妈妈，我什么时候过生日呀？</small><br>妈妈：<small style="font-family:STKaiti">九月十五日</small><br>孩子：<small style="font-family:STKaiti">那你呢？</small><br>妈妈：<small style="font-family:STKaiti">九月十日</small><br>孩子：<small style="font-family:STKaiti">呀，妈妈，你五天就把我生下来啦？！</small></p></div>
		</div>
	</div>
	<div class="am-g">
		<div class="am-u-md-5 right">
			<div style="width: 50px; height:50px;float: right;"><img src="http://115.159.86.195/0915/0.jpg" style="width:50px"></div>
			<div style="width: 80%; float: right; padding-top:20px;">哈哈！小婊砸，你智商呢？</div>
		</div>
	</div>

	<div class="am-g">
		<div class="am-u-md-5">
			<div style="width: 50px; height: 50px;float: left; overflow:hidden"><img src="http://115.159.86.195/0915/1.jpg" style="width:50px"></div>
			<div style="width: 80%; float: left; padding-top:20px;">
				<p>嘿嘿，还有还有，我还给你准备了一首诗呢</p>
			</div>
		</div>
	</div>
	<div class="am-g">
		<div class="am-u-md-5 right">
			<div style="width: 50px; height:50px;float: right;"><img src="http://115.159.86.195/0915/0.jpg" style="width:50px"></div>
			<div style="width: 80%; float: right; padding-top:20px;">哟~小婊砸，还会写诗呢！厉害了</div>
		</div>
	</div>
	
	<div class="am-g">
		<div class="am-u-md-5">
			<div style="width: 50px; height: 50px;float: left; overflow:hidden"><img src="http://115.159.86.195/0915/1.jpg" style="width:50px"></div>
			<div style="width: 80%; float: left; padding-top:20px;">
				<p>可听好喽：<br>
				<small style="font-family:STKaiti">鹊鸟登枝深院，</small>
				<small style="font-family:STKaiti">晨风吹过花墙。</small><br>
				<small style="font-family:STKaiti">夏来浓绿映纱窗。</small>
				<small style="font-family:STKaiti">镜开娇影好，帘动小诗香</small>
				</p>
			</div>
		</div>
	</div>
	<div class="am-g">
		<div class="am-u-md-5 right">
			<div style="width: 50px; height:50px;float: right;"><img src="http://115.159.86.195/0915/0.jpg" style="width:50px"></div>
			<div style="width: 80%; float: right; padding-top:20px;">不错不错，不过这不是首词么？</div>
		</div>
	</div>

	<div class="am-g">
		<div class="am-u-md-5">
			<div style="width: 50px; height: 50px;float: left; overflow:hidden"><img src="http://115.159.86.195/0915/1.jpg" style="width:50px"></div>
			<div style="width: 80%; float: left; padding-top:20px;">
				<p>呀，大行不顾细谨的啦~<br></p>
			</div>
		</div>
	</div>
	<div class="am-g">
		<div class="am-u-md-5 right">
			<div style="width: 50px; height:50px;float: right;"><img src="http://115.159.86.195/0915/0.jpg" style="width:50px"></div>
			<div style="width: 80%; float: right; padding-top:20px;">好吧，好吧</div>
		</div>
	</div>


	<div class="am-g">
		<div class="am-u-md-5">
			<div style="width: 50px; height: 50px;float: left; overflow:hidden"><img src="http://115.159.86.195/0915/1.jpg" style="width:50px"></div>
			<div style="width: 80%; float: left; padding-top:20px;">
				<p>接下来给你唱首歌吧~<br></p>
			</div>
		</div>
	</div>
	<div class="am-g">
		<div class="am-u-md-5 right">
			<div style="width: 50px; height:50px;float: right;"><img src="http://115.159.86.195/0915/0.jpg" style="width:50px"></div>
			<div style="width: 80%; float: right; padding-top:20px;">可以呀，你还会唱歌啊？还真没看出来</div>
		</div>
	</div>


	<div class="am-g">
		<div class="am-u-md-5">
			<div style="width: 50px; height: 50px;float: left; overflow:hidden"><img src="http://115.159.86.195/0915/1.jpg" style="width:50px"></div>
			<div style="width: 80%; float: left; padding-top:20px;">
				<p><span><a href="http://115.159.86.195/0915/horse.mp3">歌曲</a></span>
				<audio id="musicaudio">
  					<source src="http://115.159.86.195/0915/horse.mp3" >
				</audio></p>
			</div>
		</div>
	</div>
	<div class="am-g">
		<div class="am-u-md-5 right">
			<div style="width: 50px; height:50px;float: right;"><img src="http://115.159.86.195/0915/0.jpg" style="width:50px"></div>
			<div style="width: 80%; float: right; padding-top:20px;">额，这。。。#_#)<br/>
			<img src="http://115.159.86.195/0915/ganga.jpg" style="width:50px">
			</div>
		</div>
	</div>


	<div class="am-g">
		<div class="am-u-md-5">
			<div style="width: 50px; height: 50px;float: left; overflow:hidden"><img src="http://115.159.86.195/0915/1.jpg" style="width:50px"></div>
			<div style="width: 80%; float: left; padding-top:20px;">
				<p>啊，我刚刚是试试嗓子，下面开始唱了<br>
					<span><a href="http://115.159.86.195/0915/birthday.mp3">歌曲</a></span>
					<audio id="musikaudio">
  						<source src="http://115.159.86.195/0915/birthday.mp3" >
					</audio>
				</p>
			</div>
		</div>
	</div>
	<div class="am-g">
		<div class="am-u-md-5 right">
			<div style="width: 50px; height:50px;float: right;"><img src="http://115.159.86.195/0915/0.jpg" style="width:50px"></div>
			<div style="width: 80%; float: right; padding-top:20px;">很好听的音乐，只是这哪是你唱的啊</div>
		</div>
	</div>

	<div class="am-g">
		<div class="am-u-md-5">
			<div style="width: 50px; height: 50px;float: left; overflow:hidden"><img src="http://115.159.86.195/0915/1.jpg" style="width:50px"></div>
			<div style="width: 80%; float: left; padding-top:20px;">
				<p>你也知道我唱歌不好听，所以还是不要听了，嘿嘿~<br></p>
			</div>
		</div>
	</div>
	<div class="am-g">
		<div class="am-u-md-5 right">
			<div style="width: 50px; height:50px;float: right;"><img src="http://115.159.86.195/0915/0.jpg" style="width:50px"></div>
			<div style="width: 80%; float: right; padding-top:20px;">嗯，很喜欢这音乐，谢谢啦</div>
		</div>
	</div>

	<div class="am-g">
		<div class="am-u-md-5">
			<div style="width: 50px; height: 50px;float: left; overflow:hidden"><img src="http://115.159.86.195/0915/1.jpg" style="width:50px"></div>
			<div style="width: 80%; float: left; padding-top:20px;">
				<p>谢什么，多见外，曾经的美好彼此珍惜便是<br>
				多年不见，一见如故嘛</p>
			</div>
		</div>
	</div>
	<div class="am-g">
		<div class="am-u-md-5 right">
			<div style="width: 50px; height:50px;float: right;"><img src="http://115.159.86.195/0915/0.jpg" style="width:50px"></div>
			<div style="width: 80%; float: right; padding-top:20px;">对着呢，小伙子</div>
		</div>
	</div>

	<div class="am-g">
		<div class="am-u-md-5">
			<div style="width: 50px; height: 50px;float: left; overflow:hidden"><img src="http://115.159.86.195/0915/1.jpg" style="width:50px"></div>
			<div style="width: 80%; float: left; padding-top:20px;">
				<p>准备了这些，希望你喜欢，最重要的，开心就好<br>
				<small style="font-family:STKaiti">(平时也聊不上天，我就模拟上天啦)</small></p>
			</div>
		</div>
	</div>
	<div class="am-g">
		<div class="am-u-md-5 right">
			<div style="width: 50px; height:50px;float: right;"><img src="http://115.159.86.195/0915/0.jpg" style="width:50px"></div>
			<div style="width: 80%; float: right; padding-top:20px;">。。。</div>
		</div>
	</div>

	<div class="am-g">
		<div class="am-u-md-5">
			<div style="width: 50px; height: 50px;float: left; overflow:hidden"><img src="http://115.159.86.195/0915/1.jpg" style="width:50px"></div>
			<div style="width: 80%; float: left; padding-top:20px;">
				<p>啊，祝福到，我便要走了<br><small style="font-family:STKaiti">（相见即是缘，无论缘聚缘散，你我友谊不断）</small></p>
			</div>
		</div>
	</div>
	<div class="am-g">
		<div class="am-u-md-5 right">
			<div style="width: 50px; height:50px;float: right;"><img src="http://115.159.86.195/0915/0.jpg" style="width:50px"></div>
			<div style="width: 80%; float: right; padding-top:20px;">好的，谢谢你的祝福，慢走~~</div>
		</div>
	</div>


	<div class="am-g" style="text-align:center">
		<footer>
			<p><a href="http://115.159.86.195/0915/index.html" style="text-decoration:none;">Birthday Celebration</a><br/>
    			<small>© Copyright James Mike. 2017.9.15</small>
  			</p>
		</footer>
	</div>

	
</body>
</html>

'''

msg = MIMEText(html, 'html', 'utf-8')
msg['From'] = _format_addr('JamesMike <%s>' % '19960915@cy.com')
msg['To'] = _format_addr('明月寄诗友 <%s>' % to_addr)
msg['Subject'] = Header('来自云端的：生日祝福', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
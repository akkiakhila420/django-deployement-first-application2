from django.shortcuts import render
from django.http import HttpResponse;

# Create your views here.
def display(request):   #view-function
    #ss--->is html-data/code
    print("welcome/ url is requested&display() is executed")
    ss='''
        <center>
            <h2 style="color:Green;">
            Hello User,welcome to Django First-Project First-App
            </h2>
            <hr/>
        </center>
        ''';
    return HttpResponse(ss);
def show(request):  #view-function
    ss='''
    <!--
	HTML webpage to display "welcome-Message" with different Headings 
    -->
<html>
<head>
	<title>***welcome-page***</title>
	
	<style>
	h1{
		color:Blue;
	}
	h2{
		color:Green;
	}
	h3{
		color:Red;
	}
	h4{
		color:Orange;
	}
	h5{
		color:Pink;
	}
	h6{
		color:violet;
	}
	h1,h3,h5{
		background-color:yellow;
	}
	h2,h4,h6{
		background-color:lightgreen;
	}
	</style>
	</head>
<body>
<center>
	<h1>Welcome to DjANGO HTML webpage</h1>
	<hr color="brown" width="95%" align=""/>
	<h2>Welcome to DjANGO HTML webpage</h2>
	<hr color="brown" width="85%"/>
	<h3>Welcome to DjANGO HTML webpage</h3>
	<hr color="brown" width="75%"/>
	<h4>Welcome to DjANGO HTML webpage</h4>
	<hr color="brown" width="65%"/>
	<h5>Welcome to DjANGO HTML webpage</h5>
	<hr color="brown" width="55%"/>
	<h6>Welcome to DjANGO HTML webpage</h6>
	<hr color="brown" width="45%"/>
</center>
	
</body>
</html>

    ''';
    return HttpResponse(ss);
def hello(request):
    print("hello/ url is required &hello() is executed")
    ss='''
    <html>
    <head>
    <title>Hello webpage</title>
    <style>
    h1{
        color:Blue;
        width:90%
    }
    h2{
        color:Green;
        width:80%;
    }
    h3{
        color:Red;
        width:70%;
    }
    h1,h2,h3{
        background-color:lightblue;
        border:2px Solid Brown;
    }
    </style>
    </head>
    <body>
    <center>
        <h1>Hello User..!!!</h1>
        <hr color='brown' width=80%/>
        <h2>Welcome to Django-App</h2>
        <hr color='brown' width='60%'/>
        <h3>Have a nice day..</h3>
        <hr color='brown' width='40%'/>
        
    </center>
    </body>
    </html>
    ''';
    return HttpResponse(ss);
import time;
def senddatetime(request):
    print("dtime/url is requested &senddatetime() is executed")
    ct=time.ctime()
    print("Client Request Date &time on server::",ct);
    ss='''
    <html>
        <head>
        <title>Date-time webpage</title>
        <style>
        h1{
            color:Blue;
            width:90%;
        }
        h2{
            color:green;
            width:80%;
        }
        h3{
            color:red;
            width:70%;
        }
        h1,h2,h3{
            background-color:lightgreen;
            border:2px solid Brown;
        }
        </style>
        </head>
            <center>
                <h1>welcome to Django-User...!!</h1>
                <hr color="brown" width="80%">
                <h2>Server-Date& time::</h2>
                <hr color="brown" width="70%">
                <h3>''',ct,'''</h3>
                <hr color="brown" width="60%"/>
            </center>
        </body>
    </html>
    ''';
    return HttpResponse(ss);
                

#single-view &multiple-urls
def demo(request):
    print("multiple-Requests-URLs same response")
    htmldate='''<center>
        <h1>welcome Demo User!!!</h1>
        <hr/>
        <h2>This is same-output for diff-multiple-request-urls</h2>
        <hr/>
        <h3>Have a Great Day...</h3>
        </center>''';
    return HttpResponse(htmldate);
    
#default-url-request-view-function
def homepage(request):
    htmldata='''<center>
        <h1>Welcome to DEFAULT Home-page!!</h1>
        <hr/>
        <h2>Your Request page is Not-Found...</h2>
        <hr/>
        <h3>Plz try other URL or Link!!!</h3>
    </center>''';
    return HttpResponse(htmldata);
      
        
        
        

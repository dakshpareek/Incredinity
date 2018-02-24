print("Content-type:text/html\r\n\r\n")
print('''<!doctype html>
<!doctype html>


<html lang="en" class="no-js">
<head>
	<title>Incredinity</title>

	<meta charset="utf-8">

	<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
	<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">

	<link href='http://fonts.googleapis.com/css?family=Roboto:400,100,100italic,300,300italic,400italic,500,500italic,700,700italic' rel='stylesheet' type='text/css'>

	<link rel="stylesheet" type="text/css" href="/css/bootstrap.css" media="screen">	
	<link rel="stylesheet" type="text/css" href="/css/magnific-popup.css" media="screen">
	<link rel="stylesheet" type="text/css" href="/css/font-awesome.css" media="screen">
	<link rel="stylesheet" type="text/css" href="/css/flexslider.css" media="screen">
	<link rel="stylesheet" type="text/css" href="/css/style.css" media="screen">
	<link rel="stylesheet" type="text/css" href="/css/responsive.css" media="screen">

</head>
<body>

	<!-- Container -->
	<div id="container">
		<!-- Header
		    ================================================== -->
		<header>
			<div class="logo-box">
				<a class="logo" href="index.py"><img alt="" width="90%" src="images/logo.jpg"></a>
			</div>
			
			<a class="elemadded responsive-link" href="#">Menu</a>

			<div class="menu-box">
				<ul class="menu">
					<li><a  href="#"><span>Home</span></a></li>		
					<li><a class="active" href="index.py"><span>Movies</span></a></li>
					<li><a href="about.html"><span>About</span></a></li>
				</ul>				
			</div>

		</header>

		<!-- content 
			================================================== -->
		<div id="content">
			<div class="inner-content">
				<div class="single-project">
					<div class="single-box">
						<div class="single-box-content">
							<div class="project-post-content">

								<div class="flexslider">
									<ul class="slides">
''')
import pickle,os,cgi
from pickle import load

import cgi, cgitb
f=open("movies_data.txt","rb")
data=pickle.load(f)

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
id = int(form.getvalue('id'))


name=data[id][0]
img=data[id][1]
final=data[id][2]
for i in img:
	print('''<li><img src={} /></li>'''.format(i))
print('''
									</ul>
								</div>

							
							</div>
						</div>
						<div class="sidebar">
							<div class="post-info">
''')
print('''
								<h1>{}</h1>
								<ul>
									<li>
										<span><i class="fa fa-link"></i></span><a href="{}">Download</a>
									</li>
'''.format(name,final))
print('''				
								</ul>
							</div>
							
					
						</div>
					</div>

				</div>
			</div>
		</div>
		<!-- End content -->

	</div>
	<!-- End Container -->

	<div class="preloader">
		<img alt="" src="images/preloader.gif">
	</div>

	<script type="text/javascript" src="js/jquery.min.js"></script>
	<script type="text/javascript" src="js/jquery.migrate.js"></script>
	<script type="text/javascript" src="js/jquery.imagesloaded.min.js"></script>
	<script type="text/javascript" src="js/bootstrap.js"></script>
	<script type="text/javascript" src="js/jquery.flexslider.js"></script>
	<script type="text/javascript" src="js/retina-1.1.0.min.js"></script>
	<script type="text/javascript" src="js/jquery.nicescroll.min.js"></script>
	<script type="text/javascript" src="js/script.js"></script>

</body>
</html>
''')

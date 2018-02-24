import pickle
import cgi, cgitb
# Create instance of FieldStorage 
form = cgi.FieldStorage() 
# Get data from fields
try:
	id=int(form.getvalue('id'))
	if id < 0:
		id=0
except:
	id=0
	pass

print("Content-type:text/html\r\n\r\n")
print('''
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
				<a class="logo" href="index.py"><img alt=""  width="90%" src="images/logo.jpg"></a>
			</div>
			
			<a class="elemadded responsive-link" href="#">Menu</a>

			<div class="menu-box">
				<ul class="menu">
					<li><a class="active" href="#"><span>Home</span></a></li>		
					<li><a href="index.py"><span>Movies</span></a></li>
					<li><a href="index.py?id={}"><span>Next Page</span></a></li>
					<li><a href="index.py?id={}"><span>Previous Page</span></a></li>
					<li><a href="about.html"><span>About</span></a></li>
				</ul>				
			</div>

		</header>
		<!-- End Header -->

		<!-- content 
			================================================== -->
		<div id="content">
			<div class="inner-content">
				<div class="portfolio-page">
					<div class="portfolio-box">
'''.format(id+12,id-12))

#print('''<script>alert("{}");</script> '''.format(id))


f=open("movies_data.txt","rb")
data=pickle.load(f)
#print(data[0][3])
#print(data[0][1])
for j,i in enumerate(data[id:id+12]):
	print('''<div class="project-post web-design illustration">''')
	ime=i[3].encode('utf8')
	tit=i[0].encode('utf8')
	print('''<img class="b-lazy" src="{}">
	<div class="hover-box">
    <div class="project-title">
    <h2>{}</h2>'''.format(ime,tit))
	print('''<div><form method='post' action='movie.py'>''')
	print('''<a href="movie.py?id={}"><i class="fa fa-arrow-right"></i></a></form></div></div></div></div>'''.format(j+id))

	
print('''						
					</div>
				</div>
			</div>
		</div>
		<!-- End content -->

	</div>
	<!-- End Container -->

	<div class="info-box">
		<a class="info-toggle" style="color:#ffff;font-weight:bold;" href="daksh.com">More Movies</a>
		<!-- <a class="info-toggle" href="#"><i class="fa fa-arrow-circle-o-right"></i></a> -->
		<div class="info-content">
			<ul>
				
				<li><i class="fa fa-envelope"></i><a href="index.py?id={}">Next Page</a></li>
				<li><i class="fa fa-home"></i><a href="index.py?id={}">Previous Page</a></li>
			</ul>
		</div>
	</div>

	<div class="preloader">
		<img alt="" src="images/preloader.gif">
	</div>

	<script type="text/javascript" src="js/jquery.min.js"></script>
	<script type="text/javascript" src="js/jquery.migrate.js"></script>
	<script type="text/javascript" src="js/jquery.magnific-popup.min.js"></script>
	<script type="text/javascript" src="js/bootstrap.js"></script>
	<script type="text/javascript" src="js/jquery.imagesloaded.min.js"></script>
  	<script type="text/javascript" src="js/jquery.isotope.min.js"></script>
	<script type="text/javascript" src="js/retina-1.1.0.min.js"></script>
	<script type="text/javascript" src="js/jquery.nicescroll.min.js"></script>
	<script type="text/javascript" src="js/script.js"></script>


</body>
</html>
'''.format(id+12,id-12))

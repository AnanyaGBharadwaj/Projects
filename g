<html>
<head>
<title>Prog3</title>
<style>
form{
text-align:center;
}
</style>
<script>
function check()
{
name=document.getElementById("name").value;
if(name.length<6)
{
alert("Should be atleast 6 char");
return false
}
password=document.getElementById("password").value;
if(password.length<6)
{
alert("Should be atleast 6 char");
return false
}
email=document.getElementById("email").value;
if(!email.match(/^[A-Za-z0-9]+@[A-Za-z0-9]+\.[A-Za-z0-9]+$/))
{
alert("Enter email correctly");
return false
}
else
alert("Form submitted");
return true
}
</script>
</head>
<body>
<form onsubmit="check()">
Name:<input type="text" id="name" name="name" placeholder="Enter your name here">
<br/><br/>
Password:<input type="password" id="password" name="password">
<br/><br/>
Email:<input type="text" id="email" name="email">
<br/><br/>
<input type="submit"></input>
</form>
</body>
</html>

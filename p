<html>
<head>
<title>prog6</title>
<script type="text/javascript">
function showHelp(message)
{
document.getElementById("helpBox").value=message;
}
function clearHelp()
{
document.getElementById("helpBox").value="";
}
function validateForm(event)
{
var email=document.getElementById("email").value;
var password=document.getElementById("password").value;
var emailPattern=/^[^@]+@[^@]+\.[a-z]{2,}$/i;
if(!emailPattern.test(email))
{
alert("Enter email correctly");
event.preventDefault();
return false
}
if(password.length<6)
{
alert("atleast 6 char");
event.preventDefault();
return false
}
else
{
alert("form submitted");
return true
}
}
window.onload=function()
{
document.getElementById("name").addEventListener("mouseover",function()
{
showHelp("Enter your name");
document.getElementById("name").addEventListener("mouseout",clearHelp);
});
document.getElementById("email").addEventListener("mouseover",function(){
showHelp("Enter the email correctly");
});
document.getElementById("email").addEventListener("mouseout",clearHelp);
document.getElementById("password").addEventListener("mouseover",function(){
showHelp("Enter the password correctly");
});
document.getElementById("password").addEventListener("mouseout",clearHelp);
document.getElementById("userid").addEventListener("mouseover",function(){
showHelp("Enter the id correctly like anu123");
});
document.getElementById("userid").addEventListener("mouseout",clearHelp);
document.getElementById("userform").addEventListener("submit",validateForm);
};
</script>
</head>
<body>
<h2>User reg form</h2>
<form id="userform" action="#" method="post">
Name:<input type="text" name="name" id="name">
<br/><br/>
Email:<input type="text" name="email" id="email">
<br/><br/>
Password:<input type="password" name="password" id="password">
<br/><br/>
User ID:<input type="text" name="userid" id="userid">
<br/><br/>
<b>Help Box:</b><br/>
<textarea id="helpBox" cols="40" rows="4" readonly="readonly"></textarea>
</br></br>
<input type="submit" value="register">
</form>
</body>
</html>


